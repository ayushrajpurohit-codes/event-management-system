from django.contrib import admin
from .models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
        'status',
        'created_at',
    )
    search_fields = ('name',)
    list_filter = ('status',)