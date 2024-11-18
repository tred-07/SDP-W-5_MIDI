from car.models import Car
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import login,logout,update_session_auth_hash,authenticate
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm,UserChangeForm
from django.contrib import messages 
from . import form
from carList.form import carlist
from carList.models import CarList
from datetime import datetime
from brand.models import Brand
def home(r,slug1=None):
    cars=Car.objects.all()
    brand_names=Brand.objects.all()
    if slug1 is not None:
        brand_name=Brand.objects.get(slug=slug1)
        cars=Car.objects.filter(brand_name=brand_name)
    return render(r,'home.html',{'cars':cars,'type':'Home','brands':brand_names})

def profile(r):
    cars=Car.objects.all()
    carlists=CarList.objects.filter(owner=r.user)
    print(carlists)
    return render(r,'profile.html',{'cars':cars,'carlists':carlists,'type':'Profile',})

def edit_cars(r):
    if not r.user.is_authenticated:
        return redirect('login')
    cars=Car.objects.filter(Car_added_by=r.user)
    return render(r,'edit_Car.html',{'cars':cars,'type':'Profile','user':r.user})

def signup(r):
    # if r.user.is_authenticated:
    #     return redirect('profile')
    if r.method=='POST':
       form1=form.SignUp(r.POST)
       if form1.is_valid():
           form1.save()
           messages.success(r,'Sign up Successful')
           return redirect('home')
    return render(r,'form.html',{'form':form.SignUp(),'type':'Sign Up'})


def logIn(r):
    if r.user.is_authenticated:
        return redirect('profile')
    if r.method=='POST':
        form1=AuthenticationForm(request=r,data=r.POST)
        if form1.is_valid():
           name=form1.cleaned_data['username']
           userpassword=form1.cleaned_data['password']
           user=authenticate(username=name,password=userpassword)
           if user is not None:
               login(r,user)
               messages.success(r,'Log in Successful')
               return redirect('profile')
        messages.error(r,'Wrong Credential')
        return render(r,'form.html',{'form':AuthenticationForm(),'type':'Log In'})
    return render(r,'form.html',{'form':AuthenticationForm(),'type':'Log In'})


def logOut(r):
    logout(r)
    messages.success(r,'Log out Successful')
    return redirect('home')


def change_password(r):
    if not r.user.is_authenticated:
        return redirect('login')
    if r.method=='POST':
        form1=PasswordChangeForm(user=r.user,data=r.POST)
        if form1.is_valid():
            form1.save(commit=True)
            update_session_auth_hash(request=r,user=r.user)
            messages.success(r,'Changes Successful')
            return redirect('logout')
        messages.error(r,'Wrong Credential')
        return render(r,'form.html',{'form':form1,'type':'Change Password'})
    else:

        return render(r,'form.html',{'form':PasswordChangeForm(r.POST),'type':'Change Password'})
    

def set_password(r):
    if not r.user.is_authenticated:
        return redirect('login')
    if r.method=='POST':
        form1=SetPasswordForm(user=r.user,data=r.POST)
        if form1.is_valid():
            form1.save()
            messages.success(r,'Changes Successful')
            return redirect('logout')
        messages.error(r,'Wrong Credential')
        return render(r,'form.html',{'form':form1,'type':'Change Password Without Old Password'})
    return render(r,'form.html',{'form':SetPasswordForm(user=r.user),'type':'Change Password Without Old Password'})
    

def edit_profile(r):
    if not r.user.is_authenticated:
        return redirect('login')
    form1=form.EditForm(instance=r.user)
    if r.method=='POST':
        form1=form.EditForm(r.POST,instance=r.user)
        if form1.is_valid():
            form1.save()
            messages.success(r,'Changes Successful')
            return redirect('logout')

    return render(r,'form.html',{'form':form1,'type':'Edit Profile'})



def buy_car(r,id):
    if not r.user.is_authenticated:
        return redirect('login')
    car=Car.objects.get(pk=id)
    print(car.name)
    print(car.quantity)
    car.quantity-=1
    car.save()
    car1=CarList()
    car1.name=car.name
    car1.image=car.image
    car1.price=car.price
    car1.quantity+=1
    car1.brand_name=car.brand_name
    car1.owner=r.user
    car1.date=datetime.now()
    car1.save()
    return redirect('profile')
    