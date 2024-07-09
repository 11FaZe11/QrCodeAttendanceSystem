from . import views
from django.urls import path

urlpatterns = [
    path('', views.read_qr_code, name='read_qr_code'),
    ]