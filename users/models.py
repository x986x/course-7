from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Модель пользователя, используется для аутентификации
    """

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    username = None
    email = models.EmailField(
        verbose_name="почта",
        help_text="user's email",
        unique=True,
    )
    telegram_chat_id = models.CharField(
        max_length=64,
        verbose_name="telegram chat id",
        help_text="id of user's tg chat",
        blank=True,
        null=True,
    )

    def __str__(self):
        return getattr(self, self.USERNAME_FIELD)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
