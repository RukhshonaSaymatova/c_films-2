from django.contrib import admin
from .models import Cinema

# Register your models here.

@admin.register(Cinema)

class CinemaAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "category", "address", "city", "contact", "email", "working_mode", "image")
# Register your models here.
