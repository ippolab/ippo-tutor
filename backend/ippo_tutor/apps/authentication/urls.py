from django.urls import path

from rest_auth.views import LoginView, LogoutView

from .views import UserRetrieveAndPasswordChangeAPIView, UserListCreateAPIView, UserDeleteAPIView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),

    path('<str:username>/delete/', UserDeleteAPIView.as_view()),
    path('<str:username>/', UserRetrieveAndPasswordChangeAPIView.as_view()),
    path('', UserListCreateAPIView.as_view()),
]

