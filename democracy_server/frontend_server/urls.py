from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.catalog_view),
    path('thread/view/<int:id>/', views.view_thread, name="view_thread"),
    path('thread/post/', views.create_thread),
]
