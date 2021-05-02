from django import forms
from .models import Categories
from django.contrib.auth import get_user_model
User = get_user_model()


class CategoryForm(forms.ModelForm):
    ACTIVE = (
        (True, 'Active'),
        (False, 'Disabled'),
    )
    IS_DELETED = (
        (False,'Existed'),
        (True, 'Deleted'),
    )
    name =  forms.CharField(required=True, label='Category Name',
                            widget=forms.TextInput(
                                attrs={
                                    # 'class': 'form-control',
                                    # 'type': 'text',
                                    'placeholder': 'Write the category name here ...',
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
        model = Categories
        fields = ('name', 'description',
                'active', 'is_deleted',)#('__all__')
        # widgets = {
        #     'name' : forms.TextInput(
        #         attrs= {
                    
        #         },
        #     ),
        # }

    # init function is importanat in saving user automatically in create() function
    def __init__(self, *args, **kwargs):
        # self.user = user
        super(CategoryForm, self).__init__(*args, **kwargs)
        # self.fields['user'].widget.attrs['class'] = 'form-control'
        # self.fields['user'].queryset = User.objects.all()
