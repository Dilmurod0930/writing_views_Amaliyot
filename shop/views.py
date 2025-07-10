from django.shortcuts import render
from .models import Product, Category
from django.http  import  HttpResponse
# Create your views here.

def index(request,  catigorya_id=None):
    categories = Category.objects.all()
    searech_query = request.GET.get('q', '')
    if catigorya_id:
        praducts = Product.objects.filter(category = catigorya_id)
    else:
        praducts = Product.objects.all()

    if searech_query:
        praducts = praducts.filter(name__icontains=searech_query)
    if not praducts:
        return render(request, 'shop/eror.html')
    
    
    context = {
            'praducts': praducts,
            'categories': categories
        }
    return render(request, 'shop/index.html', context)





def  product_detail(request, product_id):
    try:
        
        product = Product.objects.get(id=product_id)
        context = {
            'product': product
        }
    
        return render(request, 'shop/product_detail.html', context)
        

    except  Product.DoesNotExist:
        return  HttpResponse("Pradukt  Paje  Topilmadi. ")