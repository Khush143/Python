from django.shortcuts import render,redirect
from .models import User

# Create your views here.

def index(request):
    return render(request,'index.html')

def signup(request):
    if request.method=='POST':

        try:
            user=User.object.get(email=request.POST['email'])
            msg="Email Is Already Registered"
            return render(request,'signup,html',{'msg':msg})
        except:
            if request.POST['password']==request.POST['cpassword']:
                name=request.POST['name']
                uname=request.POST['uname']
                email=request.POST['email']
                mobile=request.POST['mobile']
                password=request.POST['password']
                cpassword=request.POST['cpassword']
                gender=request.POST['gender']
            else:
                msg="Password & Confirm Password Does Not Matched"
                return render(request,'signup.html',{'msg':msg})
        if password == cpassword:
            user = User.objects.create(
                name=name,
                uname=uname,
                email=email,
                mobile=mobile,
                password=password,
                gender=gender,
            )
            msg="User SignUp Successfully"
            return render(request,'login.html',{'msg':msg})
        else:
            msg="Password & Confirm Pasword Does Not Matched"
            return render(request,'signup.html',{'msg':msg})

    else:
        return render(request,'signup.html')

def login(request):
    if request.method == 'POST':
        try:
            user=User.objects.get(email=request.POST['email'])
            if user.password==request.POST['password']:
                request.session['email']=user.email
                request.session['name']=user.name
                return render(request,'index.html')
            else:
                msg="Incorrect Password"
                return render(request,'login.html',{'msg':msg})
        except:
            msg="Emai Not Registered"
            return render(request,'login.html',{'msg':msg})

    else:           
        return render(request,'login.html')