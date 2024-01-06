from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    telegram_uuid = models.PositiveIntegerField(null=True)
    telegram_username = models.CharField(max_length=255, blank=True, null=True)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='users',
        blank=True,
        verbose_name='Группы',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='users',
        blank=True,
        verbose_name='Права',
    )

    class Meta:
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.username} ({self.telegram_username})'
