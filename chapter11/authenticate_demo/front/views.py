from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# from .models import Person
from .models import User
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from .forms import LoginForm
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth.models import Permission,ContentType,Group
from .models import Article

def index(request):
    #创建普通用户
    # user = User.objects.create_user(username="yingkun",email="925712087@qq.com",password="yingkun9257 ")
    #创建超级用户
    # user = User.objects.create_superuser(username="zhangjie",email="837423959@qq.com",password="zhangjie9257")
    # user = User.objects.get(pk=1)
    #修改密码
    # user.set_password("yingkun8374")
    # user.save()
    #验证用户
    # username = "zhangjie"
    # password = "zhangjie9257"
    # user = authenticate(request,username=username,password=password)
    # print(user)
    # if user:
    #     print("登录成功：%s",user.username)
    # else:
    #     print("登录失败,用户名或者密码错误！")
    # return HttpResponse("success")
    return render(request,"index.html")

# def proxy_view(request):
#     blacklist = Person.get_blacklist()
#     for person in blacklist:
#         print(person.username)
#     return HttpResponse("proxy")

# def my_authenticate(telephone,password):
#     user = User.objects.filter(extension__telephone=telephone).first()
#     if user:
#         is_correct = user.check_password(password)
#         if is_correct:
#             return user
#         else:
#             return None
#     else:
#         return None

# def one_view(request):
    # user = User.objects.create_user(username="zhangtian",email="zhangtian@qq.com",password="zhangtian9257")
    # user = User.objects.create_user(username="zhangliao",email="zhangliao@qq.com",password="zhangliao9257")
    # user.extension.telephone = "17373960306"
    # user.save()
    # telephone = request.GET.get('telephone')
    # password = request.GET.get('password')
    # user = my_authenticate(telephone,password)
    # if user:
    #     print("验证成功:%s"%user.username)
    # else:
    #     print("验证失败!")
    # return HttpResponse("一对一扩展User模型")

def inherit_view(request):
    telephone = "17373962346"
    password = "123456"
    username = "zhiiao1"
    # user = User.objects.create_user(telephone=telephone,password=password,username=username)
    # user = User.objects.create_superuser(telephone=telephone,username=username,password=password)
    # print(user.username)

    # user = authenticate(request,username="17373962346",password="123456")
    # if user:
    #     print("验证成功")
    #     print(user.username)
    # else:
    #     print("验证失败")
    # return HttpResponse("继承AbstractUser扩展用户")

    # User.objects.create_user(telephone="17373961267",password="liuxin9257",username="liuxin")
    user = authenticate(request,username="17373961267",password="liuxin9257")
    if user:
        print(user.username)
        print("验证成功")
    else:
        print("验证失败")
    return HttpResponse("继承AbstractBaseUser扩展用户")

#切记:这里一定不要定义login视图函数
#可以其它的名字
def my_login(request):
    if request.method == "GET":
        return render(request,"login.html")
    else:
        forms = LoginForm(request.POST)
        if forms.is_valid():
            telephone = forms.cleaned_data.get('telephone')
            password = forms.cleaned_data.get('password')
            remeber = forms.cleaned_data.get('remeber')
            user = authenticate(request,username=telephone,password=password)
            if user and user.is_active:
                login(request,user)
                if remeber:
                    #设置为None，表示使用了全局的过期时间
                    request.session.set_expiry(None)
                else:
                    #设置为0，当浏览器关闭的时候就会过期
                    request.session.set_expiry(0)
                next_url = request.GET.get('next')
                if next_url:
                    return redirect(reverse('profile'))
                else:
                    return HttpResponse("登录成功")
            else:
                return HttpResponse("手机号或者密码错误")
        else:
            print(forms.errors.get_json_data())
            return redirect(reverse('login'))

def my_logout(request):
    logout(request)
    return HttpResponse("成功退出登录")

@login_required(login_url='/login/')
def profile(request):
    return HttpResponse("这是个人中心，只有登录了以后才能查看到")

def add_permission(request):
    content_type = ContentType.objects.get_for_model(Article)
    permission = Permission.objects.create(codename='black_article',name='拉黑文章',content_type=content_type)
    return HttpResponse("权限创建成功")

def operate_permission(request):
    user = User.objects.first()
    content_type = ContentType.objects.get_for_model(Article)
    print(content_type)
    permissions = Permission.objects.filter(content_type=content_type)
    for permission in permissions:
        print(permission)
    #一次性添加多个权限
    # user.user_permissions.set(permissions)
    #一次性删除多个权限
    # user.user_permissions.clear()
    #一次性添加一个权限
    user.user_permissions.add(*permissions)
    #一次性移除一个权限
    # user.user_permissions.remove(*permissions)
    #判断是否有某个权限
    if user.has_perm('front.view_article'):
        print("这个用户拥有view_article权限!")
    else:
        print("这个用户没有view_article权限!")
    print(user.get_all_permissions())
    return HttpResponse("success")

@permission_required('front.add_article',login_url='/login/',raise_exception=True)
def add_article(request):
    #1.判断这个用户有没有登录,如果登录了，会返回一个True
    # if request.user.is_authenticated:
    #     print("已经登录的")
    #     if request.user.has_perm('front.add_article'):
    #         return HttpResponse("这是添加文章的界面")
    #     else:
    #         return HttpResponse("您没有访问该页面的权限",status=403)
    # else:
    #     return redirect(reverse('login'))
    return HttpResponse("这是添加文章的界面")

def operate_group(request):
    # group = Group.objects.create(name="运营")
    # content_type = ContentType.objects.get_for_model(Article)
    # permissions = Permission.objects.filter(content_type=content_type)
    # group.permissions.set(permissions)
    # group.save()
    # group = Group.objects.filter(name="运营").first()
    # user = User.objects.first()
    # user.groups.add(group)
    # user.save()
    # user = User.objects.first()
    # permissions = user.get_group_permissions()
    # print(permissions)

    user = User.objects.first()
    if user.has_perms('front.add_article'):
        print("有这个添加文章的权限")
    else:
        print("没有添加文章的权限")
    return HttpResponse("操作分组!")