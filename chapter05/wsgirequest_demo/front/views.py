from django.shortcuts import render
from django.http import HttpResponse
from django.core.handlers.wsgi import WSGIRequest

def index(request):
    # print(type(request))
    print(request.path)
    return HttpResponse("index")

def login(request):
    # print(request.path)
    # print(request.get_full_path())
    # print(request.get_raw_uri())
    # for key,value in request.META.items():
    #     print("%s:%s"%(key,value))
    # print(request.get_host())
    # print(request.is_secure())
    print(request.is_ajax())
    return HttpResponse("login")
