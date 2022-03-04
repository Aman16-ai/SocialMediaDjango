from django.contrib import admin
from django.urls import path,include
from home import views
urlpatterns = [
    path("",views.index,name="home"),
    path("signuppage",views.signuppage,name="signuppage"),
    path("HandleSignup/",views.handlesignup,name="handlesignuppage"),
    path("loginpage",views.loginpage,name="loginpage"),
    path("Handlelogin/",views.handlelogin,name="handlelogin"),
    path("myprofile/",views.myprofileinfo,name="myprofile"),
    path("logout/",views.logoutuser,name="logout"),
    path("likepost/<int:post_id>/",views.likePost,name="handlelike")
]
