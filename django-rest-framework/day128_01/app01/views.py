from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.utils.decorators import method_decorator
import json

# Create your views here.
from django.views import View

# @csrf_exempt
# @csrf_protect
def users(request):
    user_list = ['alex','oldboy']
    return HttpResponse(json.dumps((user_list)))

# class MyBaseView(object):
#     def dispatch(self, request, *args, **kwargs):
#         print("before")
#         result = super(MyBaseView,self).dispatch(request, *args, **kwargs)
#         print("after")
#         return result

# class StudentView(MyBaseView,View):

@method_decorator(csrf_exempt,name="dispatch")
class StudentView(View):
    # def dispatch(self, request, *args, **kwargs):
    #     return HttpResponse('DISPATCH')
    #     func = getattr(self,request.method.lower())
    #     result = func(request, *args, **kwargs)
    #     return result
    # 基于反射实现自动分发dispatch
    # getattr(obj,request.method)
    # 但是在Python中反射比java中简单得多。使用反射获取到的函数和方法可以像平常一样加上括号直接调用，获取到类后可以直接构造实例
    def get(self,request,*args,**kwargs):
        print("get方法")
        return HttpResponse('GET')

    def post(self,request,*args,**kwargs):
        return HttpResponse('POST')

    def put(self,request,*args,**kwargs):
        return HttpResponse('PUT')

    def delete(self,request,*args,**kwargs):
        return HttpResponse('DELETE')

#传统api接口的开发
def get_order(request):
    pass

def add_order(request):
    pass

def delete_order(request):
    pass

def update_order(request):
    pass

#restful规范开发
def order(request):
    if request.method == "GET":
        return HttpResponse("获取订单")
    elif request.method == "POST":
        return HttpResponse("创建订单")
    elif request.method == "DELETE":
        return HttpResponse("删除订单")
    elif request.method == "PUT":
        return HttpResponse("更新订单")

#restful规范开发，基于CBV
class OrderView(View):
    def get(self,request,*args,**kwargs):
        result = {
            'code':1000,
            'message':'xxx'
        }
        return HttpResponse(json.dumps(result),status=201)

    def post(self,request,*args,**kwargs):
        return HttpResponse("创建订单")

    def put(self,request,*args,**kwargs):
        return HttpResponse("更新订单")

    def delete(self,request,*args,**kwargs):
        return HttpResponse("删除订单")


#rest framework
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication
from rest_framework import exceptions
from rest_framework.request import Request

class MyAuthentication(object):
    def authenticate(self,request):
        token = request._request.GET.get('token')
        #获取用户名和密码，去数据库中进行校验
        if not token:
            raise exceptions.AuthenticationFailed('用户认证失败')
        return ('alex',None)

    def authenticate_header(self,val):
        pass

class DogView(APIView):
    authentication_classes = [MyAuthentication]
    def get(self,request,*args,**kwargs):
        print(request)
        print(request.user)
        result = {
            'code':1000,
            'message':'xxx'
        }
        return HttpResponse(json.dumps(result),status=201)

    def post(self,request,*args,**kwargs):
        # self.dispatch()
        return HttpResponse("创建Dog")

    def put(self,request,*args,**kwargs):
        return HttpResponse("更新Dog")

    def delete(self,request,*args,**kwargs):
        return HttpResponse("删除Dog")
