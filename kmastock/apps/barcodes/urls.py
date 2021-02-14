from django.urls import path
from .views import generate_barcode, read_barcode

app_name = 'barcodes'
urlpatterns = [
    path('generate/photo/', generate_barcode, name='generate_barcode'),
    path('read/photo/', read_barcode, name='read_barcode'),
]
