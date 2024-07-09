from django.db import models

class Attendance(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    attend = models.CharField(max_length=3, default='yes')