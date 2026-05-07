from django.db import models
from django.conf import settings



class SearchHistory(models.Model):
    # User
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
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

    class Meta:
        verbose_name = "Search History"
        verbose_name_plural = "Search Histories"
        ordering = ['-created_at']

    def __str__(self):
        return self.keyword