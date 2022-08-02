import urllib

from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        # print("post")
        form = UserCreationForm(request.POST)
        # print(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Account created successfully')

            return redirect('/accounts/')
        else:
            form = UserCreationForm()
            messages.error(request, 'Account creation failed')

    context = {'form': form}
    return render(request, 'register.html', context)
