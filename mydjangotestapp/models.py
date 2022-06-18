from django.db import models

# Create your models here.
class Task(models.Model):
    '''creating a task table in database'''
    name = models.CharField(max_length=400)