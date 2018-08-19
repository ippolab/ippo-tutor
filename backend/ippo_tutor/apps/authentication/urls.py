from django.urls import path

from rest_auth.views import LoginView, LogoutView

from .views import UserRetrieveAPIView, UserListCreateAPIView, UserPasswordChangeView

urlpatterns = [
    path('', UserListCreateAPIView.as_view()),
    path('<str:username>', UserRetrieveAPIView.as_view()),

    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('<str:username>/change-password/', UserPasswordChangeView.as_view()),
]
