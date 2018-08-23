from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

from ippo_tutor.apps.core.permissions import IsTutorOrTargetUser, IsTutor

from .models import StudentProfile
from .serializers import StudentProfileSerializer


class StudentProfileListAPIView(generics.ListAPIView):
    permission_classes = (IsAuthenticated, IsTutor,)
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer


class StudentProfileRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = StudentProfile.objects.select_related('user')
    serializer_class = StudentProfileSerializer
    lookup_field = 'username'

    def get_object(self):
        username = self.kwargs['username']
        user = generics.get_object_or_404(self.queryset, user__username=username)
        self.check_object_permissions(self.request, user)
        return user

    def retrieve(self, request, *args, **kwargs):
        default_permission_classes = self.permission_classes
        self.permission_classes += (IsTutorOrTargetUser,)
        result = super().retrieve(request, *args, **kwargs)
        self.permission_classes = default_permission_classes
        return result

    def update(self, request, *args, **kwargs):
        default_permission_classes = self.permission_classes
        self.permission_classes += (IsTutor,)
        result = super().update(request, *args, **kwargs)
        self.permission_classes = default_permission_classes
        return result
