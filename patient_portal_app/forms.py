from django import forms
from .models import User

class registerForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["user_fname", "user_lname", "user_email", "user_phone", "user_pw", "user_loggedIn"]