from django.shortcuts import render
from MedQuipSite.forms import RegisterForm,LoginForm,RecoverForm,PasswordForm
from Customers.models import Customer
import hashlib
import Products.view_data as view_data
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail,EmailMultiAlternatives
import django.template.loader as loader

def register(request):
    if request.method == 'POST':
        print "SUBMITTED REGISTER FORM"
        loginForm = LoginForm()
        registerForm = RegisterForm(request.POST)
        if registerForm.is_valid():
            data = registerForm.cleaned_data
            customer = Customer(first=data['first_name'],last=data['last_name'],email=data['email'],password=hashlib.sha224(data['password']).hexdigest())
            customer.save()
            request.session['user'] = customer.email
            print "ABOUT TO REDIRECT TO /THANKS"
            return HttpResponseRedirect('/Thanks')
        else:
            return render(request,'register.html',dict(view_data.get_2_plus_column_base_data(request).items()+{'login':loginForm,'register':registerForm}.items()))
        
    else: #user loaded register view without having submitted the form
        loginForm = LoginForm()
        registerForm = RegisterForm()
        return render(request,'register.html',dict(view_data.get_2_plus_column_base_data(request).items()+{'login':loginForm,'register':registerForm}.items()))

def login(request):
    form = LoginForm(request.GET)
    if form.is_valid():
        request.session['user'] = form.cleaned_data['email']
        return HttpResponseRedirect('/')
    else:   
        registerForm = RegisterForm()
        return render(request,'register.html',dict(view_data.get_2_plus_column_base_data(request).items()+{'login':form,'register':registerForm}.items()))

def register_thanks(request):
    
    return render(request,'register_thanks.html',view_data.get_2_plus_column_base_data(request))

def sign_out(request):
    if('user' in request.session):
        del request.session['user']
        
    return render(request,'signed_out.html',view_data.get_2_plus_column_base_data(request))

def recover_password(request):
    if request.method == 'POST':
        recoverForm = RecoverForm(request.POST)
        if recoverForm.is_valid():
            # TODO send email to recoverFrom.cleaned_data['email'] with link to reset password containing reset_id
            email = recoverForm.cleaned_data['email']
            customer = Customer.objects.filter(email=email).get()
            customer.reset = hashlib.sha224(email).hexdigest()
            customer.save()
            
            subject, from_email = 'Medicalquip.com Password Reset', 'no-reply@medicalquip.com'
            text_content = 'This is an important message.'
            html_content = loader.render_to_string("reset_password.html", {'customer':customer,})
            msg = EmailMultiAlternatives(subject, text_content, from_email, [email])
            msg.attach_alternative(html_content, "text/html")
            msg.content_subtype = "text"
            msg.send()
            return HttpResponseRedirect('/RecoverPassword/PasswordReset/')
        else:
            return render(request,'recover_password.html',view_data.get_2_plus_column_base_data(request).items() + {'form':recoverForm}.items())
    
    else:
        recoverForm = RecoverForm()
        return render(request,'recover_password.html',dict(view_data.get_2_plus_column_base_data(request).items() + {'form':recoverForm}.items()))
    
def password_reset(request):
    
    return render(request,'password_reset.html',view_data.get_2_plus_column_base_data(request))

def make_new_password(request):
    if request.method == 'POST':
        passwordForm = PasswordForm(request.POST)
        if passwordForm.is_valid():
            
            # find email from reset_id and change that customer's password
            password = hashlib.sha224(passwordForm.cleaned_data['password']).hexdigest()
            HttpResponseRedirect('/PasswordChanged')
        else:
            return render(request,'make_new_password.html',view_data.get_2_plus_column_base_data(request).items() + {'form':passwordForm}.items())
    
    else:
        passwordForm = PasswordForm()
        return render(request,'make_new_password.html',view_data.get_2_plus_column_base_data(request).items() + {'form':passwordForm}.items())
    
def password_changed(request):
    
    return render(request,'password_changed.html',view_data.get_2_plus_column_base_data(request))
    

def my_account(request):
    
    
    return render(request,'')

def orders(request):
    
    
    return render(request,'')

def order(request,order_id):
    
    
    return render(request,'')
