from rest_framework import viewsets
from rent_ads.models import Listing
from rent_ads.serializers.listing import (
    ListingListSerializer,
    ListingDetailSerializer,
    ListingCreateUpdateSerializer,
)


class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ListingListSerializer
        elif self.action in ['create', 'update', 'partial_update']:
            return ListingCreateUpdateSerializer
        return ListingDetailSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

