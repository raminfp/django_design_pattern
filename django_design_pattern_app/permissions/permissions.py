from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied


# permission_classes = [IsSuperUserOrAdmin, ]
class IsSuperUserOrAdmin(BasePermission):
    def has_permission(self, request, view):
        if bool(request.user.is_authenticated and (request.user.is_superuser or request.user.rule.id == 1)):
            return True
        raise PermissionDenied("You are not authorized to access this resource.")


class IsSuperUserOrEditor(BasePermission):

    def has_permission(self, request, view):
        if bool(request.user.is_authenticated and (request.user.is_superuser or request.user.rule.id == 2)):
            return True
        raise PermissionDenied("You are not authorized to access this resource.")


class IsSuperUser(BasePermission):

    def has_permission(self, request, view):
        if bool(request.user.is_authenticated and request.user.is_superuser):
            return True
        raise PermissionDenied("You are not authorized to access this resource.")


class IsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        if bool(request.user.is_authenticated):
            return True
        raise PermissionDenied("You are not authorized to access this resource.")
