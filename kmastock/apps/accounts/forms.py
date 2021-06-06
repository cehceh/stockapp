from django import forms
from django.contrib.auth import get_user_model
from .models import UserProfile
from datetime import date
# User = get_user_model()

# class LoginForm(forms.Form):
#     """docstring for ."""
#     username = forms.CharField()
#     # email = forms.EmailField()
#     password = forms.CharField(widget=forms.PasswordInput)

# class RegisterForm(forms.Form):
#     username = forms.CharField()
#     email = forms.EmailField()
#     password = forms.CharField(widget=forms.PasswordInput)
#     password2 = forms.CharField(widget=forms.PasswordInput)

#     def clean_username(self):
#         username = self.cleaned_data.get('username')
#         qs = User.objects.filter(username=username)
#         if qs.exists():
#             raise forms.ValidationError("username is taken..")
#         return username

#     def clean_email(self):
#         email = self.cleaned_data.get("email")
#         qs = User.objects.filter(email=email)
#         if qs.exists():
#             raise forms.ValidationError("email is taken.. use another one")
#         return email

#     def clean(self):
#         data = self.cleaned_data
#         password = self.cleaned_data.get('password')
#         password2 = self.cleaned_data.get('password2')
#         if password2 != password:
#             raise forms.ValidationError("password must match")
#         return data

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = CustomUser
        # fields = ('username', 'email')
        fields = UserCreationForm.Meta.fields 


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        # fields = ('username', 'email')
        fields = UserChangeForm.Meta.fields


class UserProfileForm(forms.ModelForm):
    birth_date = forms.DateField(
            widget= forms.DateInput(
                attrs={
                    'type': 'date',
                    'value': date.today(),
                }
            )
    )
    class Meta:
        model  = UserProfile
        fields = (
            'address', 'birth_date', 
            'age', 'city', 'photo',
        ) #('__all__') #
    # widgets = {
    #     'birth_date': forms.DateInput(
    #                 attrs={
    #                     'type': 'date',
    #                 }
    #     )
    # }
    # 
    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
    