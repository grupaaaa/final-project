from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordContextMixin

from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.db import models
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import FormView

from accounts.forms import SignUpForm
from django.core.exceptions import ImproperlyConfigured

User = get_user_model()


class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'register.html'
    success_url = reverse_lazy('accounts:login')

def profile_functionalities(request):
    login_form = AuthenticationForm()

    if request.method == 'POST':
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data('username')
            password = login_form.cleaned_data('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)

    context = {'login_form': login_form}
    return render(request, 'profile.html', context)


def basket_view(request):
    return render(request,'basket.html')

def index(request):
    return render(request, 'user/index.html')



