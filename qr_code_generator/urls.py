from . import views
from django.urls import path

urlpatterns = [
    path('', views.qr_code, name='qr_code'),
]