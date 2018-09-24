from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from ippo_tutor.apps.core.permissions import IsTutorOrTargetUser

from .serializers import Subject, SubjectType, Task, SubjectSerializer, SubjectTypeSerializer, TaskSerializer


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


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        permission_classes = self.permission_classes[:]
        if self.action in ['destroy']:
            permission_classes += [IsAdminUser]
        else:
            permission_classes += [IsTutorOrTargetUser]

        return [permission() for permission in permission_classes]


def download_file(request, pk):
    task = get_object_or_404(Task, pk=pk)
    file = task.zip_with_templates.open()
    response = HttpResponse(
        file,
        content_type='application/zip',
    )
    response['Content-Disposition'] = 'attachment; filename="{}"'.format(file.name)
    return response
