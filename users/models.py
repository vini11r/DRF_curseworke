from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None

    email = models.EmailField(
        unique=True, verbose_name="Email", help_text="Укажите почту"
    )
    phone = models.CharField(
        max_length=150,
        verbose_name="Телефон",
        blank=True,
        null=True,
        help_text="Укажите телефон",
    )
    tg_chat_id = models.CharField(
        max_length=50,
        verbose_name="Телеграм chat-id",
        help_text="Укажите телеграм chat-id",
        blank=True,
        null=True,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
