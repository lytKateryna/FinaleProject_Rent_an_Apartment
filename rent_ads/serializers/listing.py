from rest_framework import serializers
from rent_ads.models.listing import Listing
from rent_ads.serializers.address import AddressSerializer


class ListingListSerializer(serializers.ModelSerializer):
    views_count = serializers.IntegerField(read_only=True)
    class Meta:
        model = Listing
        fields = [
            'id',
            'title',
            'price',
            'rooms',
            'capacity',
            'area',
            'views_count',
        ]


class ListingDetailSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    address = AddressSerializer(read_only=True)
    views_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Listing
        fields = [
            'id',
            'title',
            'description',
            'address',
            'price',
            'rooms',
            'area',
            'capacity',
            'property_type',
            'is_active',
            'owner',
            'created_at',
            'updated_at',
            'views_count',
        ]


class ListingCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = [
            'title',
            'description',
            'address',
            'address',
            'price',
            'rooms',
            'area',
            'capacity',
            'property_type',
            'is_active',
        ]

