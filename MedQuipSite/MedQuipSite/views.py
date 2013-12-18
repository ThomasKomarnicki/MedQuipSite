from django.shortcuts import render
from django.http import HttpResponse, Http404
from Products.models import Product,Category
import Products.view_data


def my_cart(request):
    try:
        
    except Product.DoesNotExist:
        raise Http404
    return render(request, 'product.html', {})

def checkout(request):

            
    return render(request, 'home.html', {})

def contact_us(request):
    
    
    return render(request,'contact.html')

def about_us(request):
    
    
    return render(request,'contact.html')

def home(request):
    categories = Products.view_data.get_categories()
    home_products = Products.view_data.get_home_products()

            
    return render(request, 'home.html', {'categories':categories,'products':home_products})


