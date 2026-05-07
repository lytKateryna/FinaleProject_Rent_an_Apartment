from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.metod in ['GET', 'HEAD', 'OPTIONS']:
            return True
        return obj.owner == request.user


class IsBookingOwnerOrLandlord(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return (
                    obj.tenant == request.user or
                    obj.listing.owner == request.user
            )
        return (
                obj.tenant == request.user or
                obj.listing.owner == request.user
        )
