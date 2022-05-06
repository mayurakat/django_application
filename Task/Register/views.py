import email
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import  authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from .models import User


# Create your views here.
def home(request):
   
    return render(request,"home.html")


def register(request):

    if request.method == 'POST':

        first_name = request.POST['first_name']
        mobile = request.POST['mobile']
        email= request.POST['email']
        DOB = request.POST['dob']
        password1= request.POST['password1']
        password2= request.POST['password2']

        if password1 == password2:

            if User.objects.filter(mobile = mobile).exists():
                messages.info(request, "mobile taken")
                return redirect('register')
                
            elif User.objects.filter(email = email).exists():
                messages.info(request,"email taken")
                return redirect('register')

            else:
                user = User.objects.create_user( mobile=mobile, email= email, DOB=DOB ,password = password1, name = first_name )
                print("user Created")
                messages.info(request, "user Created")
                return redirect('login')
        else:
            messages.info(request,"password not match")
            return redirect('register')

    else:
        return render(request, 'register.html')
def login(request):


    if request.method == 'POST':


        email = request.POST.get('email')
        password = request.POST.get('password')        

        user = authenticate(request,email=email,password=password)

        if user:
                
                auth_login(request,user)
                messages.info(request,'You are logged in')
                return redirect('home')
        else:

                messages.info(request,'invalid user and password')
                return redirect('login')
       
    else:

        return render(request,"login.html")

def logout(request):

    auth_logout(request)
    messages.info(request,'succesfully logout')
    return redirect(login)