from django import forms
from .models import ShippingAddress, validate_address_line_1, validate_city, validate_zip_code
from django.core import validators
from django.forms import CharField
from django.core.exceptions import ValidationError




class AddressForm(forms.ModelForm):
    address_line_1 = forms.CharField(label='address_line_1', max_length=50, validators=[validate_address_line_1])
    address_line_2 = forms.CharField(label="address_line_2", max_length=50)
    city = forms.CharField(label="city", max_length=50, validators=[validate_city])
    zipcode = forms.CharField(label="zipcode", max_length=5, validators=[validate_zip_code])

    class Meta:
        model = ShippingAddress
        fields = ["address_line_1", "address_line_2", "city", "zipcode"]

    # def validate_zip_code(zipcode):
    #     if zipcode != float:
    #         raise ValidationError("Please enter a valid zip code.")
    #     if len(zipcode) != 5:
    #         raise ValidationError("Please enter a valid zip code.")
    #
    # def validate_city(city):
    #     if len(str(city)) < 2:
    #         raise ValidationError("Please enter a valid city.")
    #
    # def validate_address_line_1(address_line_1):
    #     if len(str(address_line_1)) < 4:
    #         raise ValidationError("Please enter the first line of your address.")
