from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from Products.models import Product,Category
import Products.view_data as view_data
import json


def product(request, product_sku):
    try:
        product = Product.objects.get(sku=product_sku)
        view_data.add_product_to_recent(request,product)
        recent_products = view_data.get_recent_products(request)
        category_links = view_data.get_category_links(product=product)
    except Product.DoesNotExist:
        raise Http404
    return render(request, 'product.html', dict(view_data.get_2_plus_column_base_data(request).items() + {'product': product,'category_links':category_links}.items()))

def category(request, category_id):
    try:
        category = Category.objects.filter(id=category_id).get()
        category_links = view_data.get_category_links(category=category)
        categories = view_data.get_categories(category_id)
        if(not categories):
            categories = view_data.get_categories()
        products = view_data.get_products_in_category(category,categories=categories)
        recent_products = view_data.get_recent_products(request)
        
    except Category.DoesNotExist:
        raise Http404
    
    
    return render(request, 'category.html', dict(view_data.get_2_plus_column_base_data(request).items() + {'category_links':category_links,'categories':categories,'products':products}.items()))

def add_to_cart(request, product_sku, quanity = 1):
    
    cart = None
    if("cart" in request.session):
        cart = json.loads(request.session['cart'])
    else:
        cart = []
    cart.append({'sku':product_sku,'count':1})
    request.session['cart'] = json.dumps(cart)
    
    
    return HttpResponseRedirect(request,'/Cart')

def remove_from_cart(request,product_sku):
    
    if("cart" in request.session):
        cart = json.loads(request.session['cart'])
        for item in cart:
            if(item['sku'] == product_sku):
                cart.remove(item)
                break
        request.session['cart'] = json.dumps(cart)
    
    return HttpResponseRedirect(request,'/Cart')

def update_cart(request):
    
    
    return HttpResponseRedirect(request,'/Cart')

