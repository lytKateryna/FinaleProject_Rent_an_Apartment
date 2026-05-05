from rest_framework import serializers
from rent_ads.models.booking import Booking


class BookingSerializer(serializers.ModelSerializer):
    tenant = serializers.ReadOnlyField(source='tenant.username')

    class Meta:
        model = Booking
        fields = [
            'id',
            'listing',
            'tenant',
            'start_date',
            'end_date',
            'status',
            'created_at',
        ]