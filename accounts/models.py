from django.core.validators import MaxValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class GenderChoices(models.IntegerChoices):
        MALE = 0, "남자"
        FEMALE = 1, "여자"

    gender = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(2),
        ],
        null=True,
        choices=GenderChoices.choices,
        default=GenderChoices.MALE,
    )
    age = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(100),
        ],
        null=True,
    )
