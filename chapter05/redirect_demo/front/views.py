from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse

def index(request):
    #如果没有登录，那么就重定向到注册界面
    #如果在url中，传递了username这个参数，那么就认为是登录了，否则就没有登录
    #/?username=xxx
    # if request.GET.get("username"):
    username = request.GET.get("username")
    if username:
        return HttpResponse("首页")
    else:
        return redirect(reverse("signup"))

def signup(request):
    return HttpResponse("注册页")
