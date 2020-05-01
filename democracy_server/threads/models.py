from django.db import models


class ThreadModel(models.Model):
    title = models.CharField(max_length=200)
    contents = models.CharField(max_length=200)
    time_posted = models.DateTimeField(auto_now_add=True)
    attached_image = models.ImageField(
        upload_to="thread_images/%Y/%m/%d/", blank=True, null=True
    )
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Thread"
        verbose_name_plural = "Threads"

    def __str__(self):
        return self.title + " | " + self.time_posted.strftime("%d/%m/%Y")


class ReplyModel(models.Model):
    thread = models.ForeignKey(ThreadModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    contents = models.CharField(max_length=200)
    time_posted = models.DateTimeField(auto_now_add=True)
    attached_image = models.ImageField(upload_to="thread_images/%Y/%m/%d/", blank=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    counter_argument_to = models.ManyToManyField(
        "self", blank=True, related_name="counter_arguments"
    )
    with_thread = models.BooleanField(default=False, blank=True)
    saved_count = models.PositiveIntegerField(default=0, blank=True)

    class Meta:
        verbose_name = "Reply"
        verbose_name_plural = "Replies"

    def __str__(self):
        return self.title + " | " + self.time_posted.strftime("%d/%m/%Y")
