from rest_framework import routers

from .views import StudentProfileViewSet, GroupViewSet

router = routers.DefaultRouter()
router.register('students', StudentProfileViewSet)
router.register('groups', GroupViewSet)

urlpatterns = [

]

urlpatterns += router.urls
