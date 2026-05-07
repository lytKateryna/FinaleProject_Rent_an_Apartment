
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from rent_ads.views.listings import ListingViewSet
from rent_ads.views.bookings import BookingViewSet
from rent_ads.views.reviews import ReviewViewSet
from rent_ads.views.search_histories import SearchHistoryViewSet
from rent_ads.views.listing_views import ListingViewViewSet
from rent_ads.views.users import UserViewSet


default_router = DefaultRouter()

default_router.register(r'listings', ListingViewSet, basename='listing')
default_router.register(r'bookings', BookingViewSet, basename='booking')
default_router.register(r'reviews', ReviewViewSet, basename='review')
default_router.register(r'search_histories', SearchHistoryViewSet, basename='search_history')
default_router.register(r'listing_views', ListingViewViewSet, basename='listing_view')
default_router.register(r'users', UserViewSet, basename='users')


urlpatterns = [
    path('auth/', include('rent_ads.urls.auth')),
]

urlpatterns += default_router.urls

