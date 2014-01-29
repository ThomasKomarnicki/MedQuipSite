import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'MedQuipSite.settings'

from Products.models import Product, Category, Attribute
from bs4 import BeautifulSoup
import decimal, sys, codecs
import json

def find_category_by_name(category_name, parent_category_name):
    try:
        category = Category.objects.filter(name=category_name).get()
        return category.id
    except:
#         print "could not find category " + category_name
        pass
    
    created_category = create_category(category_name,parent_category_name)   
    if created_category:
        return created_category.id
    
    return -1;

def create_category(category_name, parent_category_name):
    try:
        parent_category = Category.objects.filter(name=parent_category_name).get()
        category = Category(name=category_name,parent_id=parent_category.id)
        category.save()
        children_ids = json.loads(parent_category.children_ids)
        children_ids.append(category.id)
        parent_category.children_ids = json.dumps(children_ids)
        parent_category.save()
#         print "created category " + category_name.encode("ascii","ignore")
        return category
    except:
#         print " couldn't find parent category "+ parent_category_name
        return None
    
def names_are_equal(name, name1):
    if(len(name) != len(name1)):
#         print "name legnths aren't equal"
#         print len(name)
#         print len(name1)
        return False
    
    for i,char in enumerate(name):
        if(name[i] != name1[i]):
#             print i
#             print name[i]
#             print name1[i]
            return False
    return True
    
def get_price(datas):
    # 26 is price
    # 27 is future
    price = None
#     print datas[25].string 
#     print datas[26].string 
#     print datas[15].string 
#     print datas[16].string 
    if(valid_price(str(datas[25].string))):
        price = str(datas[25].string)
    if(valid_price(str(datas[26].string))):
        price = str(datas[26].string)
    if(valid_price(str(datas[15].string))):
        price = str(datas[15].string)
    if(valid_price(str(datas[16].string))):
        price = str(datas[16].string)
    
    if not price:
#         print "no prices for " + str(datas[1].string[1:])
        return 0
    price = decimal.Decimal(price)
    return price

def valid_price(price):
    for character in price:
        if not character.isdigit() and character != '.':
            return False
    return True


if __name__ == '__main__':
    categories_not_found = []
    products_2014 = BeautifulSoup(open("xml_datas.xml",'r').read())
    
    products_not_added = []
    
    
    
    rows = products_2014.findAll("row")
#     print rows[1]
#     sys.exit(0)
    row_offset = -1
    for i,row in enumerate(rows[1:],start=1):
        if row_offset < i:
            datas = row.findAll("data")
            sku = datas[1].string[1:]
            name = datas[3].string
            description_box = datas[4].string
            attribute_description = datas[5].string
            product_sub = datas[6].string
            bullet_points = datas[7].string
            img = datas[8].string
            product_category = datas[10].string
            product_category_parent = datas[9].string
            photo_caption = datas[11].string
            
            product = None
            try:
                product = Product.objects.filter(sku=sku).get()
                    
            except:
                product = Product(sku=sku)
                product.category_id = find_category_by_name(product_category,product_category_parent)
                if(product.category_id >= 0):
                    pass
                else:
                    categories_not_found.append(product.sku)
                product.img = img
                product.weight = 5
            
            #            accumulate all products with same name
            similar_rows = []
            similar_rows.append(datas)
            row_offset = i
            for row1 in rows[i+1:]:
                datas1 = row1.findAll("data")
                
                if(names_are_equal(name,datas1[3].string)):
                    similar_rows.append(datas1)
                    row_offset = row_offset +1
                else:
                    break
            row_offset = row_offset +1
                    
            product.name = name.encode('ascii', 'ignore')
            product.attribute_options = description_box
            if len(similar_rows) > 1:
                product.attribute_type = 2
            else:
                product.attribute_type = 1
            product.visible = True
            
            price = get_price(datas)
            null_price = False
            if(price != 0):
                product.price = price
            if(not product.price):
                product.price = 0;
#                 print "product "+str(product.sku) + " price is null"
                null_price = True
            
            
            if not null_price:
                product.save()
            else:
                products_not_added.append(product.sku)
#             has_valid_prices = True
#             attributes = []
    #         print "saved " + str(product)
#             print "saved product "+ str(product.sku)
            
                
            for datas in similar_rows:
                if(not null_price):
                    attribute = Attribute(product=product)
                    attribute.name = datas[3].string.encode('ascii', 'ignore') 
                    attribute.price = decimal.Decimal(get_price(datas))
                    if attribute.price == 0:
                        try:
                            p = Product.objects.filter(sku=datas[1].string[1:]).get()
                            attribute.price = p.price
                        except:
    #                         has_valid_prices = False
#                             print "attribute had no previous price, sku = " + datas[1].string[1:]
                            products_not_added.append(datas[1].string[1:])
                            null_price = True
                            
                    attribute.sku = datas[1].string[1:]
                    attribute.description = datas[5].string
                    attribute.short_description = datas[11].string
    #                 attributes.append(attribute)
                    if not null_price:
                        attribute.save()
                else:
                    products_not_added.append(datas[1].string[1:])
                    
            
#             if(has_valid_prices):
#                     product.save()
#                     for attribute in attributes:
#                         attribute.save()
#             else:
#                 products_not_added_skus.append(product.sku)
#                 for attribute in attributes:
#                     products_not_added_skus.append(attribute.sku)
                    
    not_added_products_file = open("not_added_products_files.json","w")
    not_added_products_file.write(json.dumps(products_not_added,indent=4))
    not_added_products_file.close()
    
    file = open("not_added_categories.json","w")
    file.write(json.dumps(categories_not_found,indent=4))
    file.close()
