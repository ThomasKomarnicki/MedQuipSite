from Products.models import Product, Category, Attribute
import json


def add_parent_ids(category,category_list):
    if(category.parent_id):
        parent_category = Category.objects.filter(id=category.parent_id).get()
        category_list.append(parent_category)
        add_parent_ids(parent_category,category_list)
    
def get_category_links(product=None, category=None):
    if(product):
        category = Category.objects.filter(id=product.category_id).get()
    
    print category.name
        
    category_list = []
    category_list.append(category)
    add_parent_ids(category,category_list)
    category_list.reverse()
    return category_list    
    
        
def add_sub_category(category):
#     print "adding sub category for " + str(category)
    if(category.children_ids):
        category.sub_categories = []
        for id in json.loads(category.children_ids):
#             print "category "+str(category) + "has child category id "+str(id)
            sub_id = int(id)
            sub_category1 = Category.objects.filter(id=sub_id).get()
            category.sub_categories.append(sub_category1)
            
        if(hasattr(category,'sub_categories')):
    #         print str(category) + " has attribute - sub_categories"
            for sub_category in category.sub_categories:
                add_sub_category(sub_category)
    else:
        category.sub_categories = None

def get_categories(category_id=None):
    category_tree = []
    if(category_id):
        category = Category.objects.all().filter(id=category_id).get()
#         print "getting categories for " + str(category)
        id_list = []
        if(category.children_ids):
#             print "category has child categories"
            for id in json.loads(category.children_ids):
                int_id = int(id)
                id_list.append(int_id)
                
            categories = Category.objects.filter(pk__in=id_list).iterator() #i think this works?
            for category in categories:
                category_tree.append(category)
    else:
        categories = Category.objects.all()
        for category in categories:
            if( not category.parent_id):
#                 print category
                category_tree.append(category)
    
    category_tree.sort(key=lambda x: x.name, reverse=False)  
    for category in category_tree:
#         print "calling add sub category from main func"
        add_sub_category(category)
    
    return category_tree


def get_products_in_category(category,categories=None):
    if(not categories):
        categories = get_categories(category_id=category.id)
    all_products = []
    add_products(category,all_products)
#     have single list of all products, need to make list of rows of products
    print "AFTER ACCUMULATING ALL PRODUCTS IN CATEGORIES"
    print len(all_products)
#     product_list = []
#     i = 0
#     temp_list = []
#     for product in all_products:
#         if(i != 3):
#             temp_list.append(product)
#             i+=1
#         else:
#             product_list.append(temp_list)
#             i = 0
#             temp_list = []
#             
#     if(temp_list):
#         product_list.append(temp_list)
    
    return get_products_in_rows_of_three(all_products)

def get_products_in_rows_of_three(all_products):
    product_list = []
    i = 0
    temp_list = []
    for product in all_products:
        if(i != 3):
            temp_list.append(product)
            i+=1
        else:
            product_list.append(temp_list)
            i = 0
            temp_list = []
            
    if(temp_list):
        product_list.append(temp_list)
    
    return product_list
    
    
    
def add_products(category,all_products):
    try:
        products_in_category = Product.objects.filter(category_id=category.id).all()
    except:
        print "getting products failed for " + str(category)
        return
        
    for product in products_in_category:
        all_products.append(product)
    children_ids = category.children_ids
    if(children_ids):
        children_ids = json.loads(children_ids)
        for id in children_ids:
            add_products(Category.objects.filter(id=int(id)).get(),all_products)
    
 
def get_home_products():
    products = []
    temp = Product.objects.all()[:4]
    
    for product in temp:
        products.append(product)
    
    return products

def add_product_to_recent(request,product):
    recent_products = None
    if('recent' in request.session):
        recent_products = json.loads(request.session['recent'])
    else:
        recent_products = []
    
    recent_products.append({'sku':product.sku,'name':product.name})
    if(len(recent_products)> 5):
        recent_products.pop()
    request.session['recent'] = json.dumps(recent_products)
    
def get_recent_products(request):
    if('recent' in request.session):
        return json.loads(request.session['recent'])
    else:
        print "NO RECENT PRODUCTS"
        return None;
      
def get_cart_item_count(request):
    if('cart' in request.session):
        return len(json.loads(request.session['cart']))
    else:
        return 0    

def is_logged_in(request):
    return 'user' in request.session

def get_nav_header_items(request):
    return{'logged_in':is_logged_in(request),'cart_item_count':get_cart_item_count(request)}

def get_2_plus_column_base_data(request):
    return(dict(get_nav_header_items(request).items() + {'recent':get_recent_products(request)}.items()))

def search(query):
    products = Product.objects.filter(name__icontains=query).all()
    return get_products_in_rows_of_three(products)
    