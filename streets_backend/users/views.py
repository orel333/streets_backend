import jwt
import os
import smtplib

from random import randint

from django.core.mail import send_mail
from rest_framework import permissions, status, viewsets, views
from rest_framework.response import Response

from users.models import CustomUser
from users.serializers import (
    ManagementDetailSerializer,
    ManagementListSerializer,
    SignUpSerializer
)
from utils.methods import get_confirmation_code



class ManagementViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CustomUser.objects.filter(role='fed manager')
    permission_classes = (permissions.AllowAny,)
    pagination_class = None

    def get_serializer_class(self):
        if self.action == 'list':
            return ManagementListSerializer
        return ManagementDetailSerializer


class SignUpView(views.APIView):
    """Регистрация пользователя по почте."""
    def post(self, request):
        confirmation_code = get_confirmation_code()
        rd = request.data
        rd['confirmation_code'] = confirmation_code
        serializer = SignUpSerializer(data=rd)
        if serializer.is_valid():
            serializer.save(is_active=False)
            username = rd.get('username')
            email = rd.get('email')
            mail_theme = f'Подтверждение регистрации пользователя {username}'
            mail_text = (
                f'Здравствуйте!\n\n\tВы (или кто-то другой) '
                'запросили регистрацию на сайте \'Улицы России\'. '
                'Для подтверждения регистрации пройдите по ссылке:'
                f'на адрес: http://95.163.230.143:3000/v1/confirmation/'
                f'{username}/{confirmation_code}'
            )
            mail_from = 'orel333app@gmail.com'
            mail_to = [email]
            send_mail(
                mail_theme,
                mail_text,
                mail_from,
                mail_to,
                fail_silently=False
            )
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
