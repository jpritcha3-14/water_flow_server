from django.db import models

# Create your models here.

class Flow(models.Model):
    val = models.IntegerField(default=0)
    timestamp = models.IntegerField(default=0)
