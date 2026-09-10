from django.urls import path
from . import views


urlpatterns = [
    path('', views.booking_list, name='booking_list'),
    path('new/', views.new_booking, name='new_booking'),
    path('report/', views.booking_report, name='booking_report'),

    path('<int:booking_id>/invoice/', views.invoice, name='invoice'),

    path('<int:booking_id>/approve/', views.approve_booking, name='approve_booking'),
    path('<int:booking_id>/cancel/', views.cancel_booking, name='cancel_booking'),
    path('<int:booking_id>/', views.booking_detail, name='booking_detail'),
    path('<int:booking_id>/edit/', views.edit_booking, name='edit_booking'),
    path('<int:booking_id>/delete/', views.delete_booking, name='delete_booking'),
]