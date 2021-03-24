from django.urls import path
from .views import add_vendor, edit_vendor
from django.contrib.auth.decorators import login_required

app_name = 'vendors'
urlpatterns = [
    path('add/new/vendor/', login_required(add_vendor), name='add_vendor'),
    path('edit/vendor/id/<int:vendor_id>/', login_required(edit_vendor), name='edit_vendor'),
]