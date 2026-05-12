from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from rent_ads.models import ListingView
from rent_ads.serializers.listing_view import ListingViewSerializer


class ListingViewViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = ListingView.objects.all()
    serializer_class = ListingViewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]







