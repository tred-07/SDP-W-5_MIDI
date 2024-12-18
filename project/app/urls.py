from django.urls import path
from . import views

urlpatterns=[
    path('',views.homeCls.as_view(),name='home'),
    path('brandwise/<slug:slug1>',views.home,name='brandwise'),
    # path('login/',views.logIn,name='login'),
    path('login/',views.login.as_view(),name='login'),
    path('signup/',views.signup,name='signup'),
    path('change_password_without_old_password/',views.set_password,name='Change_Password_Without_Old_Password'),
    path('change_password/',views.change_password,name='Change_Password'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),
    path('profile/',views.profile,name='profile'),
    path('logout/',views.logOutCls.as_view(),name='logout'),
    path('buy_car/<int:id>',views.buy_car,name='buy_car'),
    path('detail_post/<int:id>',views.detail_post_view,name='detail_view'),
]