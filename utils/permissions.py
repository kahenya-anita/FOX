from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthor(BasePermission):
    """check if user is the other of the post"""

    def has_object_permission(self, request, view, obj):
        user = request.user

        if request.method in SAFE_METHODS:
            return True

        if user.is_authenticated and user == obj.author:
            return True
        return False

class IsAuthenticated(BasePermission):
    """create post if user is logged in"""

    def has_permission(self, request, view):
        user = request.user

        if request.method in SAFE_METHODS:
            return True
        
        return user.is_authenticated