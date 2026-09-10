from django.db import models


class EventType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'event_types'
        ordering = ['name']

    def __str__(self):
        return self.name


class Event(models.Model):
    event_type = models.ForeignKey(
        EventType,
        on_delete=models.CASCADE,
        related_name='events'
    )
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    event_date = models.DateField()
    event_time = models.TimeField(blank=True, null=True)
    venue = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'events'
        ordering = ['-event_date']

    def __str__(self):
        return self.name