from django.contrib import admin
from rent_ads.models import Listing, Booking, Review, SearchHistory, ListingView

# Register your models here.
admin.site.register(Booking)
admin.site.register(Review)
admin.site.register(SearchHistory)
admin.site.register(ListingView)

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'owner',
        'price',
        'city',
        'is_active',
        'created_at'
    )

    list_filter = (
        'city',
        'property_type',
        'is_active',
        'created_at'
    )

    search_fields = (
        'title',
        'description',
        'address',
        'city',
        'district',
        'owner__username'
    )

    ordering = ['-created_at']

    list_per_page = 10