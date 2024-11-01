from django.shortcuts import redirect, render  
from .models import User  
from .forms import registerForm
from django.contrib import messages

user_loggedIn = False

def login(req):
    global user_loggedIn
    if req.method == 'POST':
        print(req.POST['user_email'])
        print(req.POST['user_pw'])
        if User.objects.filter(user_email=req.POST['user_email'], user_pw=req.POST['user_pw']):
            user_loggedIn = True
            print("login success!!")
            return redirect('landing')
        else:
            messages.success(req, ('User or Password does not match. Please try again!'))
            return redirect('login')
    else:
        if not user_loggedIn:
            return render(req, 'login.html', {})
        else:
            return render(req, 'landing.html', {})

def register(req):
    if req.method == 'POST':
        new_user = registerForm(req.POST or None)
        if new_user.is_valid():
            if User.objects.filter(user_email=new_user['user_email'].value()):
                messages.success(req, ('User with this E-mail id already exists! Please sign in to continue.'))
                return redirect('login')
            elif req.POST['user_pw'] != req.POST['user_cnf_pw']:
                print('pw match error!')
                messages.success(req, ('Passwords do not match! Please try again.'))
                return redirect('register')
            else:
                new_user.save()
                print("saved success!!!")
                messages.success(req, ('User Saved successfully! Please continue to sign in.'))
                return redirect('login')
        else:
            print("error creating user!")
    else:
        return render(req, 'register.html', {})
    
def landing(req):
    global user_loggedIn
    if user_loggedIn == True:
        return render(req, 'landing.html', {})
    else:
        return redirect('login')

def logout(req):
    global user_loggedIn
    user_loggedIn = False
    if 'register' in req.META['HTTP_REFERER']:
        return register(req)
    else:
        return login(req)