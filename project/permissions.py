from rest_framework import permissions

class IsAdminOrOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners or admins of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user or obj.admins.filter(id=request.user.id).exists()
