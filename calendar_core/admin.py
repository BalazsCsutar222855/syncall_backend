from django.contrib import admin
from .models import Calendar, Event, Notification

admin.site.register(Calendar)
admin.site.register(Event)
admin.site.register(Notification)

# Register your models here.
