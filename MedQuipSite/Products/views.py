from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from Products.models import Product,Category,Attribute
import Products.view_data as view_data
import json


def product(request, product_sku,attribute_sku=None):
    
    try:
        product = Product.objects.get(sku=product_sku)
        attribute_sku=product_sku
        view_data.add_product_to_recent(request,product)
#         recent_products = view_data.get_recent_products(request)
        category_links = view_data.get_category_links(product=product)
        attributes = Attribute.objects.filter(product=product).all()
            
        if 'attribute_sku' in request.GET:
            attribute_sku = request.GET['attribute_sku']
            attribute = Attribute.objects.filter(sku=attribute_sku).get()
            product.price = attribute.price
            product.description = attribute.description
            product.short_description = attribute.short_description
                
    except Product.DoesNotExist:
        raise Http404
    return render(request, 'product.html', dict(view_data.get_2_plus_column_base_data(request).items() + {'product': product,'attributes':attributes,'attribute_sku':attribute_sku,'category_links':category_links}.items()))


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

def add_to_cart(request, product_sku, quantity = 1):
    print "ADDING PRODUCT TO CART"
    print "SKU = "+product_sku
    print "quantity = "+str(quantity)
    if('quantity' in request.GET):
        quantity = request.GET['quantity']
    cart = None
    if("cart" in request.session):
        cart = json.loads(request.session['cart'])
    else:
        cart = []
    
    added = False
    for item in cart:
        if(item['sku'] == product_sku):
            item['count'] += quantity
            added = True
            break;
    if not added:
        cart.append({'sku':product_sku,'count':int(quantity)})
    request.session['cart'] = json.dumps(cart)
    
    
    return HttpResponseRedirect('/Cart')

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

