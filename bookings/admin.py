from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'customer_name',
        'customer_email',
        'event',
        'service',
        'booking_date',
        'guests',
        'amount',
        'status',
    )

    search_fields = (
        'customer_name',
        'customer_email',
        'customer_phone',
    )

    list_filter = (
        'status',
        'booking_date',
        'event',
        'service',
    )