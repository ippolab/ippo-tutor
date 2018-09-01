from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from ippo_tutor.apps.core.permissions import IsTutorOrTargetUser

from .models import Task
from .serializers import TaskSerializer


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
    from django.http import HttpResponse
    from django.shortcuts import get_object_or_404

    task = get_object_or_404(Task, pk=pk)
    file = task.zip_with_templates.open()
    response = HttpResponse(
        file,
        content_type='application/zip',
    )
    response['Content-Disposition'] = 'attachment; filename="{}"'.format(file.name)
    return response
