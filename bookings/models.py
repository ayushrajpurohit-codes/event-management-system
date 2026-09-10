from django.db import models
from events.models import Event
from services.models import Service


class Booking(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Cancelled', 'Cancelled'),
    ]

    customer_name = models.CharField(max_length=150)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=20)

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='bookings'
    )

    service = models.ForeignKey(
        Service,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='bookings'
    )

    booking_date = models.DateField()
    guests = models.PositiveIntegerField(default=1)
    venue = models.CharField(max_length=255)

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'bookings'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.customer_name} - {self.event.name}"