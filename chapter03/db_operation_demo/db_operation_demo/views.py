from django.shortcuts import render
from django.db import connection

def index(request):
    cursor = connection.cursor()
    cursor.execute("insert into book(id,name,author) values(null,'三国演义','罗贯中')")
    return render(request,"index.html")