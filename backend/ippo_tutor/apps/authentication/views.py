from rest_framework import status, viewsets, generics
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from ippo_tutor.apps.core.permissions import IsTutorOrTargetUser, IsTutor
from .models import User
from .serializers import UserSerializer, ChangeUserPasswordSerializer, CreateUserSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    lookup_field = 'username'

    def get_permissions(self):
        permission_classes = self.permission_classes[:]
        if self.action == 'list':
            permission_classes += [IsTutor]
        elif self.action in ['create', 'delete']:
            permission_classes += [IsAdminUser]
        else:
            permission_classes += [IsTutorOrTargetUser]

        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action in ['retrieve', 'list']:
            return UserSerializer
        elif self.action == 'update':
            return ChangeUserPasswordSerializer
        else:
            return CreateUserSerializer

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)

        if not user.check_password(serializer.data.get("old_password")):
            return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)

        user.set_password(serializer.data.get("new_password"))
        user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_create(self, serializer):
        if User.objects.filter(username=self.request.data.get('username')).exists():
            raise ValidationError('User already exists.')

        User.objects.create_user(**serializer.validated_data)


class CheckAuthView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()

    def retrieve(self, request, *args, **kwargs):
        return Response({"username": request.user.username, "is_tutor": request.user.username, "token": request.auth})
