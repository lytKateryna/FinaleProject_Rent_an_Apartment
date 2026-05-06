from rest_framework import viewsets
from rent_ads.models import Booking
from rent_ads.serializers.booking import BookingSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def perform_create(self, serializer):
        serializer.save(tenant=self.request.user)