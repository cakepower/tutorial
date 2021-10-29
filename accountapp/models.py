import datetime

from django.db import models
from django.utils import timezone
# Create your models here.

class World(models.Model):
    title = models.CharField(max_length=255, default="", blank = True, null=True)
    contents = models.TextField(default="", blank = True, null=True)


class Condition(models.Model):
    upcond = models.CharField(max_length=255, default="", blank = True, null=True)
    downcond = models.CharField(max_length=255, default="", blank = True, null=True)
    discond = models.CharField(max_length=255, default="", blank = True, null=True)
    transcond = models.CharField(max_length=255, default="", blank = True, null=True)
    field = models.CharField(max_length=255, default="", blank = True, null=True)
    future = models.CharField(max_length=255, default="", blank = True, null=True)

class Blog(models.Model):
    title = models.CharField(max_length=200)
    theme2 = models.CharField(max_length=200, default="")
    theme3 = models.CharField(max_length=200, default="")
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class HelloWorld(models.Model):
    text = models.CharField(max_length=255, blank=True, null=True)
    def db_type(self, connection):
        return 'stringarray'

class Hello(models.Model):
    text = models.CharField(max_length=255, default="", blank = True, null=True)
    text2 = models.TextField(default="", blank = True, null=True)

    def __str__(self):
        return self.text
    
    def publish(self):
        self.published_at = timezone.now()
        self.save()








