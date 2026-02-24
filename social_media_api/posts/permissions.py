from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        # Allow read-only requests
        if request.method in permissions.SAFE_METHODS:
            return True

        # Allow write only if owner
        return obj.author == request.user