from rest_framework import routers

from .views import TutorProfileViewSet

router = routers.DefaultRouter()
router.register('tutors', TutorProfileViewSet)

urlpatterns = [

]

urlpatterns += router.urls
