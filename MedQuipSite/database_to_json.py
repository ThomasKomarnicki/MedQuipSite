import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'MedQuipSite.settings'

import json
from Products.models import Product, Category, Attribute
from Customers.models import Customer, Order
from django.core.exceptions import ObjectDoesNotExist

if __name__ == '__main__':
    categories = []
    products = []
    customers = []
    orders = []
    attributes = []
    for category in Category.objects.all().values():
        categories.append(category)
        
    for product in Product.objects.all().values():
        product['price'] = str(product['price'])
        products.append(product)
        
    for object in Attribute.objects.all().values():
        attributes.append(object)
        
    for object in Customer.objects.all().values():
        customers.append(object)
        
    for object in Order.objects.all().values():
        orders.append(object)
        
        
open("database_json.json",'w').write(json.dumps({'categories':categories,'products':products,'customers':customers,'orders':orders,'attributes':attributes}))
        