from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from ippo_tutor.apps.core.permissions import IsTutor
from .models import TutorProfile
from .serializers import TutorProfileSerializer


class TutorProfileViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = TutorProfile.objects.select_related('user')
    serializer_class = TutorProfileSerializer
    lookup_field = 'username'

    def get_object(self):
        username = self.kwargs['username']
        user = generics.get_object_or_404(self.queryset, user__username=username)
        self.check_object_permissions(self.request, user)
        return user

    def get_permissions(self):
        permission_classes = self.permission_classes[:]
        if self.action in ['list', 'retrieve']:
            permission_classes += [IsTutor]
        else:
            permission_classes += [IsAdminUser]

        return [permission() for permission in permission_classes]
