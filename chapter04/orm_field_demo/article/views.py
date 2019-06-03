from django.shortcuts import render
from django.http import HttpResponse
from .models import Article,Person,Author
from django.utils.timezone import now,localtime
import pytz
from datetime import datetime

def index(request):
    # article = Article(remove=False)
    # article.save()
    # article = Article()
    # article.save()
    # now = datetime.now()
    # utc_timezone = pytz.timezone("UTC")
    # # now = now.replace(tzinfo=pytz.timezone("Asia/Shanghai"))
    # print(now.astimezone(utc_timezone))
    # return HttpResponse("success")
    # article = Article(title="abc",create_time=localtime())
    # article.save()
    # article = Article.objects.get(pk=1)
    # create_time = article.create_time
    # print("="*30)
    # print(create_time)
    # print(localtime(create_time))
    # print("="*30)
    # return HttpResponse("保存成功")
    # return render(request,"index.html",context={"create_time":create_time})
    # article = Article(title="aaa")
    article = Article.objects.get(pk=6)
    article.title="111"
    article.save()
    return HttpResponse("success")

def email_view(request):
    #ModelForm
    #EmailField在数据库层面并不会限制字符串一定要满足邮箱格式
    #只是以后在使用ModelForm等表单相关操作的时候会起作用
    p = Person(email="aaa")
    p.save()
    return HttpResponse("success")

def null_test_field_view(request):
    author = Author(username="zhiliao")
    author.save()
    return HttpResponse("success")

def unique_view(request):
    author = Author(username="aaa",telephone="222")
    author.save()
    return HttpResponse("success")

def order_view(request):
    authors = Author.objects.all()
    for author in authors:
        print(author)
    return HttpResponse("success")