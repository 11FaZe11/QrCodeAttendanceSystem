from django.urls import path
from . import views

urlpatterns = [
    path('record_attendance/', views.record_attendance, name='record_attendance'),
    path('attendance_recorded/', views.attendance_recorded, name='attendance_recorded'),  # New URL pattern
]