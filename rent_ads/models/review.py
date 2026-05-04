from django.db import models
from django.contrib.auth.models import User
from rent_ads.models.listing import Listing

class Review(models.Model):
    # Basic Information
    listing = models.ForeignKey(
        Listing,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    rating = models.PositiveIntegerField()
    comment = models.TextField()

    # User
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    # Date
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)









