from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rent_ads.permissions import IsReviewOwnerOrReadOnly
from rent_ads.models import Review
from rent_ads.serializers.review import ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsReviewOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
