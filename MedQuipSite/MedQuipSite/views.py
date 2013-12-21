from django.shortcuts import render
from django.http import HttpResponse, Http404
from Products.models import CartItem
import Products.view_data as view_data
import json


def my_cart(request):
    cart = None
    if("cart" in request.session):
        cart = json.loads(request.session['cart'])
    shopping_cart = []
    for item in cart:
        shopping_cart.append(CartItem(item['sku'], item['count']))
    
    subtotal = 0
    tax_total = 0  
    for item in shopping_cart:
        subtotal+=(item.product.price * item.count)
    
    tax_total = subtotal * .07
    grand_total = subtotal + tax_total
    # make these things suitable for display
        
    return render(request, 'myCart.html', dict(view_data.get_2_plus_column_base_data(request).items() + {'cart':shopping_cart}.items()))

def checkout(request):
    
            
    return render(request, 'checkout.html', {})

def contact_us(request):
    
    
    return render(request,'contact.html')

def about_us(request):
    
    
    return render(request,'contact.html')

def home(request):
    categories = view_data.get_categories()
    home_products = view_data.get_home_products()
            
    return render(request, 'home.html', dict(view_data.get_2_plus_column_base_data(request).items() + {'categories':categories,'products':home_products}.items()))

def search(request):
    products = []
    if'product_query' in request.GET:
        product_query = request.GET['product_query']
        products = view_data.search(product_query)
        
    categories = view_data.get_categories()
    return render(request,'product_search.html',dict(view_data.get_2_plus_column_base_data(request).items() + {'categories':categories,'products':products}.items()))
        # find products related to the search 


