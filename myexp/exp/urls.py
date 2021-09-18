from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.v_index, name='index'),
    path('login/', views.v_login,name='login'),
    path('register/',views.v_register,name='register'),
    path('add/<str:expense>/<int:amount>/<str:desc>/<str:expdate>', views.v_add, name='AddExp'),
    path('delete/<int:expid>/<str:expdate>', views.v_delete, name='Delete'),
    path('home/<str:sdate>',views.v_home,name='Home'),
    path('report/',views.v_report,name="Report"),
    path('logout/',views.v_logout,name="Logout"),
]