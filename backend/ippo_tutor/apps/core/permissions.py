from rest_framework import permissions


class IsTutorOrTargetUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_tutor or view.kwargs['username'] == request.user.username


class IsAdminOrTargetUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff or view.kwargs['username'] == request.user.username


class IsTutor(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_tutor
