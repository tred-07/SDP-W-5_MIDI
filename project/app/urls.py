from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home')
    ,path('login/',views.logIn,name='login'),
    path('signup/',views.signup,name='signup'),
    path('change_password_without_old_password/',views.set_password,name='Change_Password_Without_Old_Password'),
    path('change_password/',views.change_password,name='Change_Password'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),
    path('profile/',views.profile,name='profile'),
    path('logout/',views.logOut,name='logout')
]