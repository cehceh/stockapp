"""kmastock URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from apps.home.views import (frontpage, dashboard, tools,
                            change_language, test_)

from django.utils.translation import gettext_lazy as _
from django.conf.urls.i18n import i18n_patterns 


urlpatterns = [
    # # frontpage 
    # path('', frontpage, name='frontpage'), # main page means english
    path('change_language/', change_language, name='change_language'), # main page means english
    # path('', test_, name="test"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Go to this site(https://samulinatri.com/blog/django-translation/)
# the site explain it well
urlpatterns += i18n_patterns( # i18n_patterns important to handel languages
    path(_('admin/'), admin.site.urls),
    
    # for authentication
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('apps.accounts.urls', namespace='accounts')),
    
    # frontpage 
    path('', frontpage, name='frontpage'), # main page means english
    # dashboard 
    path('dashboard/', dashboard, name='dashboard'),
    # Tools
    path('tools/', tools, name='tools'),
    
    
    # apps urls
    path('home/', include('apps.home.urls', namespace='home')),
    path('barcodes/', include('apps.barcodes.urls', namespace='barcodes')),
    path('category/', include('apps.category.urls', namespace='category')),
    path('clients/', include('apps.clients.urls', namespace='clients')),
    path('products/', include('apps.products.urls', namespace='products')),
    path('vendors/', include('apps.vendors.urls', namespace='vendors')),
    path('stocks/', include('apps.stocks.urls', namespace='stocks')),
    # path('', include('', namespace='')),
    # path('', include('', namespace='')),
    # path('', include('', namespace='')),
    # path('', include('', namespace='')),
    # path('', include('', namespace='')),
    # path('', include('', namespace='')),
        
    # from this site(https://samulinatri.com/blog/django-translation/)
    # put in the buttom  
    prefix_default_language=False

) 
