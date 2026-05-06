from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rent_ads.views.listings import ListingViewSet
from rent_ads.views.bookings import BookingViewSet
from rent_ads.views.reviews import ReviewViewSet
from rent_ads.views.search_histories import SearchHistoryViewSet
from rent_ads.views.listing_views import ListingViewViewSet

router = DefaultRouter()
router.register(r'listings', ListingViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'search_histories', SearchHistoryViewSet)
router.register(r'listing_views', ListingViewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns += router.urls
