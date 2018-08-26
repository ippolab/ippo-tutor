from rest_framework import permissions


class IsTutorOrTargetUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_tutor or obj == request.user


class IsAdminOrTargetUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj == request.user


class IsTutor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_tutor
