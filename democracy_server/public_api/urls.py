from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.stub_view),
    # to test front end react app
    path('thread_count/', views.thread_count),
]
