from django.db import models
from Checkout.models import Address, CreditCard

class Customer(models.Model):
    first = models.CharField(max_length=200)
    last = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    orginization = models.CharField(max_length=200,blank=True)
    password = models.CharField(max_length=200)
    orders = models.CharField(max_length=1000,blank=True)
    reset = models.CharField(max_length=200,blank=True)
    reset_valid_through = models.CharField(max_length=200,blank=True)
    user_cookie = models.CharField(max_length=200,blank=True)
    customer_code = models.CharField(max_length=200,blank=True)
    
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.first + ' '+ self.last
    
    def get_addresses(self):
        try:
            addresses = [Address.objects.filter(customer=self).all()]
            list = []
            for address in addresses:
                list.append({address})
            return list
        except:
            return None
            
    def get_credit_cards(self):
        try:
            credit_cards = CreditCard.objects.filter(customer=self).all()
            list = []
            for cc in credit_cards:
                list.append({cc})
            return list
        except:
            return None
    
    
class Order(models.Model):
    item_skus = models.CharField(max_length=200)
    item_count = models.CharField(max_length=200)
    item_price = models.CharField(max_length=200)
    item_discount = models.CharField(max_length=200)
    tax_total = models.DecimalField(decimal_places = 2,max_digits=10)
    shipping = models.DecimalField(decimal_places = 2,max_digits=10)
    shipped_to = models.CharField(max_length=200)
    customer = models.ForeignKey(Customer)
    
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.id
    
    
    
class CustomerCode(models.Model):
    code = models.CharField(max_length=200)
    price_discount_percent = models.IntegerField()
    free_shipping = models.BooleanField(default=False)
    shipping_discount_precent = models.IntegerField()
    
    
    
