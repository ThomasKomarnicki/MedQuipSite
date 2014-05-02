import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'MedQuipSite.settings'

from Products.models import Product, Category, Attribute
import json
from os import listdir
from os.path import isfile, join

def find_image(product_sku,onlyfiles):
    for file_name in onlyfiles:
        if(product_sku in file_name):
            print "Image for "+ str(product_sku) + " found at "+ str(file_name)
            return file_name
    return None

if __name__ == '__main__':
    path = "C:\Users\Thomas\MedquipSite\MedQuipSite\Products\static\Products\images"
    only_files = [ f for f in listdir(path) if isfile(join(path,f)) ]
    
    for product in Product.objects.all():
        image_name = find_image(product.sku,only_files)
        if(image_name):
            if(not product.img):
                print " found image for "+ str(product.sku)
                                
            product.img = image_name
            product.save()
    