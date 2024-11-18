from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django import forms
class SignUp(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'id':'required','placeholder':'username'}))
    first_name=forms.CharField(widget=forms.TextInput(attrs={'id':'required','placeholder':'First Name'}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={'id':'required','placeholder':'Last Name'}))
    email=forms.CharField(widget=forms.EmailInput(attrs={'id':'required','placeholder':'email'}))
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']


class EditForm(UserChangeForm):
    first_name=forms.CharField(widget=forms.TextInput(attrs={'id':'required','placeholder':'First Name'}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={'id':'required','placeholder':'Last Name'}))
    password=None
    class Meta:
        model=User
        fields=['first_name','last_name','email']