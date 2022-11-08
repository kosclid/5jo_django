from django.db import models

from django.core.validators import MaxValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    gender = models.PositiveSmallIntegerField(validators=[MaxValueValidator(2),], null=True)
    age = models.PositiveSmallIntegerField(validators=[MaxValueValidator(100),], null=True)

