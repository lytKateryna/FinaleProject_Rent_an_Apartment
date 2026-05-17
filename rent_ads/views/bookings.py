from drf_spectacular.utils import extend_schema, OpenApiExample
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rent_ads.models import Booking
from rent_ads.serializers.booking import BookingSerializer
from rent_ads.permissions import IsBookingOwnerOrLandlord
from django.contrib.auth import get_user_model

User = get_user_model()


class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    permission_classes = [IsBookingOwnerOrLandlord]

    def get_queryset(self):
        user = self.request.user

        if user.is_anonymous:
            return Booking.objects.none()

        if user.is_superuser:
            return Booking.objects.all()

        user_role = getattr(user, 'role', None)

        if user_role == 'tenant':
            return Booking.objects.filter(tenant=user)
        if user_role == 'landlord':
            return Booking.objects.filter(listing__owner=user)
        return Booking.objects.none()

    def perform_create(self, serializer):
        user = self.request.user
        listing = serializer.validated_data['listing']

        if user.role != 'tenant':
            raise ValidationError("Only tenants can create bookings.")

        if listing.owner == user:
            raise ValidationError("You cannot book your own listing.")

        serializer.save(tenant=user)

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
