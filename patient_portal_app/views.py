from django.shortcuts import render

def home(req):
    welcome_text = "Welcome to Patient Portal."
    return render(req, 'home.html', {'welcome_text': welcome_text}) # {} for passing python code/args to our page.

def login(req):
    return render(req, 'login.html', {})

def register(req):
    return render(req, 'register.html', {})