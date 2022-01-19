from django.urls import path
from .views_home import *
urlpatterns = [
    path('',v_index, name="Index"),
    path('home/', v_home, name="Home"),
    path('savebook/',v_savebook, name="Savebook"),
]