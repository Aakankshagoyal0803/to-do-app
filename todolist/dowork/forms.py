from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django import forms

class regform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class doform(forms.ModelForm):
    class Meta:
        model=dothings
        fields=['title','due_date']
