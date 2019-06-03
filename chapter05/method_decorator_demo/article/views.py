from django.shortcuts import render
from  .models import Article
from django.views.decorators.http import require_http_methods,require_GET,require_POST,require_safe
from django.http import HttpResponse

#require_GET=require_http_methods(['GET'])

#require_safe = require_http_method(['GET','HEAD'])
# @require_http_methods(['GET'])
@require_GET
def index(request):
    #首页返回所有的文章
    #只能使用GET请求来访问这个视图函数
    articles = Article.objects.all()
    context = {
        "articles":articles
    }
    return render(request,"index.html",context=context)

@require_http_methods(['POST','GET'])
def add_article(request):
    if request.method == "GET":
        return render(request,"add_article.html")
    else:
        title = request.POST.get("title")
        content = request.POST.get("content")
        Article.objects.create(title=title,content=content)
        return HttpResponse("success")
