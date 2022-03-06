from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import serializers, status

from authentication.serializers import RegistrationSerializer, LoginSerializer


class RegistrationAPIView(GenericAPIView):
    """register new users"""

    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data

        # send_register_email.delay("no-reply@school.com",
        #                           user_data['email'])

        return Response(user_data, status=status.HTTP_201_CREATED)


class LoginAPIView(GenericAPIView):
    """api view fo login in"""

    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.data
        repsonse = {
            "data": {"user": dict(user), "message": "You have successfuly logged in"}
        }
        return Response(repsonse, status=status.HTTP_200_OK)
