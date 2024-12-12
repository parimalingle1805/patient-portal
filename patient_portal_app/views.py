from django.shortcuts import redirect, render  
from .models import User, Symptom, Appointments
from .forms import registerForm, symptomForm, appointmentForm
from django.contrib import messages
import datetime
from django.core.mail import send_mail


user_loggedIn = False
sc_appt = []
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
    global user_loggedIn, sc_appt
    if req.method == 'POST':
        # symptom = symptomForm(req.POST or None)
        # if symptom.is_valid():
        # symptoms = print(req.POST['user_symptoms'])
        # if ', ' in req.POST['user_symptoms']:
        #     symptoms = list(set(list(map(str, req.POST['user_symptoms'].split(', ')))))
        # else:
        symptoms = list(set(list(map(str, req.POST['user_symptoms'].split(',')))))
        print(symptoms)
        pres = []
        for s in symptoms:
            if s[0] == ' ':
                s = s[1:]
            if not Symptom.objects.filter(symptoms_list=s):
                messages.success(req, ('System cannot find prescription for given symptoms. Please book an appointment with a doctor.'))
                return redirect('landing')
            else:
                r = Symptom.objects.get(symptoms_list=s)   
                pres.append({'symp': s, 'pr': r.prescription, 'sugg': r.suggestions})
                # print(r)
                # print(r.prescription)
                # print(r.suggestions)
        print(pres)
        return render(req, 'prescription.html', {'pres': pres})
        # prescription(req, pres)
    else:
        if user_loggedIn == True:
            return render(req, 'landing.html', {'sc_appt': Appointments.objects.values_list('user_appointment', flat=True)})
        else:
            return redirect('login')

def logout(req):
    global user_loggedIn
    user_loggedIn = False
    if 'register' in req.META['HTTP_REFERER']:
        return register(req)
    else:
        return login(req)
    
def appointment(req):
    global sc_appt
    curr_date = datetime.datetime.today().strftime('%Y-%m-%d')
    if req.method == 'POST':
        print(req.POST['app_date'])
        dt, t = map(str, req.POST['app_date'].split('T'))
        t_12 = datetime.datetime.strptime(t, '%H:%M')
        t_12 = t_12.strftime('%I:%M %p')
        if dt <= curr_date or '00:00' < t < '07:00':
            messages.success(req, 'Scheduled appointments are fully booked and not available for this date/time . Please select another date.')
            messages.success(req, 'Note: Scheduled appointments are not available today or past dates, 7:00AM to 12:00AM. So, please select a future date only with correct time!')
        else:
            messages.success(req, f'Your appointmant has been booked successfully for {dt} at {t_12}. You will receive a confirmation shortly.')
            Appointments.objects.create(user_appointment = f'{dt} : {t_12}')
            sc_appt.append(f'{dt} : {t_12}')
        return redirect('appointment')
    else:
        return render(req, 'appointment.html', {'dt':curr_date + 'T07:00'})