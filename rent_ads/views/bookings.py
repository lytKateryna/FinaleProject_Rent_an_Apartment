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