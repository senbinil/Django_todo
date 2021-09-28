from django.db import models
from django.utils import timezone
# Create your models here.
class Task(models.Model):
    name=models.CharField(max_length=240)
    priority=models.IntegerField()
    date=models.DateField()
    date.default=timezone.now