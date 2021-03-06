from django.shortcuts import render,reverse,redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
import os
import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image
# Create your views here.

def generate_barcode(request): # Done Good Job man
    # Generate QR Code
    barcode_value = request.GET.get('code')
    if barcode_value == None:
        messages.success(request, 'Create barcode without value is not valid')
        # qr = pyqrcode.create("12345")
        # qr.png('barcode_12345.png', scale=10)
    elif barcode_value != None:
        qr = pyqrcode.create(barcode_value)
        file_path = 'D:\Django\projects\stock\mybarcode\\barcode_' + str(barcode_value) + '_.png'
        if not os.path.exists(file_path):
            qr.png('D:\Django\projects\stock\mybarcode\\barcode_' + str(barcode_value) + '_.png', scale=10)
            messages.success(request, 'Create barcode completed with name '+ '(barcode_' + str(barcode_value) + '_.png)', extra_tags='Creation Done')
        else:
            messages.success(request, 'Barcode is already exists')
            return HttpResponseRedirect(reverse('barcodes:generate_barcode'))
    return render(request, 'barcodes/generate_barcode.html', {'value': barcode_value})

####
def read_barcode(request):
    # Read QR Code
    reader = request.GET.get('reader')
    result = '' #request.GET.get('barcode')
    file_path = str(reader) 
    if reader == None or reader == '':
        messages.success(request, 'It\'s not valid')
        # d = decode(Image.open('D:\Django\projects\stock\mybarcode\\barcode_Ecc_.png'))
        # result = d[0].data.decode('ascii')
    elif not os.path.exists(file_path):
        messages.success(request, 'File path is not correct')
    else: 
        d = decode(Image.open(reader))
        result = d[0].data.decode('ascii')
        # print(result)
    context = {'code': result,}

    return render(request, 'barcodes/read_barcode.html', context)

