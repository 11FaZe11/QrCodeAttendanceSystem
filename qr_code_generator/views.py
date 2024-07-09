from django.shortcuts import render, redirect
import pyqrcode
from django.http import HttpResponse, HttpResponseRedirect
from io import BytesIO
from .forms import QRCodeForm
import base64



def qr_code(request):
    form = QRCodeForm(request.POST or None)
    qr_code_image = None
    if request.method == "POST" and form.is_valid():
        data = form.cleaned_data['data']
        image_png = generate_qr_code(data)
        # Encode the QR code image in base64
        qr_code_image = base64.b64encode(image_png).decode('utf-8')
        if 'download' in request.GET:
            response = HttpResponse(image_png, content_type="image/png")
            response['Content-Disposition'] = 'attachment; filename="qr_code.png"'
            return response
    return render(request, 'qr_code_generator.html', {'form': form, 'qr_code_image': qr_code_image})

def generate_qr_code(data):
    qr = pyqrcode.create(data)
    buffer = BytesIO()
    qr.png(buffer, scale=5)
    image_png = buffer.getvalue()
    return image_png


