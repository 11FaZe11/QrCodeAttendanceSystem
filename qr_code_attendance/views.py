from django.shortcuts import render, redirect
from .models import Attendance

def record_attendance(request):
    if request.method == "POST":
        name = request.POST.get('name')
        Attendance.objects.create(name=name)
        return redirect('attendance_recorded')  # Redirect to the confirmation page
    return render(request, 'record_attendance.html')

def attendance_recorded(request):
    return render(request, 'attendance_recorded.html')
