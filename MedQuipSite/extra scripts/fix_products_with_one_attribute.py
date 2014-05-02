import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'MedQuipSite.settings'

from Products.models import Product, Category, Attribute
import json

if __name__ == '__main__':
    for product in Product.objects.all():
        try:
            attributes = Attribute.objects.filter(product=product).all()
            
            if(len(attributes) == 1):
                product.attribute_type = 0
                attribute = attributes[0]
                product.price = attribute.price
                product.description = attribute.description
                product.short_description = attribute.short_description
                product.sku = attribute.sku
                product.save()
                attribute.delete()
                
        except:
            #no attributes
            product.attribute_type = 0
        product.save()
            