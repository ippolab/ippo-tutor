from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from ippo_tutor.apps.core.permissions import IsTutorOrTargetUser

from .models import Subject, SubjectType, Work
from .serializers import SubjectSerializer, SubjectTypeSerializer, WorkSerializer


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        permission_classes = self.permission_classes[:]
        if self.action in ['create', 'update', 'destroy']:
            permission_classes += [IsAdminUser]
        else:
            permission_classes += [IsTutorOrTargetUser]

        return [permission() for permission in permission_classes]


class SubjectTypeViewSet(viewsets.ModelViewSet):
    queryset = SubjectType.objects.all()
    serializer_class = SubjectTypeSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        permission_classes = self.permission_classes[:]
        if self.action in ['create', 'update', 'destroy']:
            permission_classes += [IsAdminUser]
        else:
            permission_classes += [IsTutorOrTargetUser]

        return [permission() for permission in permission_classes]


class WorkViewSet(viewsets.ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_tutor:
            return Work.objects.all()

        return user.student.works.all()

    def get_permissions(self):
        permission_classes = self.permission_classes[:]
        if self.action in ['destroy']:
            permission_classes += [IsAdminUser]
        else:
            permission_classes += [IsTutorOrTargetUser]

        return [permission() for permission in permission_classes]


def download_file(request, pk):
    from django.http import HttpResponse
    from django.shortcuts import get_object_or_404

    work = get_object_or_404(Work, pk=pk)
    file = work.file.open()
    response = HttpResponse(
        file,
        content_type='application/pdf'
    )
    response['Content-Disposition'] = 'attachment; filename="{}"'.format(file.name)
    return response
