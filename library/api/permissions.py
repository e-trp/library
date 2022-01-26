from rest_framework.permissions import BasePermission, SAFE_METHODS
from api.models import Book
import datetime

class LibraryPermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        if isinstance(obj, Book):
            curr_year = datetime.date.today().year
            if (curr_year - obj.publish_date.date().year) >= 1:
                return False
        return True

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated) and request.method in SAFE_METHODS
