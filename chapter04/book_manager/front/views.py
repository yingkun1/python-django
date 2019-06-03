from django.shortcuts import render,redirect,reverse
from django.db import connection

def get_cursor():
    return connection.cursor()

def index(request):
    cursor = get_cursor()
    cursor.execute("select id,name,author from book")
    books = cursor.fetchall()
    #books [(1,"三国演义","罗贯中")...()]
    return render(request,"index.html",context={"books":books})

def add_book(request):
    if request.method == "GET":
        return render(request,"add_book.html")
    else:
        name = request.POST.get("name")
        author = request.POST.get("author")
        cursor = get_cursor()
        cursor.execute("insert into book(id,name,author) values(null,'%s','%s')" % (name,author))
        return redirect(reverse("index"))

def book_detail(request,book_id):
    cursor = get_cursor()
    cursor.execute("select * from book where id=%s" % book_id)
    book = cursor.fetchone()
    return render(request,"book_detail.html",context={"book":book})

def delete_book(request):
    if request.method == "POST":
        book_id = request.POST.get("book_id")
        cursor = get_cursor()
        cursor.execute("delete from book where id=%s" % book_id)
        return redirect(reverse("index"))
    else:
        raise RuntimeError("删除图书的method错误!")