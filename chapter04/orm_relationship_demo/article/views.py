from django.shortcuts import render
from .models import Article,Category,Tag
from django.http import HttpResponse
from frontuser.models import FrontUser,UserExtension


def index(request):
    # category = Category(name="最新文章")
    # category.save()
    # article = Article(title='abc',context="111")
    # article.category = category
    # article.save()
    article = Article.objects.first()
    print("="*30)
    print(article.category.name)
    print("="*30)
    return HttpResponse("success")

def delete_view(request):
    category = Category.objects.get(pk=6)
    category.delete()
    return HttpResponse("success")

def one_to_many_view(request):
    #1对多的关联操作
    # article = Article(title="钢铁是怎样炼成的",context="dsadsadsdsad")
    # category = Category.objects.first()
    # author = FrontUser.objects.first()
    # article.category = category
    # article.author = author
    # article.save()
    # return HttpResponse("success")

    #2.获取某个分类下的所有文章
    category = Category.objects.first()
    #RelateManager
    # article = category.article_set.first()
    # print("="*30)
    # print(article)
    # return HttpResponse("success")
    # articles = category.articles.all()
    # for article in articles:
    #     print(article)
    # return HttpResponse("success")
    article = Article(title="疯狂的外星人",context="耿浩")
    article.author = FrontUser.objects.first()
    # article.save()
    category.articles.add(article,bulk=False)
    # category.save()
    return HttpResponse("success")

def one_to_one_view(request):
    # user = FrontUser.objects.first()
    # extension = UserExtension(school="清华")
    # extension.user = user
    # extension.save()
    # extension = UserExtension.objects.first()
    # print(extension.user)
    user = FrontUser.objects.first()
    print(user.extension)
    return HttpResponse("success")

def many_to_many_view(requets):
    # article = Article.objects.first()
    # tag = Tag(name="冷门文章")
    # tag.save()
    # article.tag_set.add(tag)
    # article.save()
    # tag = Tag.objects.first()
    # article = Article.objects.get(pk=6)
    # tag.article.add(article)
    # return HttpResponse("success")
    article = Article.objects.get(pk=5)
    tags = article.tags.all()
    for tag in tags:
        print(tag)
    return HttpResponse("success")