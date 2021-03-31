from django.urls import path
from .views import add_product, edit_product
from django.contrib.auth.decorators import login_required

app_name = 'products'
urlpatterns = [
    path('add/new/product/', login_required(add_product),name='add_product'),
    path('edit/product/id/<int:product_id>/', login_required(edit_product),name='edit_product'),
]