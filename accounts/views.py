from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from bookings.models import Booking


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('dashboard')

        return render(
            request,
            'accounts/login.html',
            {'error': 'Invalid username or password'}
        )

    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard(request):
    total_bookings = Booking.objects.count()
    approved_bookings = Booking.objects.filter(status='Approved').count()
    pending_bookings = Booking.objects.filter(status='Pending').count()
    cancelled_bookings = Booking.objects.filter(status='Cancelled').count()

    context = {
        'total_bookings': total_bookings,
        'approved_bookings': approved_bookings,
        'pending_bookings': pending_bookings,
        'cancelled_bookings': cancelled_bookings,
    }

    return render(
        request,
        'dashboard/dashboard.html',
        context
    )


@login_required
def settings_view(request):
    return render(
        request,
        'settings/settings.html'
    )