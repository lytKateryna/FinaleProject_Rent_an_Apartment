from django.db.models import Q
from drf_spectacular.utils import extend_schema, OpenApiExample
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError, PermissionDenied
from rent_ads.models import Booking
from rent_ads.serializers.booking import BookingSerializer
from rent_ads.permissions import IsBookingOwnerOrLandlord
from django.contrib.auth import get_user_model

User = get_user_model()


class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated, IsBookingOwnerOrLandlord]

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
        start_date = serializer.validated_data['start_date']
        end_date = serializer.validated_data['end_date']

        if listing.owner == user:
            raise ValidationError("You cannot book your own listing.")

        overlapping_bookings = Booking.objects.filter(listing=listing).exclude(
            status='cancelled'
        ).filter(
            Q(start_date__lte=end_date) &
            Q(end_date__gte=start_date)
        )

        if overlapping_bookings.exists():
            raise ValidationError(
                "Unfortunately, this property is already booked for these dates."
            )

        serializer.save(tenant=user)

    def destroy(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            raise PermissionDenied(
                "Only administrators can delete bookings."
            )

        return super().destroy(request, *args, **kwargs)

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
