import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'MedQuipSite.settings'

from Products.models import Product,Category,Attribute
from Customers.models import Customer, Order
import json


if __name__ == '__main__':
    file = open("database_json.json","r")

j = json.loads(file.read())



products = Product.objects.all()
for product in products:
    product.delete()
    
attributes = Attribute.objects.all()
for attribute in attributes:
    attribute.delete()
    
categories = Category.objects.all()
for category in categories:
    category.delete()

objects = j['categories']
for object in objects:
    db_object = Category()
    db_object.__dict__.update(object)
    db_object.save()
    
objects = j['products']
for object in objects:
    db_object = Product()
    db_object.__dict__.update(object)
    db_object.name = db_object.name.encode("ascii","ignore")
    db_object.save()
    
objects = j['attributes']
for object in objects:
    db_object = Attribute()
    db_object.__dict__.update(object)
    db_object.save()
    
# objects = j['customers']
# for object in objects:
#     db_object = Customer()
#     db_object.__dict__.update(object)
#     db_object.save()
#     
# objects = j['orders']
# for object in objects:
#     db_object = Category()
#     db_object.__dict__.update(object)
#     db_object.save()