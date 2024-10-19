from django.shortcuts import render  
from .models import User  
from .forms import registerForm

def login(req):
    welcome_text = "Welcome to Patient Portal."
    return render(req, 'login.html', {'welcome_text': welcome_text}) # {} for passing python code/args to our page.

def register(req):
    return render(req, 'register.html', {})