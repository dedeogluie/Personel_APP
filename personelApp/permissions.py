from rest_framework import permissions

class IsStaffOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
    
    def has_permission(self, request, view):
        SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_staff
        )