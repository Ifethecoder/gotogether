# import the standard Django Forms 
# from built-in library 

from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
# creating a form 
class RegisterUserForm(UserCreationForm):
    minerva_email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ["username", "minerva_email", "password1", "password2"]

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["minerva_email","current_location", "going_to", "by_this_date_and_time"]