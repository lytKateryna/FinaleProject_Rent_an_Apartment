from rest_framework import viewsets
from drf_spectacular.utils import extend_schema, OpenApiExample
from rest_framework import viewsets

from rent_ads.models import Booking
from rent_ads.serializers.booking import BookingSerializer
from rent_ads.permissions import IsBookingOwnerOrLandlord


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsBookingOwnerOrLandlord]

    def perform_create(self, serializer):
        serializer.save(tenant=self.request.user)

        @extend_schema(
            examples=[
                OpenApiExample(
                    'Booking example',
                    value={
                        "listing": 3,
                        "start_date": "2026-06-01",
                        "end_date": "2026-06-10"
                    },
                    request_only=True,
                ),
            ]
        )
        def create(self, request, *args, **kwargs):
            return super().create(request, *args, **kwargs)

