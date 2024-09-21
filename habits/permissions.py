from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Проверка пользователя на обладание сущностью
    """

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
