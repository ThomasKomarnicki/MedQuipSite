from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    children_ids = models.CharField(max_length=200,null=True,blank=True)
    parent_id = models.IntegerField(null=True,blank=True)
    
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name +"(" + str(self.id) +")"
    
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places = 2,max_digits=10)
    sku = models.CharField(max_length=20)
    img = models.CharField(max_length=200)
    description = models.CharField(max_length=4000)
    short_description = models.CharField(max_length=200,null=True,blank=True)
    category_id = models.IntegerField()
    attribute_type = models.IntegerField()
#     0 = no attributes, 1 = simple attributes, 2= long attributes
    
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name
    
    
class Attribute(models.Model):
    product = models.ForeignKey(Product)
    name = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places = 2,max_digits=10)
    sku = models.CharField(max_length=20)
    description = models.CharField(max_length=4000,blank=True)
    short_description = models.CharField(max_length=200,blank=True)
    
    
    def __unicode__(self): 
        return self.name + " - " + str(self.price)
    
    def __init__(self,**kwargs):
        if ('attribute_map' in kwargs):
            print "found attribute map"
            attribute_map = kwargs['attribute_map']
            self.product = attribute_map['product']
            self.name = attribute_map['name']
            self.price = attribute_map['price']
            self.sku = attribute_map['sku']
            self.description = attribute_map['description']
            self.short_description = attribute_map['short_description']
