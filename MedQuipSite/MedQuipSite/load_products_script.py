import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'MedQuipSite.settings'

import json
from Products.models import Product, Category
from django.core.exceptions import ObjectDoesNotExist

if __name__ == '__main__':
    products_json = json.loads(open('mqProducts.json','r').read())
    
for key in products_json.keys():
    product = products_json[key]
    product["name"] = product["name"].encode('utf8')
categories_json = json.loads(open('categories.json','r').read())



    
Category.objects.all().delete()
Product.objects.all().delete()
for category in categories_json.keys():
    try:
        Category.objects.get(name=categories_json[category])
    except ObjectDoesNotExist:
        c = Category(name = categories_json[category].strip())
        c.save()
    
    
category_stack = []
for product_key in products_json.keys():
    product = products_json[product_key]
    prev_category = None
    try:
        product_categories = product['categories']
        for category in product_categories:
            try:
                c = Category.objects.get(name=category)
            except ObjectDoesNotExist:
                c = Category(name=category)
                c.save()
                
            if(prev_category and len(product['categories']) < 4):
                prev_category.children_ids += str(c.id) + ','
                prev_category.save()
            prev_category = c
    except:
#         print "no categories for " + str(product['name'])
        pass


            
for product_sku in products_json.keys():
    product = products_json[product_sku]
    try:      
        category_name = product['categories'][len(product['categories'])-1]     
        category_id = Category.objects.get(name=category_name).id
    except:
        category_id = -1
    name = product['name']
    sku = product_sku
    price = product['price']
    short_description = product['short_description']
    if(not short_description):
        short_description = ""
    description = product['description']
    if(not description):
        description = ""
    
    p = Product(sku=sku,name=name,category_id=category_id,price=price,short_description=short_description,description=description,attribute_type=0)
    p.save()  
    
