from django.contrib import admin
from django.urls import path,include
from . import views_home
urlpatterns = [
    path('', views_home.m_index, name='index'),
    path('login/',views_home.m_login,name='login'),
    path('register/',views_home.m_signin,name='register'),
    path('home/',views_home.m_home,name='home'),
    path('profile/',views_home.m_profile, name='profile'),
    path('user/<str:usr>',views_home.m_user, name='user_usr'),
    path('friends/',views_home.m_friends, name='friends'),
    path('logout/', views_home.m_logout, name='logout'), 
    path('savebook/',views_home.m_savebook,name='savebook'),
    path('edit/',views_home.m_profile,name="edit"),
    path('accounts/',include('django.contrib.auth.urls')),
]

