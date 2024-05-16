import logging
import sys

import jwt
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import RegexValidator
from django.db import models
from rest_framework_simplejwt.tokens import AccessToken

from streets_backend.settings import SECRET_KEY
from validators import validate_birthday

formatter = logging.Formatter(
    '%(asctime)s %(levelname)s %(filename)s: '
    '%(message)s - line %(lineno)s'
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
logger.addHandler(handler)
handler.setFormatter(formatter)
logger.disabled = False
logger.debug('Logging from users.models has been started.')

ROLE_CHOICES = (
    ('promoter', 'Организатор'),
    ('admin', 'Администратор')
)


class CustomUserManager(BaseUserManager):
    def create_superuser(self, username, email, password, **other_fields):
        logger.debug('SuperUser is being initialized...')
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        if other_fields.get('is_staff') is not True:
            raise ValueError(
                '"is_staff" суперпользователя должно быть в режиме "True"'
            )
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                '"is_superuser" суперпользователя должно быть в режиме "True"'
            )
        logger.debug(
            f'Here are some other fields in parameters: {other_fields}'
        )
        if 'role' in other_fields:
            role = other_fields.get('role')
            del other_fields['role']
        else:
            role = 'admin'

        return self.create_user(
            username,
            email,
            role,
            password,
            **other_fields
        )

    def create_user(
        self,
        username,
        email,
        role='admin',
        password=None,
        **other_fields
    ):
        logger.debug(f'Got role: {role}')
        logger.debug(f'Got password: {password}')
        logger.debug(f'Is_staff: {other_fields.get("is_staff")}')
        logger.debug(f'Is_superuser: {other_fields.get("is_superuser")}')
        logger.debug('Create user func was initiated')
        if not email:
            raise ValueError('Необходимо указать email')
        if not username:
            raise ValueError('Необходимо указать username')

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=username,
            role=role,
            **other_fields
        )
        user.is_staff = True
        user.set_password(password)
        user.save()
        confirmation_code = user.confirmation_code
        token = user.token
        if user.is_superuser is True:
            first_line = f'Создан суперпользователь {username}.'
        else:
            first_line = f'Создан пользователь {username}.'
        # при запуске в производство поставить отправку по почте
        logger.debug(
            f'{first_line}\nЕго роль: {role}.'
            f'Его токен: {token}\n'
            f'Его confirmation_code для обновления токена:\n'
            f'{confirmation_code}'
        )
        logger.debug(f'user_if_staff:{user.is_staff}')
        return user


class CustomUser(AbstractUser):
    """Кастомная модель пользователя."""
    bio = models.TextField('Дополнительная информация', blank=True)
    role = models.CharField(
        'Роль',
        choices=ROLE_CHOICES,
        default='user',
        max_length=16
    )
    email = models.EmailField(
        'E-MAIL',
        unique=True,
        blank=False,
        null=True
    )
    username = models.CharField(
        max_length=150,
        unique=True,
        validators=(
            RegexValidator(
                regex=r'^[mM][eE]$',
                message=(
                    'Попытка регистрации пользователя '
                    'под me-образным именем'
                ),
                inverse_match=True
            ),
        ),
    )
    surname = models.CharField(
        'Фамилия',
        max_length=150
    )
    first_name = models.CharField(
        'Имя',
        max_length=150
    )
    third_name = models.CharField(
        'Отчество',
        max_length=150
    )
    birth_date = models.DateField(
        'День рождения',
        validators=(validate_birthday,),
        null=True
    )
    tg_nick = models.CharField(
        'Имя пользователя в телеграм',
        max_length=32,
        unique=True,
        null=True,
        validators=(
            RegexValidator(
                regex=r'^@[\w\d_]{5-32}$',
                message=(
                    'Некорректный ник телеграм'
                )
            ),
        ),
    )
    phone = models.CharField(
        'Мобильный телефон',
        max_length=11,
        unique=True,
        null=True,
        validators=(
            RegexValidator(
                regex=r'^\+79\d{9}$',
                message=(
                    'Введите реальный мобильный телефон'
                    'в формате +79XXXXXXXXX'
                )
            )
        )
    )
    avatar = models.ImageField(
        'Аватар',
        null=True,
        
    )
    objects = CustomUserManager()

    class Meta:
        ordering = ('-date_joined',)
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return f'{self.username}: {self.email}, уровень доступа: {self.role}'

    @property
    def token(self):
        token = AccessToken.for_user(self)
        token['role'] = self.role
        token['is_superuser'] = self.is_superuser
        return token

    @property
    def confirmation_code(self):
        dict = {
            'username': self.username,
            'email': self.email
        }
        return jwt.encode(
            dict,
            SECRET_KEY,
            'HS256'
        )
