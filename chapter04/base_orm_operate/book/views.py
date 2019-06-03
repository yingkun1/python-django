from django.shortcuts import render
from .models import Book
from django.http import HttpResponse

def index(request):
    #1.使用ORM添加一条数据到数据库中
    # book = Book(name="西游记",author="吴承恩",price=110)
    # book.save()
    # return HttpResponse("数据添加成功")

    #2.使用ORM查询数据
    #2.1根据主键进行查找
    #primary key
    # book = Book.objects.get(pk=2)
    # print(book)
    # return HttpResponse("数据查询成功")
    #2.2根据其它条件进行查找
    # books = Book.objects.filter(name="三国演义").first()
    # print(books)
    # return HttpResponse("数据查询成功")

    #3.使用ORM删除数据
    # book = Book.objects.get(pk=1)
    # book.delete()
    # return HttpResponse("数据删除成功")

    #4.修改数据
    book = Book.objects.get(pk=1)
    book.price = 800
    book.save()
    return HttpResponse("修改数据成功")