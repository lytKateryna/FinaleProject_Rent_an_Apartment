from rest_framework import viewsets
from rent_ads.models import Listing
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rent_ads.serializers.listing import (
    ListingListSerializer,
    ListingDetailSerializer,
    ListingCreateUpdateSerializer,
)


class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.filter(is_active=True)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]


    filterset_fields = {
        'price': ['lte', 'gte'],
        'rooms': ['lte', 'gte'],
        'city':['exact'],
        'district':['exact'],
        'property_type':['exact'],
    }
    search_fields = ['title', 'description']
    ordering_fields = ['price', 'created_at']
    ordering = ['-created_at']

    def get_serializer_class(self):
        if self.action == 'list':
            return ListingListSerializer
        elif self.action in ['create', 'update', 'partial_update']:
            return ListingCreateUpdateSerializer
        return ListingDetailSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

