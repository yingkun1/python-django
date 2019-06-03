from django.shortcuts import render,reverse
from django.views import View
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.request import Request
from rest_framework.versioning import BaseVersioning,QueryParameterVersioning,URLPathVersioning
from .models import Role,UserGroup,UserToken,UserInfo
import json
from .utils.serializers.pager import PagerSerializers

# class ParamVersion(object):
#     def determine_version(self,request,*args,**kwargs):
#         version = request.query_params.get('version')
#         return version


class UsersView(APIView):
    # versioning_class = ParamVersion
    # versioning_class = QueryParameterVersioning
    # versioning_class = URLPathVersioning
    def get(self,request,*args,**kwargs):
        # version = request._request.GET.get('version')
        # print(version)
        # version2 = request.query_params.get('version2')
        # print(version2)
        # self.dispatch() #源码入口
        #获取版本
        # print(request.version)
        # #获取处理版本的对象
        # print(request.versioning_scheme)
        # #反向生成URL(rest framework)
        # url = request.versioning_scheme.reverse(viewname="users",request=request)
        # # print(url)
        # #反向生成URL(基于django内置的)
        # url2 = reverse(viewname="users",kwargs={'version':1})
        # print(url2)
        print(request._request)
        return HttpResponse('用户列表')

class DjangoView(APIView):
    def post(self,request,*args,**kwargs):
        print(type(request._request))
        from django.core.handlers.wsgi import WSGIRequest
        return HttpResponse("POST和Body")

from rest_framework.parsers import JSONParser,FormParser
class ParserView(APIView):
    # parser_classes = [JSONParser,FormParser]
    """
    JSONParser:表示只能解析content-type:application/json头
    FormParser:表示只能解析content-type:application/x-www-form-urlencoded头
    """
    def post(self,request,*args,**kwargs):
        """
        允许用户发送JSON格式数据
            a. content-type:application/json
            b.{'name':'alex','age':18}
        :param request:
        :param args:
        :param kwargs:
        :return:
        """

        #获取解析后的结果
        """
        1.获取用户请求头
        2.获取用户请求体
        3.根据用户请求头和parser_classes = [JSONParser,FormParser]中支持的请求头进行比较
        4.JSONParser对象处理请求体
        5.处理完成后赋值给request.data
        """
        print(request.data)
        # self.dispatch()#源码入口
        return HttpResponse('ParserView')


from rest_framework import serializers
class RolesSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()


class RolesView(APIView):
    def get(self,request,*args,**kwargs):
        #方法一：解决序列化
        # roles1 = Role.objects.all()
        # print("="*30)
        # print(roles1)
        # print(type(roles1))
        # roles = Role.objects.all().values('id','title')
        # print("=" * 30)
        # print(roles)
        # print(type(roles))
        # result = list(roles)
        # print("=" * 30)
        # print(result)
        # print(type(result))
        # result1 = json.dumps(result,ensure_ascii=False)
        # print("=" * 30)
        # print(result1)
        # print(type(result1))
        # return HttpResponse(result1)

        #方法二:对于[obj,obj.obj]
        # roles = Role.objects.all()
        # ser = RolesSerializer(instance=roles,many=True)
        # print(ser.data)
        # print(type(ser.data))
        # result = json.dumps(ser.data,ensure_ascii=False)
        # print(result)
        # return HttpResponse(result)

        #方法三：
        role = Role.objects.all().first()
        ser = RolesSerializer(instance=role)
        #ser.data已经是转换完成的结果
        result = json.dumps(ser.data,ensure_ascii=False)
        return HttpResponse(result)

# class UserInfoSerializer(serializers.Serializer):
#     xxx = serializers.CharField(source="user_type")
#     xxx2 = serializers.CharField(source="get_user_type_display")#row.get_user_type_display
#     username = serializers.CharField()
#     password = serializers.CharField()
#     gp = serializers.CharField(source="group.title")
#     # rls = serializers.CharField(source="role.all")
#     rls = serializers.SerializerMethodField() #自定义显示
#     def get_rls(self,row):
#         role_obj_list = row.role.all()
#         ret = []
#         for item in role_obj_list:
#             ret.append({'id':item.id,'title':item.title})
#         # return [
#         #     {'id':1,'title':'老师'},
#         #     {'id':2,'title':'袁浩'},
#         # ]
#         return ret

class MyField(serializers.CharField):
    def to_representation(self, value):
        print(value)
        return "xxxxx"

# class UserInfoSerializer(serializers.ModelSerializer):
#     user_type = serializers.CharField(source="get_user_type_display")
#     rls = serializers.SerializerMethodField() #自定义显示
#     x1 = MyField(source="username")
#     def get_rls(self,row):
#         role_obj_list = row.role.all()
#         ret = []
#         for item in role_obj_list:
#             ret.append({'id':item.id,'title':item.title})
#             return ret
#
#     class Meta:
#         model = UserInfo
#         # fields = "__all__"
#         fields = ['id','username','password','user_type','rls','group','x1']
#         # extra_kwargs = {'group':{'source':'group.title'}}

class UserInfoSerializer(serializers.ModelSerializer):
    group = serializers.HyperlinkedIdentityField(view_name="group",lookup_field="group_id",lookup_url_kwarg="pk")
    class Meta:
        model = UserInfo
        fields = ['id','username','password','group','role']
        depth = 0

# serializers.CharField
class UserInfoView(APIView):
    def get(self,request,*args,**kwargs):
        userinfos = UserInfo.objects.all()
        # 对象，Serializer类处理:self.to_representation
        # QuerySet, ListSerializer类处理
        #1.实例化，一般是将数据封装到对象:__new__,__init__
        """
        many=True,接下来执行ListSerializer对象的构造方法
        many=False,接下来执行UserInfoSerializer对象的构造方法
        """

        ser = UserInfoSerializer(instance=userinfos,many=True,context={'request': request})
        # ser.data
        print(ser)
        #2.调用对象的data属性
        result = json.dumps(ser.data,ensure_ascii=False)
        return HttpResponse(result)
        # return HttpResponse(ser.data)


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGroup
        fields = "__all__"

class GroupView(APIView):
    def get(self,request,*args,**kwargs):
        pk = kwargs.get('pk')
        groups = UserGroup.objects.get(pk=pk)
        ser = GroupSerializer(instance=groups,many=False)
        result = json.dumps(ser.data,ensure_ascii=False)
        return HttpResponse(result)


class NameValidator(object):
    def __init__(self,base):
        self.base = str(base)

    def __call__(self,value):
        # if value != self.base:
        if not value.startswith(self.base):
            message = "标题必须以%s为开头." % self.base
            raise serializers.ValidationError(message)

    def set_context(self,serializer_field):
        pass

class UserGroupSerializer(serializers.Serializer):
    title = serializers.CharField(error_messages={'required':'标题不能为空'},validators=[NameValidator('老男人')])

    def validate(self, value):
        from rest_framework import exceptions
        # print(value,1111)
        # return value
        raise exceptions.ValidationError("看你不顺眼")
        return value

class UserGroupView(APIView):
    def post(self,request,*args,**kwargs):
        ser = UserGroupSerializer(data=request.data)
        if ser.is_valid():
            print(ser.validated_data['title'])
        else:
            print(ser.errors)
        return HttpResponse("提交数据")

from .utils.serializers.pager import PagerSerializers
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination,CursorPagination

# class MyPageNumberPagination(PageNumberPagination):
#     page_size = 2
#     page_size_query_param = 'size'
#     max_page_size = 5
#     page_query_param = 'page'

# class MyPageNumberPagination(LimitOffsetPagination):
#     default_limit = 2
#     limit_query_param = 'limit'
#     offset_query_param = 'offset'
#     max_limit = 5

class MyPageNumberPagination(CursorPagination):
    cursor_query_param = 'cursor'
    page_size = 2
    ordering = 'id'
    page_size_query_param = None
    max_page_size = None

class Pager1View(APIView):
    def get(self,request,*args,**kwargs):
        # roles = Role.objects.all()
        # ser = PagerSerializers(instance=roles,many=True)
        # result = json.dumps(ser.data,ensure_ascii=False)
        # return HttpResponse(result)

        #获取所有数据
        roles = Role.objects.all()
        # ser = PagerSerializers(instance=roles,many=True)
        #创建分页对象
        # pg = MyPageNumberPagination()
        # pg = LimitOffsetPagination()
        # pg = CursorPagination()
        pg = MyPageNumberPagination()
        #在数据库中获取分页的数据
        pager_roles = pg.paginate_queryset(queryset=roles,request=request,view=self)
        #对数据进行序列化
        ser = PagerSerializers(instance=pager_roles,many=True)
        # print(pager_roles)
        # return Response(ser.data)
        return pg.get_paginated_response(ser.data)


from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import GenericViewSet

class View1View(GenericAPIView):
    queryset = Role.objects.all()
    serializer_class = PagerSerializers
    pagination_class = PageNumberPagination
    def get(self,request,*args,**kwargs):
        #获取数据
        roles = self.get_queryset()
        #分页
        pager_roles = self.paginate_queryset(roles)
        #序列化
        ser = self.get_serializer(instance=pager_roles,many=True)
        return Response(ser.data)

class View2View(GenericViewSet):
    queryset = Role.objects.all()
    serializer_class = PagerSerializers
    pagination_class = PageNumberPagination

    def list(self, request, *args, **kwargs):
        # 获取数据
        roles = self.get_queryset()
        # 分页
        pager_roles = self.paginate_queryset(roles)
        # 序列化
        ser = self.get_serializer(instance=pager_roles, many=True)
        return Response(ser.data)

from rest_framework.viewsets import ModelViewSet
from rest_framework.mixins import ListModelMixin,CreateModelMixin

class View4View(ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = PagerSerializers
    pagination_class = PageNumberPagination



from rest_framework.renderers import JSONRenderer,BrowsableAPIRenderer,AdminRenderer,HTMLFormRenderer
class TestView(APIView):
    # renderer_classes = [JSONRenderer,BrowsableAPIRenderer]
    def get(self,request,*args,**kwargs):
        # 获取所有数据
        roles = Role.objects.all()
        pg = MyPageNumberPagination()
        # 在数据库中获取分页的数据
        pager_roles = pg.paginate_queryset(queryset=roles, request=request, view=self)
        # 对数据进行序列化
        ser = PagerSerializers(instance=pager_roles, many=True)
        return Response(ser.data)
        # return pg.get_paginated_response(ser.data)