import json
from bs4 import BeautifulSoup 

if __name__ == '__main__':
    
    products_xml = open('2013 Products 4.xml','r')
products_json = open('mqProducts.json','w')
s = open('categories.json').read()
categories_json = json.loads(s)

soup = BeautifulSoup(products_xml)
table = soup.find('table')
row_list = table.find_all('row')
#   sku | name | description | price | categories | status | visibility | short description 


product_array = {}

for row in row_list:
    data_array = row.find_all('data')
    sku = data_array[0].string
    temp_map = {'sku':sku}
    temp_map['name'] = data_array[1].string
    temp_map['description'] = data_array[2].string
    if(data_array[3].string):
        temp_map['price'] = float(data_array[3].string)
    else:
#         print 'price invalid, name = '+temp_map['name']
        temp_map['price'] = 0
    temp_map['short_description'] = data_array[7].string
    categories = data_array[4].string
    if(categories):
        category_nums = categories.split(',')
        num_array = []
        category_names = []
        for num in category_nums:
            num_array.append(int(num))
        for num in num_array:
            if(str(num) in categories_json):
                category_names.append(categories_json[str(num)].strip())
            else:
                category_names.append('unknown' + str(num))
        temp_map['categories'] = category_names
#         if(len(num_array) > 3):
#             print temp_map['name']
    product_array[sku] = temp_map;
        
    




products_json.write(json.dumps(product_array,indent=4,sort_keys=False))
products_json.close()
products_xml.close()