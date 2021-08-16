from rest_framework import serializers
from django.db.models import fields
from app1.models import Customer, Product, Cart, OrderPlaced
from django.contrib.auth.models import User
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['user','name','locality','city','zipcode','state']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title','selling_price','discounted_price','description','brand','category','product_image']

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['user','product','quantity']

class OrderPlacedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['user','customer','product','quantity','ordered_date','status']

#authentication-- login, registration

class CustomerRegistrationFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {'email': 'Email'}

#we are gonna use a django default login authenticatonform for login django will take careof authentication
#we are validating the registered user the login data wont stored in db
class LoginFormSerializer():
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(label=_("password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'form-control'}))


#using default django-passwordchageform making our own form to add the bootstrap class bcoz default wont allow bootstrap class so
class MyPasswordChangeForm(PasswordChangeForm): #everything all element will get default onluy bootstrap class form-control added 
    old_password = forms.CharField(label=_("old Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus': True, 'class': 'form-control'}))
    new_password1 = forms.CharField(label=_("New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'New-password', 'autofocus': True, 'class': 'form-control'}), help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("Confirm New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'New-password', 'autofocus': True, 'class': 'form-control'}))

#now to reset the form inherit rhe default and create the one to use bootstrap-class import passwordresertform
#no need to save tje data just we will gethe email write the functionaliy into email that send the link in email to reset the pass
class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label=_("Email"), max_length=254, widget=forms.EmailInput(attrs={'autocomplete': 'email', 'class': 'form-control'}))


class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label=_("New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'New-password', 'autofocus': True, 'class': 'form-control'}), help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("Confirm New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'New-password', 'autofocus': True, 'class': 'form-control'}))


#now create the modelform for profile address to save in db
class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'locality','city','zipcode','state']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'zipcode':forms.NumberInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-control'}),
        }