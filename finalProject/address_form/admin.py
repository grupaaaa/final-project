from django.contrib import admin

# Register your models here.
from address_form.models import ShippingAddress

admin.site.register(ShippingAddress)