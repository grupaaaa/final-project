# from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models

# User = AUTH_USER_MODEL

class ShippingAddress(models.Model):
    address_line_1 = models.CharField(max_length=50)
    address_line_2 = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=5)
    city = models.CharField(max_length=50)

    #
    # def __str__(self):
    #     return

