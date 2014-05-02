import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'MedQuipSite.settings'

from Products.models import Product, Category, Attribute
import json
from os import listdir
from os.path import isfile, join

if __name__ == '__main__':
    products_deleted = 0
    for attribute in Attribute.objects.all():
        has_attr = False
        product = None
        attributes = None
        try:
            product = Product.objects.filter(sku=attribute.sku).get()
            has_attr = True
            attributes = Attribute.objects.filter(product=product).all()
        except:
            pass
        
        if has_attr and len(attributes) == 0:
            product.delete()
            products_deleted += 1
        

    print products_deleted