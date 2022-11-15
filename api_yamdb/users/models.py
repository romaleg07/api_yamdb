from django.contrib.auth.models import AbstractUser
from django.db import models

ROLE_CHOICES = (
    ('admin', 'Администратор'),
    ('moderator', 'Модератор'),
    ('user', 'Пользователь'),
)


class User(AbstractUser):
    role = models.CharField(
        max_length=9,
        choices=ROLE_CHOICES,
        default="user"
    )
    bio = models.TextField(
        verbose_name='bio',
        help_text='Напишите о себе',
        blank=True
    )
    confirmation_code = models.CharField(
        max_length=32,
        blank=True
    )
    email = models.EmailField(
        verbose_name='Адрес электронной почты',
        unique=True,
    )

    class Meta:
        db_table = 'auth_user'

    @property
    def is_admin(self):
        return self.role == 'admin' or self.is_superuser

    @property
    def is_moderator(self):
        return self.role == 'moderator' or self.is_superuser
