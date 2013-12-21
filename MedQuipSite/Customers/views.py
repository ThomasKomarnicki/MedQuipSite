from django.shortcuts import render
from MedQuipSite.forms import RegisterForm,LoginForm
from Customers.models import Customer
import hashlib
import Products.view_data as view_data
from django.http import HttpResponse, Http404, HttpResponseRedirect

# Create your views here.

def my_account(request):
    
    
    return render(request)

def register(request):
    if request.method == 'POST':
        print "SUBMITTED REGISTER FORM"
        loginForm = LoginForm()
        registerForm = RegisterForm(request.POST)
        valid = True
        if registerForm.is_valid():
            data = registerForm.cleaned_data
            print str(data['password'])
            print str(data['confirm_password'])
            if str(data['password']) != str(data['confirm_password']):
                registerForm['confirm_password'].errors.append("Passwords do not match")
                print "PASSWORDS DO NOT MATCH"
                valid = False
            if len(str(data['password'])) < 6:
                print "PASSWORDS TO SHORT"
                print len(str(data['password'])) 
                registerForm['password'].errors.append("Password must be atleast 6 characters")
                valid = False
        else:
            print "FORM NOT VALID"
            valid = False
            
        
        if not valid:
            print "NOT VALID, RETURNING TO REGISTER"
            return render(request,'register.html',dict(view_data.get_2_plus_column_base_data(request).items()+{'login':loginForm,'register':registerForm}.items()))
        else:
            # take form data and add new customer
            data = registerForm.cleaned_data
            customer = Customer(first=data['first_name'],last=data['last_name'],email=data['email'],password=hashlib.sha224(data['password']).hexdigest())
            customer.save()
            return HttpResponseRedirect(request,'Thanks')
        
    else: #user loaded register view without having submitted the form
        loginForm = LoginForm()
        registerForm = RegisterForm()
        return render(request,'register.html',dict(view_data.get_2_plus_column_base_data(request).items()+{'login':loginForm,'register':registerForm}.items()))

def login(request):
    form = LoginForm(request.GET)
    if form.is_valid():
        customer = Customer.objects.filter(email=request.GET['email']).get()
        input_password = hashlib.sha224(request.GET['password']).hexdigest()
        if(not customer):
            form.errors.append("Email Address not found")
        else:
            if customer.password == input_password:
                request.session['user'] = customer.email
                return HttpResponseRedirect(request,'')
            else:
                form.errors.append("Email / Password combination not found")
            
    registerForm = RegisterForm()
    return render(request,'register.html',dict(view_data.get_2_plus_column_base_data(request).items()+{'login':form,'register':registerForm}.items()))

def register_thanks(request):
    
    return render(request,'register_thanks.html',view_data.get_2_plus_column_base_data(request))
    

def orders(request):
    
    
    return render(request,'register.html')

def order(request,order_id):
    
    
    return render(request,'register.html')
