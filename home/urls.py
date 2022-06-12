from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("contact", views.contact, name='contact'),
    path("other", views.other, name='other'),
    path("college", views.college, name='college'),
    path("course", views.course, name='course'),
    path("company", views.company, name='company'),
    path("updates", views.updates, name='updates'),
    path("jobrary", views.jobrary, name='jobrary'),
    
] 
