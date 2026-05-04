from django.contrib import admin
from rent_ads.models import Listing, Booking, Review, SearchHistory, ListingView

# Register your models here.
admin.site.register(Listing)
admin.site.register(Booking)
admin.site.register(Review)
admin.site.register(SearchHistory)
admin.site.register(ListingView)