from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
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


class IsLandlordOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return (request.user
                and request.user.is_authenticated
                and request.user.role == 'landlord'
                )


class IsReviewOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user
