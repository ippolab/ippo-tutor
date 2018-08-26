from rest_framework import routers

from .views import TutorProfileViewSet

router = routers.DefaultRouter()
router.register('', TutorProfileViewSet)

urlpatterns = [

]

urlpatterns += router.urls

