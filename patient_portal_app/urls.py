from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'), # to reference or create link to this page on another page, this 'name' reference is required.
    path('login/', views.login, name='login'),
]
