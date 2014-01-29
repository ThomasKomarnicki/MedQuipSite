import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'MedQuipSite.settings'

from Products.models import Product, Category, Attribute
import json
import sys

if __name__ == '__main__':
    while True:
        category_name = raw_input("Category to move: ")
        destination_parent = raw_input("Move to: ")
         
        try:
            category = Category.objects.filter(name=category_name).get()
            category_parent = Category.objects.filter(name=destination_parent).get()
        except Exception as e:
            print "FAILED2"
            print e
             
        category.parent_id = category_parent.id
        if category_parent.children_ids:
            parent_children_ids = json.loads(category_parent.children_ids)
        else:
            parent_children_ids = []
        parent_children_ids.append(int(category.id))
        category.save()
        category_parent.children_ids = json.dumps(parent_children_ids)
        category_parent.save()
