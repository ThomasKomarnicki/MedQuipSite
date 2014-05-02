import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'MedQuipSite.settings'

from Products.models import Product
from bs4 import BeautifulSoup

if __name__ == '__main__':
    soup = BeautifulSoup(open('products_with_weights.xml','r'))
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
            
            weight = int(row.findAll("data")[2].string)
            if(weight):
                product.weight = weight
                product.save()
