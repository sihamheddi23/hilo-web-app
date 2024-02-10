from django.db import models

# Create your models here.
class Room(models.Model):
    name = models.CharField()
    created_at = models.DateTimeField()