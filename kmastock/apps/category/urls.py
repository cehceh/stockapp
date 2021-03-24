from django.urls import path
from .views import add_category, edit_category
from django.contrib.auth.decorators import login_required

app_name = 'category'
urlpatterns = [
    path('add/new/category/', login_required(add_category), name='add_category'),
    path('edit/category/id/<int:category_id>/', login_required(edit_category), name='edit_category'),
]