from django.urls import path
from . import views


urlpatterns = [
    path('', views.service_list, name='service_list'),
    path('new/', views.new_service, name='new_service'),
    path('<int:service_id>/edit/', views.edit_service, name='edit_service'),
    path('<int:service_id>/delete/', views.delete_service, name='delete_service'),
]