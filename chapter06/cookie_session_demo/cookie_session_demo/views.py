from django.http import HttpResponse
from datetime import datetime
from django.utils.timezone import make_aware

def index(request):
    response = HttpResponse("index")
    expires = datetime(year=2019,month=3,day=23,hour=13,minute=20,second=20)
    expires = make_aware(expires)
    response.set_cookie('user_id','abc',expires=expires,path='/cms/')
    return response

def my_list(request):
    cookie = request.COOKIES
    username = cookie.get('user_id')
    return HttpResponse(username)

def cms_view(request):
    cookie = request.COOKIES
    user_id = cookie.get('user_id')
    return HttpResponse(user_id)

def delete(request):
    response = HttpResponse("delete")
    response.delete_cookie('user_id')
    return response

def session_view(request):
    #1、在session中设置数据
    request.session['username'] = 'zhiliao '
    # request.session['userid'] = 10
    #2、从session中获取值
    # username = request.session.get('username')
    #3、使用pop，从session中删除值
    # username = request.session.pop('username')
    # print(username)
    #4、清除session中的值
    # request.session.clear()
    #5、清除数据库中的sessionid，session值，以及expire_data
    # request.session.flush()
    #6、设置过期时间
    # request.session.set_expiry(120)
    # request.session.set_expiry(0)
    # request.session.set_expiry(None)
    # request.session.set_expiry(-1)
    #7、清除已经过期的session
    # request.session.clear_expired()
    #也可以使用manage.py clearsession的方式实现
    return HttpResponse("session view")