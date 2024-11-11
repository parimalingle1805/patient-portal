from django import forms
from .models import User, Symptom

class registerForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["user_fname", "user_lname", "user_email", "user_phone", "user_pw", "user_loggedIn"]

class symptomForm(forms.ModelForm):
    class Meta:
        model = Symptom
        fields = ["symptoms_list", "prescription", "suggestions"]