from django import forms
from.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

     
class Eform(forms.ModelForm):
     class Meta:
          model=Updates
          fields='__all__'




class Regform(UserCreationForm):
     username=forms.CharField(widget=forms.TextInput(
          attrs={
               'placeholder':'Enter Username',
               'class':'flow-label',
          }
     ))

     email=forms.EmailField(widget=forms.EmailInput(
          attrs={
               'placeholder':'Enter Email Address',
          }
     ))

     first_name=forms.CharField(widget=forms.TextInput(
          attrs={
               'placeholder':'Enter firstname',
          }
     ))

     last_name=forms.CharField(widget=forms.TextInput(
          attrs={
               'placeholder':'Enter second name',
          }
     ))

     password1=forms.CharField(widget=forms.PasswordInput(
          attrs={
               'placeholder':'Enter Password',
          }
     ))

     password2=forms.CharField(widget=forms.PasswordInput(
          attrs={
               'placeholder':'Enter Password Again', 
          }
     ))


     class Meta:
          model=User
          fields=['username','first_name','last_name','email']     


class Form(forms.Form):
     busname=forms.CharField(max_length=50)
     route=forms.CharField(max_length=100)
     update=forms.CharField(max_length=200)


class Uproform(forms.ModelForm):
     class meta:
          model=Updates
          fields=['busname','update']


class upform(UserCreationForm):
     busname=forms.CharField(widget=forms.TextInput(
          attrs={
               'placeholder':'Enter Username',
               'class':'flow-label',
          }
     ))

     busno=forms.EmailField(widget=forms.EmailInput(
          attrs={
               'placeholder':'Enter Email Address',
          }
     ))

     update=forms.CharField(widget=forms.TextInput(
          attrs={
               'placeholder':'Enter firstname',
          }
     ))


     class Meta:
          model=Updates
          fields='__all__'    

