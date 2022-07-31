from django import forms
from django.views.generic import TemplateView

class AddressForm(forms.Form):
    name = forms.CharField(label='name', max_length=100)
    street = forms.CharField(label="street", max_length=100)
    city = forms.CharField(label="city", max_length=100)
    post_code = forms.CharField(label="post_code", max_length=6)
