from django.db import models


class Address(models.Model):
    country = models.CharField(max_length=100, default='Germany')
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100, blank=True, null=True)
    street = models.CharField(max_length=150)
    house_number = models.CharField(max_length=20)
    postal_code = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.street} {self.house_number}, {self.city}'