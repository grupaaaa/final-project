from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=100)
    # username = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # password1 = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # password2 = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')