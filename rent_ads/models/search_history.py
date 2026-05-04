from django.db import models
from django.contrib.auth.models import User



class SearchHistory(models.Model):
    # User
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    session_key = models.CharField(
        max_length=40,
        null=True,
        blank=True
    )

    # Keywords
    keyword = models.CharField(
        max_length=255
    )

    # Date
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.keyword