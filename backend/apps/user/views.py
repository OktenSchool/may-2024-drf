import os

from django.contrib.auth import get_user_model
from rest_framework.generics import ListCreateAPIView, GenericAPIView
from rest_framework.response import Response
from apps.user.serializers import UserSerializer
from rest_framework import status
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from rest_framework.permissions import AllowAny

UserModel = get_user_model()


class UserListCreateView(ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class BlockUserView(GenericAPIView):
    def get_queryset(self):
        return UserModel.objects.all().exclude(id=self.request.user.id)

    # queryset = UserModel.objects.all()

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if user.is_active:
            user.is_active = False
            user.save()

        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class UnBlockUserView(GenericAPIView):

    def get_serializer(self):
        return None

    def get_queryset(self):
        return UserModel.objects.exclude(id=self.request.user.id)

    # queryset = UserModel.objects.all()

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if not user.is_active:
            user.is_active = True
            user.save()

        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class UserToAdminView(GenericAPIView):
    def get_queryset(self):
        return UserModel.objects.exclude(id=self.request.user.id)

    # queryset = UserModel.objects.all()

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if not user.is_staff:
            user.is_staff = True
            user.save()

        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class SendEmailTestView(GenericAPIView):
    permission_classes = (AllowAny,)

    def get(self, *args, **kwargs):
        template = get_template('test_email.html')
        html_content = template.render({'name': 'DJANGo'})
        msg = EmailMultiAlternatives(
            subject="Test Email",
            from_email=os.environ.get('EMAIL_HOST_USER'),
            to=['demchyshyn.v87@gmail.com']
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return Response({'message': 'Email sent!'}, status.HTTP_200_OK)
