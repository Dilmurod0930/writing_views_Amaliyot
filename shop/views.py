from django.shortcuts import render
from .models import Product, Category
from django.http  import  HttpResponse
# Create your views here.

def index(request):
    praducts = Product.objects.all()
    context = {
        'praducts': praducts
    }
    return render(request, 'shop/index.html', context)

def about(request):
    return render(request, 'shop/about.html')
    

def  product_detail(request, product_id):
    try:

        product = Product.objects.get(id=product_id)
        context = {
            'product': product
        }
    
        return render(request, 'shop/detail.html', context)
        

    except  Product.DoesNotExist:
        return  HttpResponse("Pradukt  Paje  Topilmadi. ")