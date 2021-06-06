from django.urls import path
from .views import (frontpage, dashboard, tools)


app_name = 'home'
urlpatterns = [
    path('tools/', tools, name='tools'),
    
]

