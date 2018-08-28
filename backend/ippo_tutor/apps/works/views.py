from rest_framework import viewsets

from .models import Subject, SubjectType, Work
from .serializers import SubjectSerializer, SubjectTypeSerializer, WorkSerializer


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectTypeViewSet(viewsets.ModelViewSet):
    queryset = SubjectType.objects.all()
    serializer_class = SubjectTypeSerializer

    def get_permissions(self):  # todo override permission
        return super().get_permissions()


class WorkViewSet(viewsets.ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
