from django.shortcuts import render
from django.http import HttpResponse, Http404
from Products.models import Product,Category
import Products.view_data


def product(request, product_sku):
    try:
        product = Product.objects.get(sku=product_sku)
        category_links = Products.view_data.get_category_links(product=product)
    except Product.DoesNotExist:
        raise Http404
    return render(request, 'product.html', {'product': product,'category_links':category_links})

def category(request, category_id):
    try:
        category = Category.objects.filter(id=category_id).get()
        category_links = Products.view_data.get_category_links(category=category)
        categories = Products.view_data.get_categories(category_id)
        if(not categories):
            categories = Products.view_data.get_categories()
        products = Products.view_data.get_products_in_category(category,categories=categories)
        
    except Category.DoesNotExist:
        raise Http404
    
    
    return render(request, 'category.html', {'category_links':category_links,'categories':categories,'products':products})





