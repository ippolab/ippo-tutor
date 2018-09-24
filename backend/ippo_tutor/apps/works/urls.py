from rest_framework import routers
from django.urls import path

from .views import WorkViewSet, download_document, download_source


router = routers.DefaultRouter()
router.register('works', WorkViewSet)

urlpatterns = [
    path('works-document/<pk>/', download_document),
    path('works-source/<pk>/', download_source)

]

urlpatterns += router.urls
