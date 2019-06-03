from django.http import HttpResponse
from django.shortcuts import redirect,reverse

def index(request):
    #?username=xxx
    username = request.GET.get("username")
    if username:
        return HttpResponse("前台首页")
    else:
        login_url = reverse("front:login")
        print("="*30)
        print(login_url)
        print("="*30)
        return redirect(login_url)


def login(request):
    return HttpResponse("前台登录页面")

