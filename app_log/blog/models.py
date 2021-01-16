from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Screen(models.Model):
    screen_name = models.CharField(max_length=100)
    image_name = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
