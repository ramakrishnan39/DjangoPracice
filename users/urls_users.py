from django.urls import path
from .views_users import *
urlpatterns = [
    path('login/',v_login, name="Login"),
    path('signin/',v_signin, name="Signin"),
    path('profile/', v_profile, name="Profile"),
    path('edit/',v_edit,name="Editprofile"),
    path('logout/', v_logout, name="Logout")
]