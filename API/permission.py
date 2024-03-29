from rest_framework import permissions

class CustomPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        print(user.username)
        if user and request.user.is_authenticated and user.username == 'y':
            return True
        return False

def has_permission(self, request, view):
        user = request.user
        if user.first_name == 'behruz' and request.method == 'GET':
            return True
        return False