from django.shortcuts import render
from django.http import HttpResponse
from .models import Category
from .models import Product
from .models import Storage

# Create your views here.
def index1(request):
    query1 = Product.objects.all()
    return HttpResponse(query1)

def index2(request):
    query2 = Category.objects.all()
    return HttpResponse(query2)
