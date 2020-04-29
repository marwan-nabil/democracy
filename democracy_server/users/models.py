from django.db import models
from django.contrib.auth.models import AbstractUser

# (marwan): i won't use the builtin django user model
# explanation is here:
# https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html
class UserModel(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    avatar =  models.ImageField(upload_to='avatars/%Y/%m/%d/')
    popularity = models.IntegerField(default=0)
