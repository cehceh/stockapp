from django.urls import path
from .views import add_product, edit_product


app_name = 'products'
urlpatterns = [
    path('add/new/product/', add_product,name='add_product'),
    path('edit/product/id/<int:product_id>/', edit_product,name='edit_product'),
]