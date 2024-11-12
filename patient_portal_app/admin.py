from django.contrib import admin
from .models import User, Symptom,Appointments

# Register your models here.

admin.site.register(User)
admin.site.register(Symptom)
admin.site.register(Appointments)
