import uuid
from django.db import models
from django.contrib.auth.models import User 

class Calendar(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    title = models.CharField(max_length=100, default="YourDefaultName")
    description = models.TextField(default="Custom Calendar")

    start = models.DateTimeField(auto_now=True)
    end = models.DateTimeField(auto_now_add=True)


class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    calendar_key = models.ForeignKey(Calendar, on_delete=models.CASCADE)

    title = models.CharField(max_length=100, default="Default Event Name")
    description = models.TextField(default="Default Event Desc.")
    start = models.DateTimeField()
    end = models.DateTimeField()
    color = models.CharField(max_length=100, default="bg-red-200 text-red-500")

    edited = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

class Notification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_key = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=100, default="Default Event Name")
    description = models.TextField(default="Default Event Desc.")
    start = models.DateTimeField()
    





