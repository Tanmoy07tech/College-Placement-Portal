from django.core.checks import messages
from django.http.response import HttpResponse
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
        college_id=request.POST.get('collegeid')
        
        password_log=request.POST.get('password')
        
        for member in all_students:
            
            if college_id==member.college_id and password_log==member.password:    
                print('succesfully logged')
                
                return HttpResponse('Loggin Successfull')
            elif college_id==member.college_id and password_log!=member.password:    
                messages.error(request,'Invalid Password')

                return render(request,'login.html')
            else:
                messages.error(request,'No registered College Id found please register first')

                return render(request,'login.html')   
    return render(request,'login.html')
            
   
    

def register(request):
    if request.method=='POST':
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        email=request.POST.get('email')
        collegeid=request.POST.get('collegeid')
        password=request.POST.get('password')
        s1=Student(first_name=firstname,last_name=lastname,college_id=collegeid,email=email,password=password)
        s1.save()  
        print('Created a account')
        messages.success(request,'Succesfully created an account.Please Login')
        
        return render(request,'login.html')
         
    
    return render(request,'register.html')



