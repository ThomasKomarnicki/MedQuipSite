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
    
    found_count = 0
    has_images = []
    no_images = []
    for product in Product.objects.all():
        #find img with sku in file name
        image_name = find_image(product.sku,only_files)
        if(image_name):
            found_count += 1
            product.img = image_name
            product.save()
        else:
            no_images.append(product.sku)
    
    for attribute in Attribute.objects.all():
        image_name = find_image(attribute.sku,only_files)
        if(image_name):
            attribute.img = image_name
            attribute.save()
            
        
    print "found count = "+ str(found_count)
    print "total product count = "+ str(len(Product.objects.all()))    
    has_images_file = open("has_images.json","w")
    no_images_file = open("no_images.json","w")