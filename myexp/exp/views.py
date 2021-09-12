from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.urls.base import reverse
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth import authenticate, login
from .models import Expense
from datetime import date,datetime

# Create your views here.
def v_index(request):
    return render(request, 'Index.html')

def v_register(request):
    if request.method == 'POST':
        ufname = request.POST['txt_firstname']
        ulname = request.POST['txt_lastname']
        passwd = request.POST['pwd_signin']
        umail = request.POST['txt_email']
        username = request.POST['txt_username']
        if User.objects.filter(username = username).exists():
            messages.info(request,'Username is taken')
        elif User.objects.filter(email=umail).exists():
            messages.info(request,'Email is taken')
        else:
            usr = User(username=username, password=passwd,first_name=ufname,last_name = ulname,email=umail)
            usr.save()
            messages.info(request,'Successfully signed in! Please use the login window to login now...')
        return redirect(reverse('../home'))
    else:
        return render(request,'registration/register.html', {'title': 'Sign In '})


def v_login(request):
    if request.method == 'POST':
        uname = request.POST['txt_username']
        passwd = request.POST['pwd_login']
        user = authenticate(username=uname,password=passwd)
        formdate = date.today()
        if user is not None:
            if user.is_active:
                login(request,user)
                exp = Expense.objects.filter(expense_date=formdate)
                return redirect(f"/home/{str(formdate)}",{'user':user, 'exps':exp, 'appdate' : formdate})
            else:
                return HttpResponse('Please check your Email and Password ')
        else:
            return HttpResponse('Please check your Email and Password ')
    elif request.method == 'GET':
        return render(request,'registration/login.html')

def v_home(request,sdate):
    if request.method== 'GET':
        ddate=datetime.strptime(sdate,"%Y-%m-%d")
        ex = Expense.objects.filter(expense_date=ddate)
        context = {'exps':ex, 'appdate':sdate}
        return render(request,'Homepage.html',context)


def v_add(request,expense, amount,expdate):
    dexpdate=datetime.strptime(expdate,"%Y-%m-%d")
    objExp=Expense(userid=request.user,expense_date=dexpdate,expense_name=expense,amount=amount)
    objExp.save()
    return redirect(f"/home/{expdate}")


def v_delete(request,expid,expdate):
    exp = Expense.objects.filter(id=expid)
    exp.delete()
    return redirect(f"/home/{expdate}")


def v_logout(request):
    auth.logout(request)
    return redirect("index")