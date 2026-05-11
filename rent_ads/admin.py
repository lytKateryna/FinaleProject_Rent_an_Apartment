from django.contrib import admin
from rent_ads.models import Listing, Booking, Review, SearchHistory, ListingView, User

from django.contrib.auth.admin import UserAdmin

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
        'get_city',
        'is_active',
        'created_at'
    )

    list_filter = (
        'address__city',
        'property_type',
        'is_active',
        'created_at',
    )

    search_fields = (
        'title',
        'description',
        'address__city',
        'address__district',
        'address__street',
        'owner__username'
    )

    ordering = ['-created_at']

    list_per_page = 10

    def get_city(self, obj):
        return obj.address.city

    get_city.short_description = 'City'


@admin.register(User)
class UserAdmin(UserAdmin):
    model = User
    list_display = [
        'username',
        'email',
        'role',
        'is_staff',
        'is_superuser',
        'is_active',
    ]
    list_filter = [
        'is_staff',
        'is_superuser',
        'role',
    ]
    search_fields = [
        'username',
        'email'
    ]
    ordering = ['email']

    readonly_fields = [
        'last_login',
        'date_joined'
    ]

    # fields = (
    #     'first_name',
    #     'last_name',
    #     'username',
    #     'email',
    #     'password',
    #     'phone',
    #     'birth_date',
    #     'role',
    #     'is_active',
    #     'is_staff',
    #     'is_superuser',
    #     'groups',
    #     'user_permissions',
    #     'last_login',
    #     'date_joined',
    # )
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'is_active')}),
        ('Important dates', {'fields': ('birth_date',)}),
        ('Profile', {'fields': ('first_name', 'last_name', 'phone')}),
        ('Groups', {'fields': ('groups', 'role')}),
        ('User Permissions', {'fields': ('user_permissions',)}),
    )
