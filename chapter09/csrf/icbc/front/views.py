from django.shortcuts import render,redirect,reverse
from django.views.generic import View
from .forms import RegisterForm,LoginForm,TransferForm
from .models import User
from django.db.models import F
from django.http import HttpResponse
from .decorators import login_required
from django.utils.decorators import method_decorator

def index(request):
    return render(request,"index.html")

class LoginView(View):
    def get(self,request):
        return render(request,"login.html")

    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            front_user = User.objects.filter(email=email,password=password).first()
            if front_user:
                request.session['user_id'] = front_user.pk
                return redirect(reverse('index'))
            else:
                print("用户名或者密码错误")
                return redirect(reverse('login'))
        else:
            print(form.errors.get_json_data())

class RegisterView(View):
    def get(self,request):
        return render(request,"register.html")

    def post(self,request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            User.objects.create(email=email,username=username,password=password,balance=1000)
            return redirect(reverse('login'))
        else:
            print(form.errors.get_json_data())
            return redirect(reverse('register'))

@method_decorator(login_required,name='dispatch')
class TransferView(View):
    def get(self,request):
        return render(request,"transfer.html")

    def post(self,request):
        form = TransferForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            money = form.cleaned_data.get('money')
            # to_user = User.objects.get(email=email)
            user = request.front_user
            if user.balance >= money:
                user.balance-=money
                # to_user.balance+=money
                User.objects.filter(email=email).update(balance=F('balance')+money)
                user.save()
                return HttpResponse("转账成功!")
            else:
                return HttpResponse("余额不足!")
        else:
            print(form.errors.get_json_data())
            return redirect(reverse('transfer'))

def logout(request):
    request.session.flush()
    return redirect(reverse('index'))