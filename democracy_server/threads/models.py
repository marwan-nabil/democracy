from django.db import models


class ThreadModel(models.Model):
    title = models.CharField(max_length=200)
    contents = models.CharField(max_length=200)
    time_posted = models.DateTimeField(auto_now_add=True)
    attached_image = models.ImageField(upload_to='thread_images/%Y/%m/%d/')
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Thread"
        verbose_name_plural = "Threads"


class ReplyModel(models.Model):
    thread = models.ForeignKey(ThreadModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    contents = models.CharField(max_length=200)
    time_posted = models.DateTimeField(auto_now_add=True)
    attached_image = models.ImageField(upload_to='thread_images/%Y/%m/%d/')
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    # (marwan): strange i know, documented here:
    # https://docs.djangoproject.com/en/3.0/topics/db/models/#relationships
    # https://docs.djangoproject.com/en/3.0/ref/models/fields/#manytomanyfield
    linked_counter_arguments = models.ManyToManyField("self", blank=True)

    class Meta:
        verbose_name = "Reply"
        verbose_name_plural = "Replys"