from django.contrib import admin
from .models import Theater

# Register your models here.

@admin.register(Theater)

class TheaterAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "category", "address", "city", "contact", "email", "working_mode", "image")

