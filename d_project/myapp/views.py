from django.shortcuts import render, redirect
from .models import User
from django.conf import settings
from django.core.mail import send_mail
import random

def signup(request):
    if request.method == "POST":

        try:
            user=User.objects.get(email=request.POST['email'])
            msg="Email Is Already Registered"
            return render(request, 'signup.html', {'msg': msg})
        except:
            if request.POST['password']==request.POST['cpassword']:
                username = request.POST['username']
                fname = request.POST['fname']
                lname = request.POST['lname']
                email = request.POST['email']
                mobile = request.POST['mobile']
                password = request.POST['password']
                cpassword = request.POST['cpassword']  # Removed from form, added here for confirmation
                profile_pic=request.FILES['profile_pic']
            else:
                msg="Password & Confirm Password Does Not Matched"
                return render(request, 'signup.html', {'msg': msg})
        if password == cpassword:
            # Passwords match, create user instance
            user = User.objects.create(
                username=username,
                fname=fname,
                lname=lname,
                email=email,
                mobile=mobile,
                password=password,
                profile_pic=profile_pic,
            )
            msg = "User Sign Up Successfully"
            return render(request, 'signup.html', {'msg': msg})
        else:
            msg = "Password & Confirm Password Do Not Match"
            return render(request, 'signup.html', {'msg': msg})
    else:
        return render(request, 'signup.html')

def login(request):
	if request.method=="POST":
		try:
			user=User.objects.get(username=request.POST['username'])
			if user.password==request.POST['password']:
				request.session['username']=user.username
				request.session['fname']=user.fname
				request.session['profile_pic']=user.profile_pic.url
				return render(request,'home.html')
			else:
				msg="Incorrect Password"
				return render(request,'login.html',{'msg':msg})
		except:
			msg="Username Not Registered"
			return render(request,'login.html',{'msg':msg})
	else:
		return render(request,'login.html')

def home(request):
    # username = request.user.username
    return render(request, 'home.html')

def logout(request):
	return render(request,'login.html')

def change_password(request):
    if request.method=="POST":
        user=User.objects.get(username=request.session['username'])
        if user.password==request.POST['old_password']:
            if request.POST['new_password']==request.POST['cnew_password']:
                user.password=request.POST['new_password']
                user.save()
                return redirect('logout')
            else:
                  msg="Password & Confirm Password Does Not Matched"
                  return render(request,'change-password.html',{'msg':msg})
        else:
            msg="Old Password Does Not Matched" 
            return render(request,'change-password.html',{'msg':msg})
    else:
	    return render(request,'change-password.html')
    
def forgot_password(request):
    if request.method=="POST":
        try:
            user=User.objects.get(email=request.POST['email'])
            otp=random.randint(1000,9999)
            subject = 'OTP For Forgot Password'
            message = 'Hello '+user.fname+", Your OTP For Forgot Password Is "+str(otp)
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email,]
            send_mail( subject, message, email_from, recipient_list )
            return render(request,'otp.html',{'email':user.email,'otp':otp})
        except:
             msg="Email not Registered"
             return render(request,'forgot-password.html',{'msg':msg})

    else:
        return render(request,'forgot-password.html')

def verify_otp(request):
     email=request.POST['email']
     otp=request.POST['otp']
     uotp=request.POST['uotp']

     if otp==uotp:
        return render(request,'new-password.html',{'email':email})
     else:
        msg="Invalid OTP"
        return render(request,'otp.html',{'email':User.email,'otp':otp,'msg':msg})

def new_password(request):
     email=request.POST['email']
     new_password=request.POST['new_password']
     cnew_password=request.POST['cnew_password']

     if new_password==cnew_password:
          user=User.objects.get(email=email)
          user.password=new_password
          user.save()
          msg="Password Update Successfully"
          return render(request,'login.html',{'msg':msg})
     else:
          msg='Password & Confrm Password Dose Not Matched'
          return render(request,'new-password.html',{'email':email,'msg':msg})
    
def profile(request):
     user=User.objects.get(username=request.session['username'])
     if request.method=="POST":
        user=username=request.POST['username']
        user=fname=request.POST['fname']
        user=lname=request.POST['lname']
        user=mobile=request.POST['mobile']
        user.save()
        try:
            user=profile_pic=request.FILES['profile_pic']
        except:
            pass
        
        msg="Profile Updated Successfully"
        request.session['profile_pic']=user.profile_pic.url
        return render(request,'profile.html',{'user':user,'msg':msg})

     else:
        return render(request,'profile.html',{'user':user})