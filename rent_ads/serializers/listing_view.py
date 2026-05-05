from rest_framework import serializers
from rent_ads.models.listing_view import ListingView


class ListingViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListingView
        fields = '__all__'
