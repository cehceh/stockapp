from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
# from django.contrib.auth import authenticate, login
from .forms import UserProfileForm
# from .forms import CustomUserCreationForm, CustomUserChangeForm

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.views import generic
from .models import UserProfile
from django.conf import settings
from kmastock.utils import prevent_changing_user_id

# class UserProfilePageView(generic.DetailView):
#     model = UserProfile
#     template_name = 'account/profile.html'
#     slug_field = 'profile_uuid'
#     slug_url_kwarg = 'profile_uuid'
#     context_object_name = profile
@login_required
@prevent_changing_user_id
def add_user_profile(request, user_id):
    # match = UserProfile.objects.filter(user_id=request.user.id).exists()
    # if match:
    #     profile = UserProfile.objects.get(user_id=request.user.id)
    # else:
    #     profile = None

    if request.method == 'POST':
        form = UserProfileForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            profile_form = form.save(commit=False)
            profile_form.user_id = request.user.id
            profile_form.save()
            uuid = profile_form.profile_uuid
            return redirect(reverse('accounts:edit_user_profile', args=(profile_form.user_id, uuid))) 
    else:
        form = UserProfileForm()

    context = {
        'btn' : 'Add User Profile',
        'form': form,
        # 'profile': profile,
        # 'match_user': match,
    }
    return render(request, 'account/profile.html', context)

@login_required
@prevent_changing_user_id
def edit_user_profile(request, user_id, uuid):
    # if user_id != request.user.id:
    # match = UserProfile.objects.filter(user_id=request.user.id).exists()
    # if match:
    #     qs = UserProfile.objects.get(user_id=request.user.id)
    # else:
    #     qs = None
    # if request.path == '/':
    #     request.LANGUAGE_CODE = 'en'
    # else:
    #     request.LANGUAGE_CODE 

    print(request.LANGUAGE_CODE)
    qs = UserProfile.objects.get(user_id=request.user.id)
    form = UserProfileForm(request.POST or None, request.FILES or None, instance=qs)
    if form.is_valid():
        profile_form = form.save(commit=False)
        # auth_user = request.user.id 
        profile_form.user_id = request.user.id
        profile_form.save()
        # return redirect(reverse('accounts:edit_user_profile', args=(uuid))) 
    # else:
    #     form = UserProfileForm()
    context = {
        'btn' : 'Save Changes',
        'form': form,
        # 'profile': qs,
        # 'match_user': match,
    }
    return render(request, 'account/profile.html', context)

# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request,
#             username=cd['username'],
#             password=cd['password'])
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return HttpResponse('Authenticated '\
#                                         'successfully')
#                 else:
#                     return HttpResponse('Disabled account')
#             else:
#                 return HttpResponse('Invalid login')
#     else:
#         form = LoginForm()

#     return render(request, 'account/login.html', {'form': form})







