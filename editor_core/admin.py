from django.contrib import admin
from .models import Shelf, Book, Chapter, Page
# Register your models here.


admin.site.register(Shelf)
admin.site.register(Book)
admin.site.register(Chapter)
admin.site.register(Page)
