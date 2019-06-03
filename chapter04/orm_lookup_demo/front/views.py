from django.shortcuts import render
from django.http import HttpResponse
from .models import Article,Category
from datetime import datetime,time
from django.utils.timezone import make_aware

# Create your views here.
def index(request):
    #在windows操作系统上，mysql的排序规则(collation)无论是什么都是大小写不敏感的
    #在linux操作系统上，Mysql的排序规则(collation)是utf8_bin，那么就是大小写敏感的
    # article = Article.objects.filter(title="hello world")
    # article = Article.objects.filter(title=None)
    # article = Article.objects.filter(title__iexact="hrello world")
    #like %hello% "hello world","nihao hello"
    #LIKE和=:大部分情况下都是等价的，只有少数情况下是不等价的
    #iexact和exact:他们的区别其实就是LIKE和=的区别，exact会被翻译成=号，而iexact会被翻译成like
    article = Article.objects.filter(title__iexact="%hello%")
    print(article)
    print(article.query)
    return HttpResponse("success")

def index1(request):
    article = Article.objects.filter(pk=1)
    print(type(article))
    print(article)
    print(article.query)
    return HttpResponse("success")

def index2(request):
    result = Article.objects.filter(title__icontains="Hello")
    print(result.query)
    print(result)
    return HttpResponse("success")

def index3(request):
    # articles = Article.objects.filter(id__in=[1,2,3,4])
    # print(articles.query)
    # for article in articles:
    #     print(article)
    # return HttpResponse("success")
    # categorys = Category.objects.filter(articles__in=[1,2,3])
    # for category in categorys:
    #     print(category)
    # return HttpResponse("success")
    categorys = Category.objects.filter(articles__title__icontains="hello")
    for category in categorys:
        print(category)
    print(categorys.query)
    return HttpResponse("success")

def index4(request):
    #查询id大于2的所有文章
    articles = Article.objects.filter(id__lt=3)
    for article in articles:
        print(article)
    print(articles.query)
    return HttpResponse("success")

def index5(request):
    articles = Article.objects.filter(title__istartswith="hello")
    print(articles.query)
    for article in articles:
        print(article)
    return HttpResponse("success")

def index6(request):
    start_time = make_aware(datetime(year=2019,month=3,day=7,hour=16,minute=0,second=0))
    end_time = make_aware(datetime(year=2019,month=3,day=7,hour=17,minute=0,second=0))
    article = Article.objects.filter(create_time__range=(start_time,end_time))
    print(article.query)
    print(article)
    return HttpResponse("success")

def index7(request):
    # articles = Article.objects.filter(create_time__date=datetime(year=2019,month=3,day=7))
    # articles = Article.objects.filter(create_time__year__gte=2019)
    # articles = Article.objects.filter(create_time__week_day=5)
    start_time = time(hour=16,minute=35,second=4)
    end_time = time(hour=16,minute=35,second=5)
    articles = Article.objects.filter(create_time__time__range=(start_time,end_time))
    print(articles.query)
    # for article in articles:
    #     print(article)
    print(articles)
    return HttpResponse("success")

def index8(request):
    # articles = Article.objects.filter(create_time__isnull=False)
    # articles = Article.objects.filter(title__iregex=r"^hello")
    articles = Article.objects.filter(title__regex=r"hello$")
    print(articles.query)
    print(articles)
    return HttpResponse("success")




















