from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    img = models.ImageField("Аватар", upload_to="media", blank=True, null=True)


# Create your models here.
