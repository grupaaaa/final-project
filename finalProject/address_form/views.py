from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView

from .forms import AddressForm

from django import forms
from django.views.generic import TemplateView

class AddressForm(forms.Form):
    name = forms.CharField(label='name', max_length=100)
    street = forms.CharField(label="street", max_length=100)
    city = forms.CharField(label="city", max_length=100)
    post_code = forms.CharField(label="post_code", max_length=6)

def get_address(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AddressForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AddressForm()

    return render(request, 'name.html', {'form': form})
