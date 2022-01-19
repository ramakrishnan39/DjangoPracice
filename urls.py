from django.contrib import admin
from django.urls import path,include
from .home import views_home
urlpatterns = [
    path('home/',views_home.m_home,name='home'),
    path('profile/',views_home.m_profile, name='profile'),
    path('user/<str:usr>',views_home.m_user, name='user_usr'),
    path('friends/',views_home.m_friends, name='friends'), 
    path('savebook/',views_home.m_savebook,name='savebook'),
    path('edit/',views_home.m_profile,name="edit"),
]

