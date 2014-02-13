from django import forms
from Customers.models import Customer
from django.core.exceptions import ValidationError
import hashlib
import selectors_data
from datetime import date

class ContactForm(forms.Form):
    subject = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField()
    
class RecoverForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'registerInput'}), error_messages = {'email_exist': 'There is no account associated with this Email'})
    
    def clean_email(self):
        email = self.cleaned_data['email']
        error = False
        try:
            Customer.objects.filter(email=email).get()
        except:
            error = True
        if error:    
            raise ValidationError(self.fields['email'].error_messages['email_exist'])
        return email
    
class PasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'registerInput'}),error_messages = {'too_short': 'Your Password must contain at least 6 characters'})
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'registerInput'}),error_messages = {'no_match': 'Your Passwords do not match'})
    
    def clean_password(self):
        password = self.cleaned_data['password']
        if(len(password) < 6):
            raise ValidationError(self.fields['password'].error_messages['too_short'])
        return password
    
    def clean_confirm_password(self):
        confirm_password = self.cleaned_data['confirm_password']
        if('password' in self.cleaned_data):
            password = self.cleaned_data['password']
            if(confirm_password != password):
                raise ValidationError(self.fields['confirm_password'].error_messages['no_match'])
        
        return confirm_password
    
class RegisterForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'registerInput'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'registerInput'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'registerInput'}), error_messages = {'email_taken': 'This Email Address is already in use'})
    orginization = forms.CharField(widget=forms.TextInput(attrs={'class':'registerInput'}),required=False)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'registerInput'}),error_messages = {'too_short': 'Your Password must contain at least 6 characters'})
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'registerInput'}),error_messages = {'no_match': 'Your Passwords do not match'})
    
    def clean_email(self):
        email = self.cleaned_data['email']
        print "REGISTER CLEAN EMAIL"
        customer_found = False
        try:
            customer = Customer.objects.filter(email=email).get()
            print "found customer with email "+ str(customer.email)
            customer_found = True
        except:
            print "REGISTER CLEAN EMAIL EXCEPTION"
            print "THEREFORE, EMAIL/USER DOESN'T EXIST"
        if customer_found:
            raise ValidationError(self.fields['email'].error_messages['email_taken'])
        return email
        
    def clean_password(self):
        password = self.cleaned_data['password']
        if(len(password) < 6):
            raise ValidationError(self.fields['password'].error_messages['too_short'])
        return password
    
    def clean_confirm_password(self):
        confirm_password = self.cleaned_data['confirm_password']
        if('password' in self.cleaned_data):
            password = self.cleaned_data['password']
            if(confirm_password != password):
                raise ValidationError(self.fields['confirm_password'].error_messages['no_match'])
        
        return confirm_password
        
        
class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'registerInput'}),error_messages = {'email_not_found': 'Email Address was not found'})
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'registerInput'}),error_messages = {'incorrect_password': 'Incorrect Email/Password'})
    
    def clean_email(self):
        print "CLEAN EMAIL"
        email = self.cleaned_data['email']
        print email
        error = False
        try:
            Customer.objects.filter(email=email).get()
        except:
            error = True
        if error:    
            raise ValidationError(self.fields['email'].error_messages['email_not_found'])
        return email
    
    def clean_password(self):
        print "CLEAN PASSWORD"
        password = self.cleaned_data['password']
        print password
        can_check = False
        try:
            customer = Customer.objects.filter(email=self.cleaned_data['email']).get()
            customer_password = customer.password
            input_password = hashlib.sha224(password).hexdigest()
            can_check = True
        except:
            print "CLEAN PASSWORD EXCEPTION"
            
        if(can_check and customer_password != input_password):
            raise ValidationError(self.fields['password'].error_messages['incorrect_password'])
        
        return password
    
    
    
class ShippingForm(forms.Form):
    first_name = forms.CharField(label="First Name")
    last_name = forms.CharField(label="Last Name")
    company = forms.CharField(required=False)
    email = forms.EmailField(label="Email Address")
    address = forms.CharField(label="Address")
    address_line2 = forms.CharField(required=False,label="")
    city = forms.CharField(label="City")
    state = forms.ChoiceField(label="State/Province",choices=selectors_data.get_states_as_selector_data())
    non_us_state = forms.CharField(label="State/Province")
    zip = forms.CharField(label="Zip Code")
    country = forms.ChoiceField(label="Country",choices=selectors_data.get_countries_as_selector_data())
    telephone = forms.CharField(label="Telephone")
    fax = forms.CharField(label="Fax")
    
    def __init__(self, *args, **kwargs):
        super(ShippingForm, self).__init__(*args, **kwargs)
        self.fields['state'].initial = 'Florida'
        self.fields['country'].initial = 'United States'
    
class BillingForm(ShippingForm):
    same = forms.BooleanField(widget=forms.CheckboxInput(attrs={"id":"same_as_billing"}))
    
    
class CreditCardForm(forms.Form):
    name = forms.CharField(label="Name on Card")
    number = forms.CharField(label="Number",error_messages = {'not_selected': 'Please enter a valid Credit Card Number'})
    cvc = forms.CharField(label="CVC",min_length=3,widget=forms.TextInput(attrs={'maxlength':'4'}))
    date_month = forms.DateField(label="Exp Date",widget=forms.DateInput(attrs={'maxlength':'2'}),input_formats=['%m'])
    date_year = forms.DateField(required=False,label="",widget=forms.DateInput(attrs={'maxlength':'2'}),input_formats=['%y'])
    type = forms.ChoiceField(choices = selectors_data.get_cc_types(),error_messages={'not_selected': 'Please select a credit card type'}) 
    
    def clean_type(self):
        type = self.cleaned_data['type']
        if type == "None":
            raise ValidationError(self.fields['type'].error_messages['not_selected'])
        return type
        
    def clean_number(self):
        number = self.cleaned_data['number']
        if not luhn(number):
            raise ValidationError(self.fields['number'].error_messages['invalid_number'])
        return number
        
    def clean_date_month(self):
        month = self.cleaned_data['date_month']
        year = self.cleaned_data['year']
        today_year = date.today().year
        today_month = date.today().month
    
    
def luhn(n):
    r = [int(ch) for ch in str(n)][::-1]
    return (sum(r[0::2]) + sum(sum(divmod(d*2,10)) for d in r[1::2])) % 10 == 0
  
    
    
    
    
    