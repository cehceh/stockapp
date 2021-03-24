from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from django.contrib import messages
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