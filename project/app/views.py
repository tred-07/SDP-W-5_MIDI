from car.models import Car
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import login,logout,update_session_auth_hash,authenticate
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm,UserChangeForm
from django.contrib import messages 
from . import form
from django.contrib.auth.decorators import login_required
def home(r):
    # if r.user.is_authenticated:
    #     return redirect('profile')
    cars=Car.objects.all()
    return render(r,'home.html',{'cars':cars,'type':'Home'})

def profile(r):
    cars=Car.objects.all()
    return render(r,'profile.html',{'cars':cars,'type':'Profile'})

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
    
@login_required
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



# def add_Car(r):
#     if not r.user.is_authenticated:
#         return redirect('login')
#     if r.method=='POST':
#        form1=form.AddCar(r.POST)
#        form1.instance.Car_added_by=r.user
#        if form1.is_valid():
#            form1.save()
#            return redirect('profile')
#     return render(r,'form.html',{'form':form.AddCar(),'type':'Add Car'})

# def add_musician(r):
#     if not r.user.is_authenticated:
#         return redirect('login')
#     if r.method=='POST':
#        form1=form.AddMusician(r.POST)
#        if form1.is_valid() :
#            form1.save()
#            return redirect('profile')
#     return render(r,'form.html',{'form':form.AddMusician(),'type':'Add Musician'})

# @login_required
# def edit_Car(r,id):
#     if not r.user.is_authenticated:
#         return redirect('login')
#     Car=Car.objects.get(pk=id)
#     form1=form.AddCar(instance=Car)
#     print(type(form1.instance.Car_added_by))
#     print(type(str(r.user)))
#     if r.method=='POST' and form1.instance.Car_added_by==str(r.user):
#         form1=form.AddCar(r.POST,instance=Car)
#         if form1.is_valid():
#             form1.save()
#             return redirect('profile')
#         return render(r,'form.html',{'form':form1,'type':'Edit Car'})
#     return render(r,'form.html',{'form':form1,'type':'Edit Car'})


# def delete_Car(r,id):
#     if not r.user.is_authenticated:
#         return redirect('login')
#     Car=Car.objects.get(pk=id)
#     print(Car)
#     Car.delete()
#     print(Car)
#     return redirect('profile')
    





