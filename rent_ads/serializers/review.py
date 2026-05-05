from rest_framework import serializers
from rent_ads.models.review import Review


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Review
        fields = [
            'id',
            'listing',
            'user',
            'rating',
            'comment',
            'created_at',
        ]
