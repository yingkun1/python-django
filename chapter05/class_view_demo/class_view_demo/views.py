from django.http import HttpResponse
from django.views.generic import View,TemplateView
from django.shortcuts import render,reverse

def index(request):
    return HttpResponse("success")

class BookListView(View):
    def get(self,request,*args,**kwargs):
        return HttpResponse("book list view")

class AddBookView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"add_book.html")

    def post(self,request,*args,**kargs):
        book_name = request.POST.get("name")
        book_author = request.POST.get("author")
        # print("name:{},author:{}".format(book_name,book_author))
        print("name:%s,author:%s"%(book_name,book_author))
        return HttpResponse("success")

class BookDetailView(View):
    def get(self,request,book_id):
        print("图书的id是:%s"%book_id)
        return HttpResponse("success")

    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponse("不支持GET以外的其他请求!")

    def dispatch(self, request, *args, **kwargs):
        print('dispatch')
        return super(BookDetailView, self).dispatch(request,*args,**kwargs)

class AboutView(TemplateView):
    template_name = "about.html"
    def get_context_data(self, **kwargs):
        context = {
            "phone":"0731-888888",
        }
        return context