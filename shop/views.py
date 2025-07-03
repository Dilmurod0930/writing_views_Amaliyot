from django.shortcuts import render
from .models import Product, Category
# Create your views here.

def index(request):
    praducts = Product.objects.all()
    context = {
        'praducts': praducts
    }
    return render(request, 'shop/index.html', context)

def about(request):
    return render(request, 'shop/about.html')
    