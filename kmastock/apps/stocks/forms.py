from django import forms
from .models import Stock
from django.contrib.auth import get_user_model
User = get_user_model()


class StocksForm(forms.ModelForm):
    name = forms.CharField(required=True, label='Stock Name',
                            widget=forms.TextInput(
                                attrs={
                                    'class': 'form-control',
                                    'type': 'text',
                                    'placeholder': 'Write the stock name here ...',
                                })
    )

    # eventdate = forms.DateField(required=True, label='Event Date',
    #                         widget=forms.TextInput(
    #                             attrs={
    #                                 'class': 'form-control',
    #                                 'type': 'text',
    #                                 'value': date.today(),
    #                             })
    # )

    description = forms.CharField(required=False, label='Description',
                            widget=forms.Textarea(
                                attrs={
                                    'class': 'form-control',
                                    'type': 'text',
                                    'placeholder': 'Write a detailed description for your stock ....',
                                })
    )
    class Meta:
        model = Stock
        fields = ('user', 'name', 'description')#('__all__')
    
    # init function is importanat in saving user automatically in create() function
    def __init__(self, *args, **kwargs):
        # self.user = user
        super(StocksForm, self).__init__(*args, **kwargs)
        # self.fields['user'].widget.attrs['class'] = 'form-control'
        # self.fields['user'].queryset = User.objects.all()
