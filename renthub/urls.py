"""
URL configuration for renthub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from rent_ads.views.listings import ListingViewSet
# from rent_ads.views.bookings import BookingViewSet
# from rent_ads.views.reviews import ReviewViewSet
# from rent_ads.views.search_histories import SearchHistoryViewSet
# from rent_ads.views.listing_views import ListingViewViewSet
#
# default_router = DefaultRouter()
#
# default_router.register(r'listings', ListingViewSet, basename='listing')
# default_router.register(r'bookings', BookingViewSet, basename='booking')
# default_router.register(r'reviews', ReviewViewSet, basename='review')
# default_router.register(r'search_histories', SearchHistoryViewSet, basename='search_history')
# default_router.register(r'listing_views', ListingViewViewSet, basename='listing_view')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('rent_ads.urls')),
]



