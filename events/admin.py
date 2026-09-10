from django.contrib import admin
from .models import EventType, Event


@admin.register(EventType)
class EventTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'created_at')
    search_fields = ('name',)
    list_filter = ('status',)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'event_type',
        'event_date',
        'event_time',
        'venue',
        'status',
    )
    search_fields = ('name', 'venue')
    list_filter = ('event_type', 'status', 'event_date')