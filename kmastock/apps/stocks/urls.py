from django.urls import path
from .views import add_stock, edit_stock


app_name = 'stocks'
urlpatterns = [
    path('add/new/stock/', add_stock,name='add_stock'),
    path('edit/stock/id/<int:stock_id>/', edit_stock,name='edit_stock'),
]