from django import forms
from .models import ShippingAddress


class AddressForm(forms.ModelForm):
    address_line_1 = forms.CharField(label='address_line_1', max_length=50)
    address_line_2 = forms.CharField(label="address_line_2", max_length=50)
    city = forms.CharField(label="city", max_length=50)
    zipcode = forms.CharField(label="zipcode", max_length=5)

    class Meta:
        model = ShippingAddress
        fields = ["address_line_1", "address_line_2", "city", "zipcode"]
