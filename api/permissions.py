from rest_framework.permissions import SAFE_METHODS, BasePermission
import datetime


class AdminPermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        return bool(request.user and request.user.is_staff)

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)


class LibraryUserPermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        return bool(request.method in SAFE_METHODS)

    def has_permission(self, request, view):
        return bool(
            request.user and request.user.is_authenticated and
            request.method in SAFE_METHODS
        )
        

class BooksPermission(LibraryUserPermission):

    def has_object_permission(self, request, view, obj):
        curr_year = datetime.date.today().year
        if (curr_year - obj.publish_date.date().year == 0) and request.method in SAFE_METHODS:
                return True
        return False
