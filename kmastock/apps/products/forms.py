from django import forms
from .models import Product
from django.contrib.auth import get_user_model
User = get_user_model()


class ProductForm(forms.ModelForm):
    ACTIVE = (
        (True, 'Active'),
        (False, 'Disabled'),
    )
    IS_DELETED = (
        (False,'Existed'),
        (True, 'Deleted'),
    )
    name =  forms.CharField(required=True, label='Product Name',
                            widget=forms.TextInput(
                                attrs={
                                    # 'class': 'form-control',
                                    # 'type': 'text',
                                    'placeholder': 'Write the product name here ...',
                                })
            )

    # rep_person =  forms.CharField(required=False, label='Representative Person',
    #                         widget=forms.TextInput(
    #                             attrs={
    #                                 # 'class': 'form-control',
    #                                 # 'type': 'text',
    #                                 'placeholder': 'Write the representative person name here ...',
    #                             })
    #         )

    description = forms.CharField(required=False, label='Description',
                            widget=forms.Textarea(
                                attrs={
                                    # 'class': 'form-control',
                                    # 'type': 'text',
                                    'placeholder': 'Write a detailed description about vendor ....',
                                })
    )
    active = forms.BooleanField(required=False, label='Active',
                            widget=forms.Select(choices= ACTIVE,
                                attrs={
                                    # 'class': 'form-control',
                                    # 'type': 'text',
                                })
    )
    is_deleted = forms.BooleanField(required=False, label='Deleted',
                            widget=forms.Select(choices= IS_DELETED,
                                attrs={
                                    # 'class': 'form-control',
                                    # 'type': 'text',
                                    
                                })
    )

    class Meta:
        model = Product
        fields = ('vendor', 'category', 'stock', 'name', 'barcode',
                'originprice', 'price', 'image', 'description',
                'active', 'is_deleted',)
        widgets = {
            'vendor': forms.Select(
                attrs={
                    'required':'true'
                }
            ),
            'category': forms.Select(
                attrs={
                    'required':'true'
                }
            ),
            'stock': forms.Select(
                attrs={
                    'required':'true'
                }
            )
        }
    # init function is importanat in saving user automatically in create() function
    def __init__(self, *args, **kwargs):
        # self.user = user
        super(ProductForm, self).__init__(*args, **kwargs)
        # self.fields['user'].widget.attrs['class'] = 'form-control'
        # self.fields['user'].queryset = User.objects.all()
