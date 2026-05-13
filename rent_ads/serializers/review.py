from rest_framework import serializers
from rent_ads.models.review import Review
from rent_ads.models.booking import Booking


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
    def validate(self, attrs):
        request = self.context['request']
        listing = attrs['listing']

        has_booking = Booking.objects.filter(
            tenant=request.user,
            listing=listing,
            status='completed'
        ).exists()

        if not has_booking:
            raise serializers.ValidationError(
                'You can leave a review only after confirmed booking.'
            )
        return attrs
