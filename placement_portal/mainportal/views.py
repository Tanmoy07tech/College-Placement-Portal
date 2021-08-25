from django.core.checks import messages
from django.shortcuts import redirect, render
from mainportal.models import Student
from django.contrib import messages
# Create your views here.
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
def home(request):
   
    return render(request,'home.html')


def login(request):
    if request.method=='POST':
        all_students=Student.objects.all()
        email_log=request.POST.get('email')
        print(email_log)
        password_log=request.POST.get('password')
        for member in all_students:
            if email_log==member.email and password_log==member.password:    
                print('succesfully logged')
                return render(request,'succesfulled.html')
   
    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        email=request.POST.get('email')
        password=request.POST.get('password')
        s1=Student(first_name=firstname,last_name=lastname,email=email,password=password)
        s1.save()  
        print('Created a account')
        messages.success(request,'Succesfully created account')
        
        return render(request,'login.html')
         
    
    return render(request,'register.html')


def succesfulled(request):
    return render(request,'succesfulled.html')

