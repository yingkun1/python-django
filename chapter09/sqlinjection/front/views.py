from django.shortcuts import render
from django.db import connection
from .models import User

# def index(request):
#     context = {}
#     user_id = request.GET.get('user_id')
#     if user_id:
#         cursor = connection.cursor()
#         cursor.execute("select id,username from front_user where id=%s "%user_id)
#         rows = cursor.fetchall()
#         context['rows'] = rows
#     return render(request,"index.html",context=context   )

def index(request):
    context = {}
    username = request.GET.get('username')
    if username:
        cursor = connection.cursor()
        sql = "select id,username from front_user where username=%s"
        cursor.execute(sql,(username,))
        rows = cursor.fetchall()
        context['rows'] = rows
    return render(request, "index.html", context=context)
