from pyexpat import model
from django import forms
from aboutUs.models import Customer


class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ('name', 'phone', 'comment')
