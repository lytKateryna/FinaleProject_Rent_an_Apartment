from django.db.models import Count
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rent_ads.models import Listing, SearchHistory, ListingView

from rent_ads.serializers.listing import (
    ListingListSerializer,
    ListingDetailSerializer,
    ListingCreateUpdateSerializer,
)
from rent_ads.permissions import IsOwnerOrReadOnly, IsLandlordOrReadOnly


class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.filter(is_active=True)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    permission_classes = [
        IsLandlordOrReadOnly,
        IsOwnerOrReadOnly
    ]

    filterset_fields = {
        'price': ['gte', 'lte'],
        'rooms': ['gte', 'lte'],
        'address__city': ['exact'],
        'address__district': ['exact'],
        'property_type': ['exact'],
    }
    search_fields = [
        'title',
        'description',
        'address__city',
        'address__district',
        'address__street',
    ]
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

    def retrieve(self, request, *args, **kwargs):
        listing = self.get_object()
        ListingView.objects.create(
            listing=listing,
            user=request.user if request.user.is_authenticated else None
        )
        serializer = self.get_serializer(listing)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        search_query = request.query_params.get('search')

        if search_query:
            SearchHistory.objects.create(
                user=request.user if request.user.is_authenticated else None,
                keyword=search_query
            )

        return super().list(request, *args, **kwargs)

    @action(detail=False, methods=['get'])
    def popular(self, request):
        listings = Listing.objects.filter(is_active=True).annotate(
            views_count=Count('views')
        ).order_by('-views_count')

        serializer = self.get_serializer(listings, many=True)
        return Response(serializer.data)
