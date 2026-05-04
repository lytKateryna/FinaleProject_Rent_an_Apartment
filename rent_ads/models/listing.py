from django.db import models
from django.contrib.auth.models import User


class Listing(models.Model):
    Property_Types = [
        ('apartment', 'Apartment'),
        ('house', 'House'),
        ('studio', 'Studio'),
    ]

    # Basic Information
    title = models.CharField(max_length=255)
    description = models.TextField()

    # Location
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    district = models.CharField(max_length=100)

    # Price and Details
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rooms = models.IntegerField()
    area = models.FloatField()
    capacity = models.IntegerField()

    # Property Type
    property_type = models.CharField(max_length=100, choices=Property_Types)

    # Status
    is_active = models.BooleanField(default=True)

    # Owner
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    # Date
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title