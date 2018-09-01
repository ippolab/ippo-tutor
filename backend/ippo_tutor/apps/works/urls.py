from rest_framework import routers
from django.urls import path

from .views import (
    SubjectViewSet,
    SubjectTypeViewSet,
    WorkViewSet,
    download_file
)

router = routers.DefaultRouter()
router.register('subjects', SubjectViewSet)
router.register('works', WorkViewSet)
router.register('subjects-types', SubjectTypeViewSet)

urlpatterns = [
    path('works-downloads/<pk>/', download_file)
]

urlpatterns += router.urls
