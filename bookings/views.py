from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking
from events.models import Event
from services.models import Service


@login_required
def booking_list(request):
    bookings = Booking.objects.select_related(
        'event',
        'service'
    ).all()

    return render(
        request,
        'bookings/booking_list.html',
        {'bookings': bookings}
    )


@login_required
def new_booking(request):
    events = Event.objects.filter(status=True)
    services = Service.objects.filter(status=True)

    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        customer_email = request.POST.get('customer_email')
        customer_phone = request.POST.get('customer_phone')
        event_id = request.POST.get('event')
        service_id = request.POST.get('service')
        booking_date = request.POST.get('booking_date')
        guests = request.POST.get('guests')
        venue = request.POST.get('venue')
        amount = request.POST.get('amount') or 0
        notes = request.POST.get('notes')

        event = get_object_or_404(
            Event,
            id=event_id,
            status=True
        )

        service = None

        if service_id:
            service = get_object_or_404(
                Service,
                id=service_id,
                status=True
            )

        Booking.objects.create(
            customer_name=customer_name,
            customer_email=customer_email,
            customer_phone=customer_phone,
            event=event,
            service=service,
            booking_date=booking_date,
            guests=guests,
            venue=venue,
            amount=amount,
            notes=notes,
            status='Pending'
        )

        return redirect('booking_list')

    context = {
        'events': events,
        'services': services,
    }

    return render(
        request,
        'bookings/new_booking.html',
        context
    )


@login_required
def approve_booking(request, booking_id):
    booking = get_object_or_404(
        Booking,
        id=booking_id
    )

    booking.status = 'Approved'
    booking.save()

    return redirect('booking_list')


@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(
        Booking,
        id=booking_id
    )

    booking.status = 'Cancelled'
    booking.save()

    return redirect('booking_list')


@login_required
def booking_detail(request, booking_id):
    booking = get_object_or_404(
        Booking.objects.select_related(
            'event',
            'service'
        ),
        id=booking_id
    )

    return render(
        request,
        'bookings/booking_detail.html',
        {'booking': booking}
    )


@login_required
def edit_booking(request, booking_id):
    booking = get_object_or_404(
        Booking,
        id=booking_id
    )

    events = Event.objects.filter(status=True)
    services = Service.objects.filter(status=True)

    if request.method == 'POST':
        booking.customer_name = request.POST.get('customer_name')
        booking.customer_email = request.POST.get('customer_email')
        booking.customer_phone = request.POST.get('customer_phone')

        event_id = request.POST.get('event')
        service_id = request.POST.get('service')

        booking.event = get_object_or_404(
            Event,
            id=event_id,
            status=True
        )

        if service_id:
            booking.service = get_object_or_404(
                Service,
                id=service_id,
                status=True
            )
        else:
            booking.service = None

        booking.booking_date = request.POST.get('booking_date')
        booking.guests = request.POST.get('guests')
        booking.venue = request.POST.get('venue')
        booking.amount = request.POST.get('amount') or 0
        booking.notes = request.POST.get('notes')

        booking.save()

        return redirect('booking_list')

    context = {
        'booking': booking,
        'events': events,
        'services': services,
    }

    return render(
        request,
        'bookings/edit_booking.html',
        context
    )


@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(
        Booking,
        id=booking_id
    )

    booking.delete()

    return redirect('booking_list')


@login_required
def booking_report(request):
    bookings = Booking.objects.select_related(
        'event',
        'service'
    ).all()

    total_bookings = bookings.count()
    approved_bookings = bookings.filter(status='Approved').count()
    pending_bookings = bookings.filter(status='Pending').count()
    cancelled_bookings = bookings.filter(status='Cancelled').count()

    total_amount = sum(
        booking.amount for booking in bookings
    )

    context = {
        'bookings': bookings,
        'total_bookings': total_bookings,
        'approved_bookings': approved_bookings,
        'pending_bookings': pending_bookings,
        'cancelled_bookings': cancelled_bookings,
        'total_amount': total_amount,
    }

    return render(
        request,
        'bookings/booking_report.html',
        context
    )


@login_required
def invoice(request, booking_id):
    booking = get_object_or_404(
        Booking.objects.select_related(
            'event',
            'event__event_type',
            'service'
        ),
        id=booking_id
    )

    return render(
        request,
        'bookings/invoice.html',
        {'booking': booking}
    )