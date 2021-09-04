from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.urls.base import reverse

# Create your views here.
def v_index(request):
    return render(request, 'Home.html')

def v_login(request):
    if request.method == "GET":
        return render(request,"registration/login.html")
    elif request.method =="POST":
        return redirect('../home')

def v_home(request):
    return render(request,'Homepage.html')


def v_entry(request):
    return render(request,'Entry.html')

def v_viewall(request):
    return render(request,'Viewall.html')

def v_viewreport(request):
    return render(request, 'Reports.html')

def v_logout(request):
    return render(request,'Home.html')