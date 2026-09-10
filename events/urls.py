from django.urls import path
from . import views


urlpatterns = [
    # Events
    path('', views.event_list, name='event_list'),
    path('new/', views.new_event, name='new_event'),
    path('<int:event_id>/edit/', views.edit_event, name='edit_event'),
    path('<int:event_id>/delete/', views.delete_event, name='delete_event'),

    # Event Types
    path('types/', views.event_type_list, name='event_type_list'),
    path('types/new/', views.new_event_type, name='new_event_type'),
    path(
        'types/<int:event_type_id>/edit/',
        views.edit_event_type,
        name='edit_event_type'
    ),
    path(
        'types/<int:event_type_id>/delete/',
        views.delete_event_type,
        name='delete_event_type'
    ),
]