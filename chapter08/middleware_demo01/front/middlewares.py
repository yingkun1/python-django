from .models import User
from django.utils.deprecation import MiddlewareMixin
def front_user_middleware(get_response):
    #执行一些初始化的代码
    print("front_user_middleware中间件初始化的代码...")
    def middleware(request):
        print("request到达view之前执行的代码...")
        user_id = request.session.get('user_id')
        if user_id:
            try:
                user = User.objects.get(pk=user_id)
                request.front_user = user
            except:
                request.front_user = None
        else:
            request.front_user = None
        #在这行代码执行之前的代码，是request到达view之前的代码
        response = get_response(request)
        print('response到达浏览器之前执行的代码...')
        #response对象到达浏览器之前执行的代码
        return response

    return middleware

#以类的形式定义中间件
class FrontMiddleWare(object):
    def __init__(self,get_response):
        #执行一些初始化的代码
        print('front_user_middleware中间件初始化代码')
        self.get_response = get_response

    def __call__(self,request):
        print("request到达view之前执行的代码...")
        user_id = request.session.get('user_id')
        if user_id:
            try:
                user = User.objects.get(pk=user_id)
                request.front_user = user
            except:
                request.front_user = None
        else:
            request.front_user = None
        # 在这行代码执行之前的代码，是request到达view之前的代码
        response = self.get_response(request)
        print('response到达浏览器之前执行的代码...')
        # response对象到达浏览器之前执行的代码
        return response

class FrontUserMiddlewareMixin(MiddlewareMixin):
    def __init__(self,get_response):
        #执行一些初始化的代码
        print('front_user_middleware中间件初始化代码')
        super(FrontUserMiddlewareMixin, self).__init__(get_response)

    #这个方法是在request到达view之前调用的
    def process_request(self,request):
        print("request到达view之前执行的代码...")
        user_id = request.session.get('user_id')
        if user_id:
            try:
                user = User.objects.get(pk=user_id)
                request.front_user = user
            except:
                request.front_user = None
        else:
            request.front_user = None

    #这个方法是在response到达浏览器之前调用的
    def process_response(self,request,response):
        print("response到达浏览器之前执行的代码...")
        #一定要返回response
        return response