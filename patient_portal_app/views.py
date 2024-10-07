from django.shortcuts import render

def home(req):
    return render(req, 'home.html', {}) # {} for passing python code/args to our page.

def login(req):
    return render(req, 'login.html', {})