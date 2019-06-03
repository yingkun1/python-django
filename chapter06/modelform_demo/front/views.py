from django.shortcuts import render
from .forms import AddBookForm,RegisterForm
from .models import Book,User
from django.http import HttpResponse
from django.views.decorators.http import require_POST

def index(request):
    pass

def add_book(request):
    form = AddBookForm(request.POST)
    if form.is_valid():
        # title = form.cleaned_data.get('title')
        # page = form.cleaned_data.get('page')
        # price = form.cleaned_data.get('price')
        # print("title:%s"%title)
        # print("page:%s"%page)
        # book = Book.objects.create(title=title,page=page,price=price)
        # return HttpResponse("添加图书成功")
        form.save()
        return HttpResponse("success")
    else:
        print(form.errors.get_json_data())
        return HttpResponse("FAIL")

@require_POST
def register(request):
    form = RegisterForm(require_POST)
    if form.is_valid():
        user = form.save(commit=False)
        user.password = form.cleaned_data.get('pwd1')
        user.save()
        return HttpResponse("success")
    else:
        print(form.errors.get_json_data())
        return HttpResponse("fail")
