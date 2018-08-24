import django.db

from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from ippo_tutor.apps.core.permissions import IsTutorOrTargetUser, IsTutor
from ippo_tutor.apps.core.helpers import DRFViewPermissionsSubstituteManager, DRFViewSerializerSubstituteManager

from .models import User
from .serializers import UserSerializer, ChangeUserPasswordSerializer, CreateUserSerializer


class UserRetrieveAndPasswordChangeAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated, IsTutorOrTargetUser,)
    queryset = User.objects.all()
    lookup_field = 'username'

    def retrieve(self, request, *args, **kwargs):
        with DRFViewSerializerSubstituteManager(self, attr_value=UserSerializer):
            return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        with DRFViewSerializerSubstituteManager(self, attr_value=ChangeUserPasswordSerializer):
            user = self.get_object()
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            if not user.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            user.set_password(serializer.data.get("new_password"))
            user.save()
            return Response(status=status.HTTP_204_NO_CONTENT)


class UserListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()

    def list(self, request, *args, **kwargs):
        with DRFViewSerializerSubstituteManager(self, attr_value=UserSerializer):
            with DRFViewPermissionsSubstituteManager(self, attr_value=(IsTutor,)):
                return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        with DRFViewSerializerSubstituteManager(self, attr_value=CreateUserSerializer):
            with DRFViewPermissionsSubstituteManager(self, attr_value=(IsAdminUser,)):
                if User.objects.filter(username=request.data.get('username', None)).exists():
                    return Response({"detail": ["User already exists."]}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return super().create(request, *args, **kwargs)


class UserDeleteAPIView(generics.DestroyAPIView):
    permission_classes = (IsAuthenticated, IsAdminUser)
    queryset = User.objects.all()
    lookup_field = 'username'
