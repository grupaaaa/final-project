from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "main/base.html"

class AddressForm(TemplateView):
    template_name = "address_form.html"
    