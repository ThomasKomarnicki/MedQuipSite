import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'MedQuipSite.settings'

import json
from Products.models import Product, Category
from django.core.exceptions import ObjectDoesNotExist


if __name__ == '__main__':
    categories = Category.objects.all()
    
biodex = Category.objects.filter(id=98).get()
children_ids = []
for category in categories:
    if category.parent_id == 98:
        children_ids.append(category.id)

c_ids = json.dumps(children_ids)
print c_ids
biodex.children_ids = c_ids
biodex.save()

#     for category in categories:
#         children_ids = json.loads(category.children_ids)
#         for id in children_ids:
#             child_category = Category.objects.filter(id=id).get()
#             child_category_children = json.loads(child_category.children_ids)
#             if id in child_category_children



# file = open('categories_with_children.json','r')
# list = json.loads(file.read())
# 
# for item in list:
#     category = Category(id=item['id'],children_ids=item['children_ids'],parent_id=item['parent_id'],name=item['name'])
#     category.save()

# for category in categories:
#     if(category.children_ids):
#         children_ids = json.loads(category.children_ids)
#         if(category.id in children_ids):
#             children_ids.remove(category.id)
#             category.children_ids = json.dumps(children_ids)
#             category.save()
    
# for category in categories:
#     if(category.children_ids):
#         children_ids = category.children_ids.split(',')
#         children_ids_json = []
#         for id in children_ids:
#             children_ids_json.append(int(id))
#         category.children_ids = json.dumps(children_ids_json)
#         category.save()

#     for category in categories:
#         if(category.children_ids):
#             category.children_ids = category.children_ids[:-1]
#             category.save()
#             print category
                
#     for category in categories:
#         if(category.children_ids):
#             splits = category.children_ids.split(',')
#             for item in splits:
#                 try:
#                     child_category = Category.objects.get(id=int(item))
#                     child_category.parent_id = category.id
#                     child_category.save()
#                     print child_category
#                 except:
#                     pass
                    
                
#     for category in categories:
#         id_list = []
#         if(category.children_ids):
#             splits = category.children_ids.split(',')
#             for item in splits:
#                 if(item not in id_list and item != ""):
#                     id_list.append(item)
#             children_ids = ""
#             for id in id_list:
#                 children_ids += (id + ',')
#             category.children_ids = children_ids
#             category.save()
#             print category

# for product_key in products_json:
#     product = products_json[product_key]
#     prev_category = None
#     try:
#         product_categories = product['categories']
#         for category in product_categories:
#             c = Category.objects.get(name=category)
#  
#                  
#             if(prev_category and len(product['categories']) < 4):
#                 if(prev_category.children_ids):
#                     prev_category.children_ids += str(c.id) + ','
#                 else:
#                     prev_category.children_ids = str(c.id) + ','
#                 prev_category.save()
#                 print prev_category
#             prev_category = c
#     except:
# #         print "no categories for " + str(product['name'])
#         pass