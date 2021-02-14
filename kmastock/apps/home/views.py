from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.conf import settings
from django.utils import translation

# Create your views here.

def frontpage(request):
    ''' Home page before user sign in '''
    context = {}
    return render(request, 'home/frontpage.html', context)

# handel changes between languages in frontpage 
def en_frontpage(request): 
    ''' Handeling English Language '''
    # from django.utils import translation
    user_language = 'en' 
    translation.activate(user_language)
    response = render(request, 'home/frontpage.html')
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)
    return response

def ar_frontpage(request): 
    ''' Handeling Arabic Language '''
    user_language = 'ar' 
    translation.activate(user_language)
    response = render(request, 'home/frontpage.html')
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)
    return response


def de_frontpage(request): 
    ''' Handeling German Language '''
    user_language = 'de' 
    translation.activate(user_language)
    response = render(request, 'home/frontpage.html')
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)
    return response

#################################
def dashboard(request):
    ''' Dashboard page main page means English'''
    context = {}
    return render(request, 'home/dashboard.html', context)


def ar_dashboard(request): 
    ''' Handeling dashboard Arabic Language '''
    # from django.utils import translation
    user_language = 'ar' 
    translation.activate(user_language)
    response = render(request, 'home/dashboard.html')
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)
    return response


def de_dashboard(request): 
    ''' Handeling dashboard German Language '''
    # from django.utils import translation
    user_language = 'de' 
    translation.activate(user_language)
    response = render(request, 'home/dashboard.html')
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)
    return response

################### For changing URL for every language ################   
def change_language(request):
    response = HttpResponseRedirect('/')
    if request.method == 'POST':
        language = request.POST.get('language')
        if language:
            if language != settings.LANGUAGE_CODE and [lang for lang in settings.LANGUAGES if lang[0] == language]:
                redirect_path = f'/{language}/'
            elif language == settings.LANGUAGE_CODE:
                redirect_path = '/'
            else:
                return response
            translation.activate(language)
            response = HttpResponseRedirect(redirect_path)
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    return response

############ Tools ################
def tools(request):
    '''  '''
    context = {}
    return render(request, 'base/tools_navbar.html', context)