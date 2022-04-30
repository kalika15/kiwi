from django.contrib import admin
from django.urls import path
from home import views 

urlpatterns = [
    path("",views.index, name='home'),
    path("services",views.services,name='services'),
    path("contact",views.contact,name='contact'),
    path("menwear",views.menwear,name='menwear'),
    path("kidswear",views.kidswear,name='kidswear'),
]