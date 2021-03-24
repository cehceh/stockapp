from django import forms
from .models import Vendor
from django.contrib.auth import get_user_model
User = get_user_model()


class VendorsForm(forms.ModelForm):
    name =  forms.CharField(required=True, label='Vendor Name',
                            widget=forms.TextInput(
                                attrs={
                                    # 'class': 'form-control',
                                    # 'type': 'text',
                                    'placeholder': 'Write the vendor name here ...',
                                })
            )

    rep_person =  forms.CharField(required=False, label='Representative Person',
                            widget=forms.TextInput(
                                attrs={
                                    # 'class': 'form-control',
                                    # 'type': 'text',
                                    'placeholder': 'Write the representative person name here ...',
                                })
            )

    description = forms.CharField(required=False, label='Description',
                            widget=forms.Textarea(
                                attrs={
                                    # 'class': 'form-control',
                                    # 'type': 'text',
                                    'placeholder': 'Write a detailed description about vendor ....',
                                })
    )
    class Meta:
        model = Vendor
        fields = ('name', 'rep_person',
                'phone', 'mobile', 'fax',
                'address', 'email', 'description',)#('__all__')
        # widgets = {
        #     'name' : forms.TextInput(
        #         attrs= {
                    
        #         },
        #     ),
        # }

    # init function is importanat in saving user automatically in create() function
    def __init__(self, *args, **kwargs):
        # self.user = user
        super(VendorsForm, self).__init__(*args, **kwargs)
        # self.fields['user'].widget.attrs['class'] = 'form-control'
        # self.fields['user'].queryset = User.objects.all()
