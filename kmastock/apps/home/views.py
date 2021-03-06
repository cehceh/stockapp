from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from django.contrib import messages
from django.conf import settings
from django.utils import translation
from apps.accounts.models import UserProfile


# Create your views here.
def frontpage(request):
    ''' Home page before user sign in '''
    # response = HttpResponseRedirect('hello')
    # if request.path == '/':
    #     request.LANGUAGE_CODE = 'en'
    #     language = 'en'
    # else:
    #     request.LANGUAGE_CODE = language 
    # language = request.GET.get('language')
    # language = request.POST.get('language')
    response = HttpResponse('hello')
    lang_path = request.path #.split('/')[1]
    # print('language: '+str(language), lang_path, 'frontpage_LANG_CODE: '+ str(request.LANGUAGE_CODE))
    print(lang_path, 'frontpage_LANG_CODE: '+ str(request.LANGUAGE_CODE))
    
            # translation.activate(language)
            # response = HttpResponseRedirect(redirect_path)
            # response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    # return response
    # match = UserProfile.objects.filter(user_id=request.user.id).exists()
    # if match:
    #     profile = UserProfile.objects.get(user_id=request.user.id)
    # else:
    #     profile = None

    # print(match, request.user.id, profile)
    key = request.session.session_key
    # print(dir(request.session), key)
    print(request.session.get('username'))
    context = {
        # 'match_user': match,
        # 'profile': profile,
    }
    # return response
    return render(request, 'home/frontpage.html', context)

# if request.method == 'POST':
    #     language = request.POST.get('language')
    #     print('language:- ' + language)
    #     if language:
    #     # if request.LANGUAGE_CODE :
    #         # if language != settings.LANGUAGE_CODE: #and [lang for lang in settings.LANGUAGES if lang[0] == language]: 
    #         if language == settings.LANGUAGES[1][0]: #and [lang for lang in settings.LANGUAGES if lang[0] == language]: 
    #             redirect_path = f'/{language}/'
    #             translation.activate(language)
    #             response = HttpResponseRedirect(redirect_path)
    #             response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    #             print(language, redirect_path)
    #             return response #HttpResponseRedirect(f'/{language}/') #render(request, redirect_path)
    #         elif language == settings.LANGUAGES[2][0]:
    #             print(language)
    #             redirect_path = f'/{language}/'
    #             translation.activate(language)
    #             response = HttpResponseRedirect(redirect_path)
    #             response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    #             return response
    #         else:
    #             print(language)
    #             translation.activate(language)
    #             response = HttpResponseRedirect(redirect_path)
    #             response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    #             return response


    
# handel changes between languages in frontpage 
# def en_frontpage(request):  ## It is useless till now
#     ''' Handeling English Language '''
#     # from django.utils import translation
#     user_language = 'en' 
#     translation.activate(user_language)
#     response = render(request, 'home/frontpage.html')
#     response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)
#     return response

# def ar_frontpage(request): 
#     ''' Handeling Arabic Language '''
#     user_language = 'ar' 
#     translation.activate(user_language)
#     response = render(request, 'home/frontpage.html')
#     response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)
#     return response


# def de_frontpage(request): 
#     ''' Handeling German Language '''
#     user_language = 'de' 
#     translation.activate(user_language)
#     response = render(request, 'home/frontpage.html')
#     response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)
#     return response

#################################
def dashboard(request):
    ''' Dashboard page main page means English'''
    from xml.dom import minidom
    # parse an xml file by name
    mydoc = minidom.parse('myfile.xml')
    items = mydoc.getElementsByTagName('item')
    # num1 = items[0].firstChild.data          # access data
    # attr1 = items[0].attributes['num'].value # access atribute name value
    num2 = items[1].childNodes[0].data       # access data
    # attr2 = items[1].attributes['num'].value # access atribute name value
    context = {
        'num2':num2,
    }
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
    response = HttpResponseRedirect('/en/')
    if request.method == 'POST':
        language = request.POST.get('language')
        if language:
            # print(settings.LANGUAGE_CODE)
            if language != settings.LANGUAGE_CODE and [lang for lang in settings.LANGUAGES if lang[0] == language]:
            # if language != settings.LANGUAGES[0][0]:
                print(language, settings.LANGUAGES[0][0])
                print(settings.LANGUAGES[1][0])
                print(settings.LANGUAGES[2])
                print(settings.LANGUAGE_CODE)
                redirect_path = f'/{language}/'
            elif language == settings.LANGUAGE_CODE:
                print('your settings' + settings.LANGUAGE_CODE)
                redirect_path = '/en/'
            else:
                print(settings.LANGUAGES[1])
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


def test_(request):
    from xml.dom import minidom
    # parse an xml file by name
    # mydoc = minidom.parse('item.xml')
    # items = mydoc.getElementsByTagName('item')
    # num1 = items[0].firstChild.data          # access data
    # attr1 = items[0].attributes['num'].value # access atribute name value
    # num2 = items[1].childNodes[0].data       # access data
    # attr2 = items[1].attributes['num'].value # access atribute name value

    # if num2 > attr2:
    #     messages.success(request, 'num2 is great number')
    #     return redirect('/de')
    
    # create xml file
    import xml.etree.ElementTree as ET
    # create the file structure
    data = ET.Element('dataroot')
    items = ET.SubElement(data, 'items')
    item1 = ET.SubElement(items, 'item')
    item2 = ET.SubElement(items, 'item')
    x = 0
    # x += 1
    item1.set('name', str(x))
    item2.set('name','20')
    for e in range(0,3):
        e += 1
    # if x == 0:
    #     x +=1
    item1.text = str(e)
    item2.text = '2'

    # create a new XML file with the results
    mydata = ET.tostring(data)
    myfile = open("myfile.xml", "wb") # wb insteed of w to write binary
    myfile.write(mydata)
    if int(item1.text) == int(3):
        return redirect('/dashboard')
    
    # myxml = ET.parse("myfile.xml")
    # item = myxml.getElementsByTagName('item')
    # var = item[0].childNodes[0].data 
    # if num1 > 0:
    #     num1 +=1
    #     messages.success(request, 'good')
    context = {
        # 'var': var,
        # 'num1': num1,
        # 'num2': num2,
        # 'attr1': attr1,
        # 'attr2':attr2,
    }
    return render(request, 'base/sidebar.html', context)