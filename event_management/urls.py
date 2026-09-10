from django.contrib import admin
from django.urls import path, include
from accounts.views import dashboard, settings_view


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('accounts.urls')),
    path('dashboard/', dashboard, name='dashboard'),

    path('bookings/', include('bookings.urls')),
    path('events/', include('events.urls')),
    path('services/', include('services.urls')),
    path('users/', include('users.urls')),
    path('settings/', settings_view, name='settings'),
]