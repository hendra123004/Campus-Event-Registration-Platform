from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('participants/', views.participants, name='participants'),
    path('participants/<int:event_id>/', views.participants, name='participants_by_event'),  # <— ini penting
]

