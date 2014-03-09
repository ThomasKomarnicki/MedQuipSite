from models import Address,Checkout,CreditCard
from MedQuipSite.forms import BillingForm,ContactForm,ShippingForm,CreditCardForm
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import Products.view_data as view_data

def checkout(request):
    
    if not view_data.is_logged_in(request):
        response = HttpResponseRedirect("/Login/")
        response.set_signed_cookie("redirect", "/Cart/Checkout/", salt="dog")
        return response
        
    billing_form = None
    shipping_form = None
    cc_form = None
    
    if request.method == 'POST':
        billing_form = BillingForm(request.POST)
        shipping_form = ShippingForm(request.POST)
        cc_form = CreditCardForm(request.POST)
        
        if billing_forms_are_valid(request,billing_form,shipping_form,cc_form):
            checkout = None
            shipping = None
            cc = None
            if not shipping_to_billing_address(billing_form):
                shipping = shipping_form
            if paying_with_cc(request):
                cc = cc_form
            
            checkout(billing_form,cleaned_shipping=shipping,cleaned_cc=cc_form)
            checkout.save()
            request.session['checkout_id'] = checkout.id
            return HttpResponseRedirect('/Cart/Checkout/Shipping')
            
        
        
    else:
        billing_form = BillingForm()
        shipping_form = ShippingForm()
        cc_form = CreditCardForm()
    
            
    return render(request, 'checkout2.html', dict(view_data.get_2_plus_column_base_data(request).items() + {'billing_form':billing_form,"shipping_form":shipping_form,"cc_form":cc_form}.items()))

def paying_with_cc(request):
    return request.POST['payment_method'] == "Credit Card"

def shipping_to_billing_address(billing_form):
    return billing_form.cleaned_data['same']

def billing_forms_are_valid(request,billing_form,shipping_form,cc_form):
    if not billing_form.is_valid():
        return False
    
    if shipping_to_billing_address(billing_form):
        if not shipping_form.is_valid():
            return False
        
    if paying_with_cc(request):
        if not cc_form.is_valid():
            return False
    
    return True
    
    
def submit_billing(request):
    pass


def checkout_shipping(request):
    checkout = None
    if 'checkout_id' in request.session:
        try:
            checkout = Checkout.objects.filter(id=request.session['checkout_id']).get()
        except:
            del request.session['checkout_id']
            
            
    return render(request, 'checkout_shipping.html', dict(view_data.get_2_plus_column_base_data(request).items() + {}.items()))
        
    
