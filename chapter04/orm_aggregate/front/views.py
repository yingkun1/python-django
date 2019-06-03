from django.shortcuts import render
from .models import Author,Book,BookOrder,Publisher
from django.db.models import Avg,Count,Max,Min,Sum,F,Q,Prefetch
from django.http import HttpResponse
from django.db import connection
from django.db.models.manager import Manager
from django.db.models.query import QuerySet

def index(request):
    result = Book.objects.aggregate(avg=Avg("price"))
    print(result)
    # print(result.query)
    print(connection.queries)
    return HttpResponse("success")

def index2(request):
    # result = Book.objects.aggregate(avg=Avg("bookorder__price"))
    #我要获取每一本图书销售的平均价格，详情见book_order表
    books = Book.objects.annotate(avg=Avg("bookorder__price"))
    for book in books:
        print('%s/%s'%(book.name,book.avg))
    print(connection.queries)
    return HttpResponse("success")

def index3(request):
    #book表中总共有多少本书(book表中总共有多少个id)
    # result = Book.objects.aggregate(book_nums=Count("id"))
    # results = Book.objects.annotate(book_sale=Count("bookorder__id"))
    # print(result)
    # for result in results:
    #     print("%s/%s"%(result.name,result.book_sale))
    # print(connection.queries)
    # return HttpResponse("success")
    #统计作者表中总共有多少个不同的邮箱
    # result = Author.objects.aggregate(diff_email=Count("email",distinct=True))
    # print(result)
    # print(connection.queries)
    # return HttpResponse("success")
    results = Book.objects.annotate(diff_price=Count("bookorder__price",distinct=True))
    for result in results:
        print("%s/%s"%(result.name,result.diff_price))
    print(connection.queries)
    return HttpResponse("success")

def index4(request):
    # results = Author.objects.aggregate(max=Max("age"),min=Min("age"))
    # print(results)
    # print(connection.queries)
    # return HttpResponse("success")
    #获取每一本图书售卖的最大价格和最小价格
    results = Book.objects.annotate(max_price=Max("bookorder__price"),min_price=Min("bookorder__price"))
    for result in results:
        print("name:%s,max:%s,min:%s"%(result.name,result.max_price,result.min_price))
    print(connection.queries)
    return HttpResponse("success")

# def index5(request):
    #求出所有图书的销售总额
    # result = Book.objects.aggregate(sum_price=Sum("bookorder__price"))
    # print(result)
    # print(connection.queries)
    # return HttpResponse("success")
    #求每一本图书的销售总额
    # results = Book.objects.annotate(sum_price=Sum("bookorder__price"))
    # for result in results:
    #     print("%s:%s"%(result.name,result.sum_price))
    # print(connection.queries)
    # return HttpResponse("success")
    #求2019年每一本图书的销售总额
    # results = Book.objects.annotate(sum_price=Sum("bookorder__price")).filter(bookorder__create_time__year=2019)
    # for result in results:
    #     print("%s/%s"%(result.name,result.sum_price))
    # print(connection.queries)
    # return HttpResponse("success")
    #求2019年销售总额
    # results = BookOrder.objects.filter(cieate_time__year=2019).annotate(sum_price=Sum("price"))
    # for result in results:
        # print("%s/%s"%(
    # return HttpResponse("success")iii)
    # results = Book.objects.filter(""
    # results = Book.objects.filter(bookorder__create_time__year=2019).annotate(sum_price=Sum("bookorder__price"))
    # for result in results:
    #     print("%s,%s"%(result.name,result.sum_price))
    # print(connection.queries)
    # return HttpResponse("success")

def index6(request):
    #给每一本图书的售价增加10元
    # books = Book.objects.all()
    # for book in books:
    #     book.price += 10
    #     book.save()
    # print(connection.queries)
    # return HttpResponse("success")
    # Book.objects.update(price=F("price")+10)
    # print(connection.queries[-1])
    # return HttpResponse("success")
    authors = Author.objects.filter(name=F("email"))
    for author in authors:
        print("%s,%s"%(author.name,author.email))
    print(connection.queries[-1])
    return HttpResponse("success")

# def index7(request):
    # 1.获取价格大于90，并且评分在4.85以上的图书
    # results = Book.objects.filter(price__gte=90,rating__gte=4.85)
    # for result in results:
    #     print("%s:%s:%s"%(result.name,result.price,result.rating))
    # print(connection.queries[-1])
    # return HttpResponse("success")

    # results = Book.objects.filter(Q(price__gte=90)&Q(rating__gte=4.85))
    # for result in results:
    #     print("%s:%s:%s"%(result.name,result.price,result.rating))
    # print(connection.queries[-1])
    # return HttpResponse("success")

    #2.价格低于100元，或者评分低于4分的图书
    # results = Book.objects.filter(Q(price__lt=100)|Q(rating__lt=4))
    # for result in results:
    #     print("%s:%s:%s"%(result.name,result.price,result.rating))
    # print(connection.queries[-1])
    # return HttpResponse("success")

    #3.获取价格大于100，并且图书名字中不包含"记"字的图书
    # results = Book.objects.filter(Q(price__gte=100)&~Q(name__contains="记"))
    # for result in results:
    #     print("%s:%s:%s"%(result.name,result.price,result.rating))
    # print(connection.queries[-1])
    # return HttpResponse("success")

def index8(request):
    print(type(Book.objects))
    return HttpResponse("success")

def index9(request):
    # 提取所有id大于等于2的图书
    #链式调用
    # results = Book.objects.filter(id__gte=2).filter(~Q(id=3))
    # results = Book.objects.filter(id__gte=2).exclude(id=3)
    # result1s = results.filter(~Q(id=3))
    # print(type(results))
    # for result in results:
    #     print("%s:%s"%(result.id,result.name))
    # print(connection.queries[-1])
    # return HttpResponse("success")
    results = Book.objects.annotate(author_name=F("author__name"))
    for result in results:
        print("%s:%s"%(result.name,result.author_name))
    print(connection.queries[-1])
    return HttpResponse("success")

def index10(request):
    #1.根据create_time从小到大进行排序：
    # results = BookOrder.objects.order_by("create_time")

    #2.根据create_time从大到小进行排序：
    # results = BookOrder.objects.order_by("-create_time","-price")

    #3.根据订单额图书的评分来进行排序(从小到大)
    # results = BookOrder.objects.order_by("-book__rating")
    # for result in results:
        # print(result)
        # print("%s---%s"%(result.id,result.book.rating))
    # print(connection.queries[-1])
    # return HttpResponse("success")
    # orders = BookOrder.objects.order_by("create_time").order_by("price")
    # orders = BookOrder.objects.all()
    # for order in orders:
    #     print("%s--%s"%(order.create_time,order.price))
    # print(connection.queries[-1])
    # return HttpResponse("success")
    results = Book.objects.annotate(sum_number=Count("bookorder")).order_by("-sum_number")
    for result in results:
        print("%s:%s"%(result.name,result.sum_number))
    print(connection.queries)
    return HttpResponse("success")

def index11(request):
    # books = Book.objects.values("id","name",author_name=F("author__name"))
    # books = Book.objects.annotate(sum_number=Count("bookorder")).values("id","name","sum_number")
    # books = Book.objects.values("id","name",sum_numbers=Count("bookorder"))
    # books = Book.objects.values()
    books = Book.objects.values_list("name",flat=True)
    print(type(books))
    for book in books:
        # print("%s:%s"%(book["id"],book["name"]))
        print(book)
    print(connection.queries)
    return HttpResponse("success")

def index12(request):
    # books = Book.objects.all().select_related("author","publisher")
    # books = Book.objects.all().select_related("bookorder")
    books = Book.objects.all()
    # for book in books:
        # print("%s:%s"%(book.bookorder.price,book.bookorder.id))
        # print(book.publisher.name)
    # print(connection.queries)
    # return HttpResponse("success")

def index14(request):
    # books = Book.objects.all()
    # books = Book.objects.prefetch_related("bookorder_set")
    # for book in books:
    #     print("="*30)
    #     print(book.name)
    #     results = book.bookorder_set.all()
    #     for result in results:
    #         print("%s:%s"%(result.id,result.price))
    # books = Book.objects.prefetch_related("author")
    # for book in books:
    #     print(book.author.name)
    prefetch = Prefetch("bookorder_set",queryset=BookOrder.objects.filter(price__gte=90))
    books = Book.objects.prefetch_related("bookorder_set")
    for book in books:
        print("="*30)
        print(book.name)
        results = book.bookorder_set.all()
        results = book.bookorder_set.filter(price__get=90)
        for result in  results:
            print("%s:%s"%(result.id,result.price))
    for sql in connection.queries:
        print(sql)
    return HttpResponse("success")

def index15(request):
    # results = Book.objects.defer("name")
    # for result in results:
    #     print(result.name)
    # print(connection.queries)
    # return HttpResponse("success")

    results = Book.objects.only("name")
    for result in results:
        print("%s:%s"%(result.id,result.price))
    print(connection.queries)
    return HttpResponse("success")

def index16(request):
    book = Book.objects.get(pk__gte=2)
    print(book)
    print(connection.queries)
    return HttpResponse("success")

def index17(request):
    # publisher = Publisher(name="南邮出版社")
    # publisher.save()
    # print(connection.queries)
    # return HttpResponse("success")

    publisher = Publisher.objects.create(name="南方文学出版社")
    print(connection.queries)
    return HttpResponse("success")

def index18(request):
    # result = Publisher.objects.get_or_create(name="知了出版社")
    # result = Publisher.objects.get_or_create(name="知了efg出版社")
    # print(result[0])
    # print(connection.queries)
    # return HttpResponse("success")
    result = Publisher.objects.bulk_create(
        [Publisher(name="清华大学出版社"),
         Publisher(name="北京大学出版社"),
         ]
    )
    print(connection.queries)

    return HttpResponse("success")

def index19(request):
    # books = Book.objects.all()
    count = Book.objects.count()
    print(count)
    print(connection.queries)
    return HttpResponse("success")

def index20(request):
    result = Book.objects.filter(name="三国演义").exists()
    print(result)
    print(connection.queries)
    return HttpResponse("success")

def index21(request):
    # results = Book.objects.annotate(order_price=F("bookorder__price")).filter(bookorder__price__gte=80).distinct()
    # results = Book.objects.filter(bookorder__price__get=80).order_by("bookorder__price").distinct()
    results = Book.objects.filter(bookorder__price__gte=80).order_by("bookorder__price").distinct()
    for result in results:
        print("%s"%(result.name))
    print(connection.queries)
    return HttpResponse("success")

def index22(request):
    # Book.objects.update(price=F("price")+5)
    # books = Book.objects.all()
    # for book in books:
    #     book.price+=5
    #     book.save()
    Author.objects.filter(id__gte=4).delete()
    return HttpResponse("success")

def index23(request):
    #[0:2]
    # books = Book.objects.all()[0:2]
    books = Book.objects.get_queryset()[1:2]
    for book in books:
        print("%s:%s"%(book.id,book.name))
    print(connection.queries)
    return HttpResponse("success")

def index24(request):
    books = Book.objects.all()
    print(list(books))
    print(connection.queries)
    return HttpResponse("success")
