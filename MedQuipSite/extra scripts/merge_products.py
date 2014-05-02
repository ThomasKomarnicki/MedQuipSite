import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'MedQuipSite.settings'

from Products.models import Product, Category,Attribute
import re

def product_name_matches(product1, product2, product1_name, product2_name, pattern_id,match_count):
    if( product1.category_id != product2.category_id):
        return False
    
    if(pattern_id == 0):
        return product1_name == product2_name
    if(pattern_id == 1):
        i = 0
        while(i<match_count):
            i+=1
            if(product1_name[i] != product2_name[i]):
                return False
    return True
        
        
# def create_product_name(product, pattern_id, match_count):
#     
#     val = product.name
#     if(pattern_id == 1):
#         split = re.split(",|;",product.name)
#         val = ""
#         i = 0
#         while(i < match_count):
#             val += split[i]
#             i += 1
#     
#     return val
    
def get_attribute_titles(similar_products):
    attribute_titles = []
    print "========= NEW PRODUCT =========="
    for product in similar_products.reverse():
        print "NAME = "+product.name
        print "DESCRIPTION = "+product.description
        print "SHORT = "+product.short_description

    first_product = similar_products[0]    
    first_attribute = raw_input("Attribute title for above product")
    
    attribute_titles.append(first_attribute)
    
    sections = first_attribute.split(';')
    section_res = []
    for section in sections:
        # RE that matches word before word in section
        word_before_section_re = ""
        section_re = 
    
    
    
    return attribute_titles
        
     
        
def make_product_group(similar_products):
    product_group = {}
    product_group['sku'] = similar_products[0].sku
    product_group['short_description'] = similar_products[0].short_description
    product_group['description'] = similar_products[0].description
    product_group['price'] = similar_products[0].price
    attributes = []
    attribute_titles = get_attribute_titles(similar_products)
    for i,product in enumerate(similar_products,start=1):
        attribute = {}
        attribute['name'] = attribute_titles[i]
        attribute['sku'] = product.sku
        attribute['short_description'] = product.short_description
        attribute['description'] = product.description
        attribute['price'] = product.price
        attributes.append(attribute)
    
    product_group['name'] = similar_products[0].name
    
    # save to database
    
    for product in similar_products:
        product.delete()
    
    head_product = similar_products[0]  
    head_product.save()
#   save attributes  
    for attribute_map in attributes:
        attribute = Attribute(attribute_map)
        attribute.save()
        
    
    return product_group
        

# def get_match_count(product_splits,all_products):
#     match_count = 0
#     for product in all_products:
#         splits = re.split(",|;",product.name)
#         for idx, split in enumerate(splits):
#             if(product_splits[idx] != split):
#                 if(idx > match_count):
#                     match_count = idx
#                 break
#     return match_count  
    
    
if __name__ == '__main__':
    global name_pattern

all_products = Product.objects.all()
    
grouped_products = []

similar_products = []

#products with matching name
for i, product in enumerate(all_products):
    product_name = product.name
    
    for j, product1 in enumerate(all_products):
        if(product1.name == product_name and j != i and product.category_id == product1.category_id):
            similar_products.append(product1)
            
    if(similar_products):
        similar_products.insert(0, product)
        grouped_products.append(make_product_group(similar_products,0,0))
        similar_products = []

# products with different names that have attributes after , or ;
# for i, product in enumerate(all_products):
#     product_splits = re.split(",|;", product.name)
#     
#     match_count = get_match_count(product_splits,all_products)
#     
#     for j, product1 in enumerate(all_products):
#         product1_splits = re.split(",|;",product1.name)
#         if(product_name_matches(product, product1, product_splits, product1_splits, 1, match_count)):
#             similar_products.append(product1)
#             
#     if(similar_products):
#         similar_products.insert(0, product)
#         grouped_products.append(make_product_group(similar_products,0,get_match_count(product_splits,all_products)))
#         similar_products = []
            