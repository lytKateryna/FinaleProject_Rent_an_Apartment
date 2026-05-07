from django.db import models
from django.conf import settings
from rent_ads.models.listing import Listing

class ListingView(models.Model):

    # Listing
    listing = models.ForeignKey(
        Listing,
        on_delete=models.CASCADE,
        related_name='views'
    )

    # User
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='listing_views',
        null=True,
        blank=True
    )
    session_key = models.CharField(
        max_length=40,
        null=True,
        blank=True
    )

    # Date
    viewed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Listing View"
        verbose_name_plural = "Listing Views"
        ordering = ['-viewed_at']

    def __str__(self):
        return f'{self.listing.title} viewed'