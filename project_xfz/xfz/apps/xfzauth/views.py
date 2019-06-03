from django.contrib.auth import login,logout,authenticate
from django.views.decorators.http import require_POST
from .forms import LoginForm,RegisterForm
from django.http import JsonResponse,HttpResponse
from utils import restful
from django.shortcuts import redirect,reverse
from utils.captcha.xfzcaptcha_test import Captcha
from io import BytesIO
from utils.aliyunsdk import aliyunsms
from django.core.cache import cache
from django.contrib.auth import get_user_model
from .models import User
from django.views.decorators.csrf import csrf_exempt

#一般我是这样去设计的
@require_POST
@csrf_exempt
def login_view(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        telephone = form.cleaned_data.get('telephone')
        password = form.cleaned_data.get('password')
        remember = form.cleaned_data.get('remember')
        user = authenticate(request,username=telephone,password=password)
        if user:
            if user.is_active:
                login(request,user)
                if remember:
                    request.session.set_expiry(None)
                else:
                    request.session.set_expiry(0)
                return restful.result()
            else:
                return restful.unauth_errors(message="您的账号已经被冻结了!")
        else:
            return restful.params_errors(message="手机号码或者密码错误!")
    else:
        errors = form.get_errors()
        return restful.params_errors(message=errors)

@require_POST
def register(request):
    form = RegisterForm(request.POST)
    if form.is_valid():
        telephone = form.cleaned_data.get('telephone')
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = User.object.create_user(username=username,telephone=telephone,password=password)
        login(request,user)
        return restful.ok()
    else:
        return restful.params_errors(message=form.get_errors())

def logout_view(request):
    logout(request)
    return redirect(reverse('index'))

def img_captcha(request):
    text,image = Captcha.gene_code()
    #BytesIO:相当于一个管道，用来存储图片的流数据
    out = BytesIO()
    #调用image的save方法，将这个image对象保存到BytesIO中
    image.save(out,'png')
    #将BytesIO的文件指针移动到最开始的位置
    out.seek(0)
    response = HttpResponse(content_type='image/png')
    #从BytesIO的管道中，读取出图片数据，保存到response的对象上
    response.write(out.read())
    response['Content-length'] = out.tell()
    cache.set(text.lower(),text.lower(),5*60)
    return response

def sms_captcha(request):
    telephone = request.GET.get('telephone')
    code = Captcha.gene_text()
    # cache.set(telephone,"8888",5*60)
    cache.set(telephone,code,5*60)
    print('短信验证码:',code)
    # result = aliyunsms.send_sms('telephone','code')
    # print(result)
    return restful.ok()

def cache_test(request):
    cache.set('username','8888',60)
    result = cache.get('username')
    print(result)
    return HttpResponse("success")


