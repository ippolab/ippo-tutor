from django.urls import path

from rest_framework.routers import DefaultRouter

from rest_auth.views import LoginView, LogoutView

from .views import UserViewSet

router = DefaultRouter()
router.register('', UserViewSet)

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
]

urlpatterns += router.urls

