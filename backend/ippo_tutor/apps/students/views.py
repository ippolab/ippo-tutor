from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ippo_tutor.apps.core.permissions import IsTutorOrTargetUser, IsTutor
from ippo_tutor.apps.core.helpers import DRFViewPermissionsSubstituteManager

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

    def get_object(self):
        username = self.kwargs['username']
        user = generics.get_object_or_404(self.queryset, user__username=username)
        self.check_object_permissions(self.request, user)
        return user

    def retrieve(self, request, *args, **kwargs):
        with DRFViewPermissionsSubstituteManager(self, attr_value=(IsTutorOrTargetUser,)):
            return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        with DRFViewPermissionsSubstituteManager(self, attr_value=(IsTutor,)):
            return super().update(request, *args, **kwargs)

