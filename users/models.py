from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Custrom User Model"""

    KEY_GENDER = ["male", "female", "other"]
    KEY_LANGUAGE = ["en", "kr", "other"]
    KEY_CURRENCY = ["usd", "krw", "other"]
    GENDER_CHOICE = (
        (KEY_GENDER[0], "Male"),
        (KEY_GENDER[1], "Female"),
        (KEY_GENDER[2], "Other"),
    )
    LANGUAGE_CHOICE = (
        (KEY_LANGUAGE[0], "English"),
        (KEY_LANGUAGE[1], "Korean"),
        (KEY_LANGUAGE[2], "Other"),
    )
    CURRENCY_CHOICE = (
        (KEY_CURRENCY[0], "USD"),
        (KEY_CURRENCY[1], "KRW"),
        (KEY_CURRENCY[2], "Other"),
    )
    avatar = models.ImageField(blank=True)
    gender = models.CharField(choices=GENDER_CHOICE, max_length=10, blank=True)
    bio = models.TextField(blank=True)
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(choices=LANGUAGE_CHOICE, max_length=10, blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICE, max_length=10, blank=True)
    superhost = models.BooleanField(default=False)
