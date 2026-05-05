from rest_framework import serializers
from rent_ads.models.listing import Listing


class ListingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = [
            'id',
            'title',
            'price',
            'rooms',
            'capacity',
            'area',
        ]


class ListingDetailSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Listing
        fields = [
            'id',
            'title',
            'description',
            'address',
            'city',
            'district',
            'price',
            'rooms',
            'area',
            'capacity',
            'property_type',
            'is_active',
            'owner',
            'created_at',
            'updated_at',
        ]


class ListingCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = [
            'title',
            'description',
            'address',
            'city',
            'district',
            'price',
            'rooms',
            'area',
            'capacity',
            'property_type',
            'is_active',
        ]
