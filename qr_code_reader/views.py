from django.shortcuts import render
from django.http import HttpResponse
from pyzbar.pyzbar import decode
from PIL import Image

def read_qr_code(request):
    message = ''  # Initialize an empty message
    if request.method == 'POST' and request.FILES.get('qr_image', None):
        qr_image = request.FILES['qr_image']
        image = Image.open(qr_image)
        decoded_objects = decode(image)
        if decoded_objects:
            data = decoded_objects[0].data.decode("utf-8")
            message = f"Decoded QR code data: {data}"
        else:
            message = "No QR code found."
    return render(request, 'qr_code_reader.html', {'message': message})