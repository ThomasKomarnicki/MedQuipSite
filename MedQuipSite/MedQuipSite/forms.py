from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField()
    
class RegisterForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'registerInput'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'registerInput'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'registerInput'}))
    orginization = forms.CharField(widget=forms.TextInput(attrs={'class':'registerInput'}),required=False)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'registerInput'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'registerInput'}))

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'registerInput'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'registerInput'}))