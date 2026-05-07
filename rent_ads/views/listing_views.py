from rest_framework import viewsets
from rent_ads.models import ListingView
from rent_ads.serializers.listing_view import ListingViewSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rent_ads.permissions import IsOwnerOrReadOnly


class ListingViewViewSet(viewsets.ModelViewSet):
    queryset = ListingView.objects.all()
    serializer_class = ListingViewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(user=self.request.user)
        else:
            if not self.request.session.session_key:
                self.request.session.save()

            serializer.save(session_key=self.request.session.session_key)



