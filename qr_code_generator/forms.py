# In qr_code/forms.py
from django import forms

class QRCodeForm(forms.Form):
    data = forms.CharField(label='QR Code Data', max_length=1000)