from django.urls import path
from rest_auth.views import LoginView, LogoutView
from rest_framework.routers import DefaultRouter

from .views import UserViewSet

router = DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('users/login/', LoginView.as_view()),
    path('users/logout/', LogoutView.as_view()),
]

urlpatterns += router.urls
