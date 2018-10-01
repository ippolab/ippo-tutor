from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from ippo_tutor.apps.core.permissions import IsTutorOrTargetUser

from .serializers import Work, WorkSerializer


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


def download_document(request, pk):
    work = get_object_or_404(Work, pk=pk)
    file = work.document.open()
    response = HttpResponse(
        file,
        content_type='application/pdf'
    )
    response['Content-Disposition'] = 'attachment; filename="{}"'.format(file.name)
    return response


def download_source(request, pk):
    work = get_object_or_404(Work, pk=pk)
    file = work.source_code.open()
    response = HttpResponse(
        file,
        content_type='application/zip'
    )
    response['Content-Disposition'] = 'attachment; filename="{}"'.format(file.name)
    return response
