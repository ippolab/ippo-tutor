from rest_framework import routers

from .views import (
    SubjectViewSet,
    SubjectTypeViewSet,
    WorkViewSet,
)

router = routers.DefaultRouter()
router.register('subjects', SubjectViewSet)
router.register('works', WorkViewSet)
router.register('subjects-types', SubjectTypeViewSet)

urlpatterns = []

urlpatterns += router.urls
