from django.shortcuts import render, HttpResponse
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, "about.html")
def contact(request):
    if request.method == "POST":
        Name = request.POST.get('Name')
        Phone = request.POST.get('Phone')
        Email = request.POST.get('Email')
        contact = Contact(Name=Name, Email=Email, Phone=Phone)
        contact.save()
        messages.success(request, 'Your profile details updated!')
    return render(request, "contact.html")
def other(request):
    return render(request, "other.html")
def college(request):
    return render(request, "college.html")
def course(request):
    return render(request, "course.html")    
def company(request):
    return render(request, "company.html")

   

