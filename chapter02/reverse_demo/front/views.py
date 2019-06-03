from django.http import HttpResponse
from django.shortcuts import reverse,redirect

def index(request):
    username = request.GET.get("username")
    if username:
        return HttpResponse("首页")
    else:
        # login_url = reverse("login")
        # return redirect(login_url)
        #kwargs:keyword arguments
        # detail_url = reverse("detail",kwargs={"article_id":1,"page":2})
        # return redirect(detail_url)
        login_url = reverse('login') + "?next=/"
        return redirect(login_url)


def login(request):
    return HttpResponse("登录页面")

def article_detail(request,article_id,page):
    text = "您的文章id是:%s" % article_id
    return HttpResponse(text)
