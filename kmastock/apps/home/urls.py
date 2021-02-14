from django.urls import path
from .views import (frontpage, dashboard, en_frontpage, 
                    ar_frontpage, de_frontpage, tools)


app_name = 'home'
urlpatterns = [
    # path('english/', en_frontpage, name='en_frontpage'), # no need to it 
    # path('arabic/', ar_frontpage, name='ar_frontpage'),
    # path('german/', de_frontpage, name='de_frontpage'),
    path('tools/', tools, name='tools'),
    
]

