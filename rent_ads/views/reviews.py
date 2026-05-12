from rest_framework import viewsets
from rent_ads.models import Review
from rent_ads.serializers.review import ReviewSerializer
from rest_framework.permissions import IsAuthenticated


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)