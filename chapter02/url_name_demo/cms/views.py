from django.http import HttpResponse
from django.shortcuts import redirect,reverse

def index(request):
    username = request.GET.get("username")
    if username:
        return HttpResponse("CMS首页")
    else:
        #获取当前的命名空间
        current_namespace = request.resolver_match.namespace
        return redirect(reverse("%s:login"%current_namespace))

def login(request):
    return HttpResponse("CMS登录页面")


