from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.v_index, name='index'),
    path('login/', views.v_login,name='login'),
    path('entry/', views.v_entry, name='Entry'),
    path('home/',views.v_home,name='Home'),
    path('viewall/',views.v_viewall, name='View_all'),
    path('viewreport/', views.v_viewreport, name='View_report'),
    path('logout/',views.v_logout,name="Logout"),
]