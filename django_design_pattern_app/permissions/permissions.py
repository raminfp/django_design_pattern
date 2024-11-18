from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied


# permission_classes = [IsSuperUserOrAdmin, ]
class IsSuperUserOrAdmin(BasePermission):
    def has_permission(self, request, view):
        """
        Check if the request user is a superuser or an admin.

        Args:
            request: The request object.
            view: The view object.

        Returns:
            bool: True if the user is a superuser or an admin, False otherwise.

        Raises:
            PermissionDenied: If the user is not authorized to access this resource.
        """
        if bool(request.user.is_authenticated and (request.user.is_superuser or request.user.rule.id == 1)):
            return True
        raise PermissionDenied("You are not authorized to access this resource.")


class IsSuperUserOrEditor(BasePermission):

    def has_permission(self, request, view):
        """
        Check if the request user is a superuser or an editor.

        Args:
            request: The request object.
            view: The view object.

        Returns:
            bool: True if the user is a superuser or an editor, False otherwise.

        Raises:
            PermissionDenied: If the user is not authorized to access this resource.
        """
        if bool(request.user.is_authenticated and (request.user.is_superuser or request.user.rule.id == 2)):
            return True
        raise PermissionDenied("You are not authorized to access this resource.")


class IsSuperUser(BasePermission):

    def has_permission(self, request, view):
        """
        Check if the request user is a superuser.

        Args:
            request: The request object.
            view: The view object.

        Returns:
            bool: True if the user is a superuser, False otherwise.

        Raises:
            PermissionDenied: If the user is not authorized to access this resource.
        """
        if bool(request.user.is_authenticated and request.user.is_superuser):
            return True
        raise PermissionDenied("You are not authorized to access this resource.")


class IsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        """
        Check if the request user is authenticated.

        Args:
            request: The request object.
            view: The view object.

        Returns:
            bool: True if the user is authenticated, False otherwise.

        Raises:
            PermissionDenied: If the user is not authorized to access this resource.
        """
        if bool(request.user.is_authenticated):
            return True
        raise PermissionDenied("You are not authorized to access this resource.")
