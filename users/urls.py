from django.urls import path
from . import views


urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('new/', views.new_user, name='new_user'),
    path('<int:user_id>/edit/', views.edit_user, name='edit_user'),
    path('<int:user_id>/delete/', views.delete_user, name='delete_user'),
]