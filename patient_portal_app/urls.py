from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'), # to reference or create link to this page on another page, this 'name' reference is required.
    # path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
]
