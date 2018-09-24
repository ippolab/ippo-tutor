from rest_framework import routers
from django.urls import path

from .views import SubjectViewSet, SubjectTypeViewSet, TaskViewSet, download_file

router = routers.DefaultRouter()
router.register('subjects', SubjectViewSet)
router.register('subjects-types', SubjectTypeViewSet)
router.register('tasks', TaskViewSet)

urlpatterns = [
    path('tasks-downloads/<pk>/', download_file)
]

urlpatterns += router.urls
