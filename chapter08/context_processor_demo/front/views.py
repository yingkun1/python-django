from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.views.generic import View
from .forms import SignupForm,SigninForm
from .models import User
from django.template.context_processors import debug
from django.contrib.auth.context_processors import auth
from django.contrib import messages
# from django.contrib.messages.context_processors import messages

def index(request):
    # user_id = request.session.get('user_id')
    # context = {}
    # try:
    #     user = User.objects.get(pk=user_id)
    #     context['front_user'] = user
    # except:
    #     pass
    users = User.objects.all()
    for user in users:
        print(user)
    return render(request,"index.html")
    # return render(request,"index.html")

class SigninView(View):
    def get(self,request):
        return render(request,"signin.html")

    def post(self,request):
        form = SigninForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # exists = User.objects.filter(username=username,password=password).exists()
            user = User.objects.filter(username=username,password=password).first()
            if user:
                request.session['user_id'] = user.id
                return redirect(reverse('index'))
            else:
                print("用户名或者密码不正确，请重新输入")
                # messages.add_message(request,messages.INFO,"用户名或者密码不正确，请重新输入!")
                messages.info(request,"用户名或者密码不正确，请重新输入!")
                return redirect(reverse('signin'))
        else:
            # print(form.errors.get_json_data())
            # print(form.get_error())
            errors = form.get_error()
            for error in errors:
                messages.info(request,error)
            return redirect(reverse('signin'))

class SignupView(View):
    def get(self,request):
        return render(request,"signup.html")

    def post(self,request):
         form = SignupForm(request.POST)
         if form.is_valid():
             form.save()
             return redirect(reverse("index"))
         else:
             print(form.get_json_data())
             return redirect(reverse('signup'))

def blog(request):
    return render(request,"blog.html")

def video(request):
    return render(request,"video.html")
