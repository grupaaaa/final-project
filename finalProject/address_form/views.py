from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView

from .forms import AddressForm
from .models import ShippingAddress

from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt


class AddressFormView(TemplateView):
    template_name = "address_form/address_form.html"

class AddresSuccessfulView(TemplateView):
    template_name = "address_form/address_successful.html"

#TODO:Once login ready delete line below
@csrf_exempt
def get_address(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('successful/')
    else:
        form = AddressForm()

    return render(request, 'address_form/address_form.html', {'form': form})

