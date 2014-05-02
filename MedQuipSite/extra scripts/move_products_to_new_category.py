import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'MedQuipSite.settings'

from Products.models import Product, Category, Attribute
import json

if __name__ == '__main__':
    while True:
        category_name = raw_input("Category to move: ")
        category = Category.objects.filter(name=category_name).get()
        
        destination_category = raw_input("Move Products to: ")
        destination_category = Category.objects.filter(name=destination_category).get()

            
        products = Product.objects.filter(category_id=category.id).all()
        for product in products:
            product.category_id = destination_category.id
            product.save()
        
        category.delete()
        
#         [351, 272, 383]
        
        