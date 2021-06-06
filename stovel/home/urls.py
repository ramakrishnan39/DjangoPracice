from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.m_index, name='index'),
    path('login/',views.m_login,name='login'),
    path('register/',views.m_signin,name='register'),
    path('home/',views.m_home,name='home'),
    path('profile/',views.m_profile, name='profile'),
    path('friends/',views.m_friends, name='friends'),
    path('logout/', views.m_logout, name='logout'), 
    path('savebook/',views.m_savebook,name='savebook'),
    path('edit/',views.m_edit,name="edit"),
    path('accounts/',include('django.contrib.auth.urls'))
]

