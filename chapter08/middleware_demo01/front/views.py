from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic import View
from .models import User
from django.middleware.common import CommonMiddleware
from django.middleware.gzip import GZipMiddleware
from django.contrib.messages.middleware import MessageMiddleware
from django.middleware.security import SecurityMiddleware
from django.contrib.sessions.middleware import SessionMiddleware
from django.contrib.auth.middleware import AuthenticationMiddleware
from django.middleware.csrf import CsrfViewMiddleware
from django.middleware.clickjacking import XFrameOptionsMiddleware

def index(request):
    # user_id = request.session.get('user_id')
    # user = User.objects.get(pk=user_id)
    # print(user.username)
    print("这是index view中执行的代码")
    if request.front_user:
        print(request.front_user.username)
    # return HttpResponse("index")
    return render(request,"index.html ")

def my_list(request):
    if request.front_user:
        print(request.front_user.username)
    return HttpResponse("success")

class SigninView(View):
    def get(self,request):
        return render(request,"login.html")

    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username,password=password).first()
        if user:
            request.session['user_id'] = user.id
            return redirect(reverse("index"))
        else:
            messages.info(request,'用户名或者密码错误!')
            return redirect(reverse("login"))