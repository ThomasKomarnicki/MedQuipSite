import urllib2
from bs4 import BeautifulSoup  
import json

prev_url = ""

def SearchCategory(url):
    global prev_url
    equals_prev = False
    if(url[:-2] ==  prev_url[:-2]):
        equals_prev = True
    prev_url = url
    
    print "fetching from "+url
    usock = urllib2.urlopen(url)
    data = usock.read()
    usock.close()
    soup = BeautifulSoup(data)
    list = soup.find('ol')
#     print list
    if(list and not list.has_attr('class') and not equals_prev):
        list = list.find_all('a')
        for item in list:
#             print item
            if(item):
#                 soup1 = BeautifulSoup(item)
                sub_category_url = item['href']
                SearchCategory(sub_category_url)
    
    index = data.find('category/')
    subString = data[index:index+15]
    numberString = ''
    for c in subString:
        if(c.isdigit()):
            numberString = numberString + c;
    split_string = soup.find('title').string.split('|')[0].split(' - ')[0]
#     url.split('/')
    print 'getting category id from '+url
    print numberString
    
    if( not numberString):
        print 'numberString fail'
        unordered = soup.find("ul",class_="breadcrumbs")
        
        list_items = unordered.find_all('li')
        li = list_items[len(list_items)-1]
        clss = li['class']
        subString = str(clss)
       
        for c in subString:
            if(c.isdigit()):
                numberString = numberString + c;
        print numberString        
        
    category_name = split_string
    print 'category name = '+category_name
#     split_string[len(split_string)-1].split('.')[0]
    category_name.replace('-','')
    for c in category_name:
        if(c.isdigit()):
            category_name.replace(c,"")
            
    category_ids[numberString] = category_name
    
    
    
if __name__ == '__main__':
    
    url = 'http://www.medicalquip.com'

#get category list
categories = []
category_ids = {}


usock = urllib2.urlopen(url)
data = usock.read()
usock.close()

soup = BeautifulSoup(data)
tag = soup.find('ul', id="nav_vert")
links = tag.find_all('a')

for a in links:
    val = a['href']
    val = val.partition('?SID')
    
    categories.append(val[0]+'?limit=all')
    
for category in categories:
    SearchCategory(category)
    
file = open('categories.json','w')
file.write(str(category_ids))
file.close()
print 'wrote to file'
   
   
    
# file = open('2013 products 1','r')
# soup = BeautifulSoup(file)
# table = soup.find('Table')
# row_list = table.find_all('Row')
# #   sku | name | description | stock | price | categories | status | visibility | short description | category names  
# 
# 
# 
# 
# 
# file = open('mqProducts.xml','w')  
