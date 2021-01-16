from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="applog-home"),
    path('upload', views.upload, name="applog-upload"),
]