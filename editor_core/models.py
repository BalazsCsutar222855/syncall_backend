import uuid
from django.db import models
from django.contrib.auth.models import User 

class Shelf(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_key = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=100, default="YourDefaultName")
    description = models.TextField(default="Custom Calcreatedar")

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    shelf_key = models.ForeignKey(Shelf, on_delete=models.CASCADE)
    user_key = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=100, default="YourDefaultName")
    description = models.TextField(default="Custom Calcreatedar")

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

class Chapter(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    book_key = models.ForeignKey(Book, on_delete=models.CASCADE)

    title = models.CharField(max_length=100, default="YourDefaultName")
    description = models.TextField(default="Custom Calcreatedar")

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

class Page(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    chapter_key = models.ForeignKey(Chapter, on_delete=models.CASCADE)

    title = models.CharField(max_length=100, default="YourDefaultName")
    description = models.TextField(default="Custom Calcreatedar")

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)