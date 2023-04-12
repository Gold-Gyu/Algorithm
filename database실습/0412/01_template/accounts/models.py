from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# 커스텀 유저로 만들어놈
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
