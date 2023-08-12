from django.contrib import admin
from .models import Museum

# Register your models here.

@admin.register(Museum)

class MuseumAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "category", "address", "city", "contact", "email", "working_mode", "image")
    
    
    

