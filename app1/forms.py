from django.db.models import fields
from django.forms import widgets
from .models import Customer
from django import forms
#from django we will get the default usercreation for for user registration we will use that default
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm,PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User 
from django.utils.translation import gettext, gettext_lazy as _# for login form
from django.contrib.auth import password_validation #for password change validation

#custor registration form gives username bydefault
class CustomerRegistrationForm(UserCreationForm):
    #to make the form look good and alignment proper use a bootstrap class form control and widgets
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))     ##here we have given a bootstrap class
    password2 = forms.CharField(label="Confirm Password(again)", widget=forms.PasswordInput(attrs={'class': 'form-cotrol'}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    #in two cases need to write a meta class one modelform,usercreationform
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {'email': 'Email'}
        #adding widgets to username 
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'})}

#we are gonna use a django default login authenticatonform for login django will take careof authentication
#we are validating the registered user the login data wont stored in db
class LoginForm(AuthenticationForm):
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
