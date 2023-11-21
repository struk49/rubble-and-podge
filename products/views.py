from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .models import Product

# Create your views here.
def all_products(request):
    products = Product.objects.filter(active=True)

    return render(request, 'products/all.html')

