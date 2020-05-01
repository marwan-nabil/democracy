from django.db import models
from django.contrib.auth.models import AbstractUser
from threads.models import ReplyModel


# (marwan): i won't use the builtin django user model
# explanation is here:
# https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html
class UserModel(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    avatar =  models.ImageField(upload_to='avatars/%Y/%m/%d/')
    popularity = models.IntegerField(default=0)
    factions = models.ManyToManyField("FactionModel", related_name="members")


# users can save important replies into categories on their profiles
class ReplyCategoryModel(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    replies = models.ManyToManyField(ReplyModel, blank=True, related_name='linked_categories')


class FactionModel(models.Model):
    name = models.CharField(max_length=50)
    leader = models.ForeignKey(UserModel, null=True, on_delete=models.SET_NULL)
    # (marwan): e.g. a user cant be both communist and capitalist
    mutualy_exclusive_with = models.ManyToManyField("self", blank=True, related_name="mutualy_exclusive_factions")