from rest_framework import serializers
from rent_ads.models.address import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
            'id',
            'country',
            'city',
            'district',
            'street',
            'house_number',
            'postal_code',
        ]