from django.db import models
from Customers.models import Customer

class Checkout(models.Model):
    payment_type = models.CharField(max_length=200)
    shipping_cost = models.DecimalField(decimal_places = 2,max_digits=10,blank=True)
    shipping_method = models.CharField(max_length=200,blank=True)

    def __init__(self,cleaned_billing,cleaned_shipping = None,cleaned_cc=None):
        super.__init__(self)
        billing_address = Address(cleaned_address=cleaned_billing,checkout = self,type="billing")
        if cleaned_shipping:
            shipping_address = Address(cleaned_address=cleaned_shipping,checkout = self,type="shipping")
        else:
            shipping_address = Address(cleaned_address=cleaned_billing,checkout = self,type="shipping")
        
        if(cleaned_cc):
            self.payment_type = "Credit Card"
            cc_data = CreditCard(cleaned_cc=cleaned_cc,checkout = self)
        else:
            self.payment_type = "Money Order"
            
        billing_address.save()
        shipping_address.save()
        cc_data.save()
        
        
             
        
class Address(models.Model):

    type = models.CharField(max_length=200,blank=True,null=True)
    customer = models.ForeignKey(Customer)
    checkout = models.ForeignKey(Checkout,blank=True,null=True)
    first = models.CharField(max_length=200)
    last = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    orginization = models.CharField(max_length=200,blank=True)
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200,blank=True)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    zip = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    fax = models.CharField(max_length=200,blank=True)

    
    
    def __init__(self,cleaned_address=None,checkout = None,type1 = "billing", customer = None,*args, **kwargs):
        super(Address, self).__init__(*args, **kwargs)
        self.type = type1
        if cleaned_address:
            self.first = cleaned_address['first_name']
            self.last = cleaned_address['last_name']
            self.email = cleaned_address['email']
            self.orginization = cleaned_address['company']
            self.address1 = cleaned_address['address']
            self.address2 = cleaned_address['address_line2']
            self.city = cleaned_address['city']
            self.state = cleaned_address['state']
            self.country = cleaned_address['country']
            self.zip = cleaned_address['zip']
            self.phone = cleaned_address['telephone']
            self.fax = cleaned_address['fax']

        if(checkout):
            self.checkout = checkout
        if customer:
            self.customer = customer
            
    
    

class CreditCard(models.Model):
    customer = models.ForeignKey(Customer)
    checkout = models.ForeignKey(Checkout,null=True,blank=True)
    name = models.CharField(max_length=200)
    number = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    exp_date = models.CharField(max_length=200)
    cvc = models.CharField(max_length=200)
    
    def __init__(self,cleaned_cc=None,checkout = None, customer = None,*args, **kwargs):
        super(CreditCard, self).__init__(*args, **kwargs)
        if checkout:
            self.checkout = checkout
        if customer:
            self.customer = customer
        if cleaned_cc:
            self.name = cleaned_cc['name']
            self.number = cleaned_cc['number']
            self.type = cleaned_cc['type']
            self.exp_date = str(cleaned_cc['date_month'] + "/" + cleaned_cc['date_year'])
            self.cvc = cleaned_cc['cvc']
        
def get_addresses(customer):
    try:
        addresses = Address.objects.filter(customer=customer).all()
        list = []
        for address in addresses:
            list.append(dict(address));

        return list
    except:
        return None
             
def get_credit_cards(customer):
    try:
        credit_cards = CreditCard.objects.filter(customer=customer).all()
        list = []
        for cc in credit_cards:
            list.append(dict(cc))
        return list
    except:
        return None    
    
