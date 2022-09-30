# from django.conf.global_settings import AUTH_USER_MODEL
from django.core.exceptions import ValidationError
from django.db import models

def validate_zip_code(zipcode):
    if len(zipcode) != 5:
        raise ValidationError("Please enter a valid zip code.")

def validate_city(city):
    if len(str(city)) < 2:
        raise ValidationError("Please enter a valid city.")

def validate_address_line_1(address_line_1):
    if len(str(address_line_1)) < 3:
        raise ValidationError("Please enter the first line of your address.")

# User = AUTH_USER_MODEL

class ShippingAddress(models.Model):
    address_line_1 = models.CharField(max_length=50, validators=[validate_address_line_1])
    address_line_2 = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=5, validators=[validate_zip_code])
    city = models.CharField(max_length=50, validators=[validate_city])

    #
    # def __str__(self):
    #     return

