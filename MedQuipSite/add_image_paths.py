import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'MedQuipSite.settings'

import json
from Products.models import Product, Category
from bs4 import BeautifulSoup

if __name__ == '__main__':
    soup = BeautifulSoup(open('products_images.xml','r'))
    rows = soup.findAll("row")
#     print rows[1]
#     datas = rows[1].findAll("data")
#     
#     for data in datas:
#         print data.string
    
    for row in rows:
        sku_data = row.find("data")
        if( str(sku_data.string).isdigit()):
            sku = int(sku_data.string)
            product = Product.objects.filter(sku=sku).get()
            
            img = row.findAll("data")[3].string
            if(not img):
                img = "0"+str(sku)+".jpg"
            product.img = img
            product.save()
        
