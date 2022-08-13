from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm



User = get_user_model()


def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        # print("post")
        form = UserCreationForm(request.POST)
        # print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login/')

    else:
        form = UserCreationForm()


    context = {'form': form}
    return render(request, 'register.html', context)


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

    context = {'login_form': login_form }
    return render(request, 'profile.html', context)


def basket_view(request):
    return render(request,'basket.html')



