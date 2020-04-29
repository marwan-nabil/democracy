from django.contrib import admin
from .models import ThreadModel, ReplyModel

# Register your models here.
admin.site.register(ThreadModel)
admin.site.register(ReplyModel)
