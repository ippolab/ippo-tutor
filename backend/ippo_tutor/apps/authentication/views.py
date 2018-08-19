from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from .models import User
from .serializers import UserSerializer, ChangeUserPasswordSerializer
from .permissions import IsStaffOrTargetUser


class UserRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = (IsStaffOrTargetUser,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'


class UserListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAdminUser,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserPasswordChangeView(generics.GenericAPIView):
    permission_classes = (IsStaffOrTargetUser,)
    queryset = User.objects.all()
    serializer_class = ChangeUserPasswordSerializer
    lookup_field = 'username'

    def put(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if not user.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            user.set_password(serializer.data.get("new_password"))
            user.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
