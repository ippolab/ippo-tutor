from django.urls import path

from .views import StudentProfileListAPIView, StudentProfileRetrieveUpdateAPIView

urlpatterns = [
    path('', StudentProfileListAPIView.as_view()),
    path('<str:username>/', StudentProfileRetrieveUpdateAPIView.as_view())
]

