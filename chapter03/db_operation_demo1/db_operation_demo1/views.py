from django.shortcuts import render
from django.db import connection

def index(request):
    cursor = connection.cursor()
    # cursor.execute("insert into book(id,name,author) values(null,'三国演义','罗贯中')")
    cursor.execute("select * from book")
    #返回一条数据
    # rows = cursor.fetchone()
    #返回所有数据
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    return render(request,"index.html")
