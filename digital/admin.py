from django.contrib import admin
from .models import DigitalStorage

# Register your models here.
@admin.register(DigitalStorage)
class DigitalStorageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in DigitalStorage._meta.fields]
    