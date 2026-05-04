from django.db import models
from django.contrib.auth.models import User
from rent_ads.models.listing import Listing


class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('rejected', 'Rejected'),
        ('completed', 'Completed'),
    ]

    # Basic Information
    listing = models.ForeignKey(
        Listing,
        on_delete=models.CASCADE
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES
    )

    # User
    tenant = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='bookings'
    )

    # Date
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.listing.title} - {self.tenant.username}'