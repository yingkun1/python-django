from django.shortcuts import render
# from django.http import HttpResponse
from datetime import datetime
from django.template import defaultfilters,defaulttags


def greet(word):
    # return HttpResponse("hello")
    return "hello world %s" % word

def index(request):
    context = {
        "greet":greet,
        "name":"yingkun",
    }
    return render(request,"index.html",context=context)

def add_view(request):
    context = {
        "value1":["1","2","3"],
        "value2":["4","5","6"],
    }
    return render(request,"add.html",context=context)

def cut_view(request):
    return render(request,"cut.html")

def data_view(request):
    context = {
        "today":datetime.now()
    }
    return render(request,"data.html",context=context)

def default_view(request):
    context = {
        "value":"hello",
    }
    return render(request,"default.html",context=context)

def first_view(request):
    context = {
        "value":["1","2","3"]
    }
    return render(request,"first.html",context=context)

def floatformat_view(request):
    context = {
        "value":34.269,
    }
    return render(request,"floatformat.html",context=context)

def join_view(request):
    context = {
        "value":[1,2,3],
    }
    return render(request,"join.html",context=context)

def length_view(request):
    context = {
        "value":"asdasdasdasdasd"
    }
    return render(request, "length.html", context=context)

def lower_view(request):
    context = {
        "value":"HELLO WORLD"
    }
    return render(request,"lower.html",context=context)

def random_view(request):
    context = {
        "value":["a","g","h"]
    }
    return render(request,"random.html",context=context)

def safe_view(request):
    context = {
        "value":"<script>alert('hello world');</script>"
    }
    return render(request,"safe.html",context=context)

def slice_view(request):
    context = {
        "value":[1,2,3,4,5,6,7,8,9]
    }
    return render(request,"slice.html",context=context)

def striptags_view(request):
    context = {
        "value":"<script>alert('hello world')</script>",
    }
    return render(request,"striptags.html",context=context)

def truncatechars_views(request):
    context = {
        "value":"<a>北京欢迎你~</a>"
    }
    return render(request,"truncatechars.html",context=context)