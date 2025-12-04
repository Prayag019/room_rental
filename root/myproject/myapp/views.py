from django.shortcuts import render,redirect
from .forms import Room_Details_Form,SignUpForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import Room_Details
from django.contrib.auth import login

# Create your views here.
def Room_Form_View(request):
    if request.method=='POST':
       form=Room_Details_Form(request.POST)
       if form.is_valid() :
        room_details=form.save(commit=False)
        room_details.owner=request.user
        room_details.save()
        return redirect('homepage')
    else:    
     form=Room_Details_Form()



    return render(request,'form/Room_Details_Form.html',{'form':form})

def User_Information(request):

    if request.method=='POST':

        form=SignUpForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('login-form')
    else:
     form=SignUpForm()
    return render(request,'form/user_information.html',{'form':form})

def Login_Form(request):
    if request.method=='POST':
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('homepage')
    else:        
       form=AuthenticationForm()
    return render(request,'form/login_form.html',{'form':form}) 

def Homepage(request):
    if request.user.is_authenticated:
      return render(request,'pages/home-page.html')
    else:
       return redirect('login-form')      





