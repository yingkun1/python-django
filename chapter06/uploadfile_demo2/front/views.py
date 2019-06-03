from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from .models import Article
from .forms import ArticleForm

class IndexView(View):
    def get(self,request):
        return render(request,"index.html")

    # def post(self,request):
    #     myfile = request.FILES.get('myfile')
    #     with open("somefile","wb") as fp:
    #         for chunck in myfile.chunks():
    #             fp.write(chunck)
    #     return HttpResponse("success")

    # def post(self,request):
    #     title = request.POST.get('title')
    #     content = request.POST.get('content')
    #     myfile = request.FILES.get('myfile')
    #     Article.objects.create(title=title,content=content,thumbnail=myfile)
    #     return HttpResponse("success")

    def post(self,request):
        form = ArticleForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("success")
        else:
            print(form.errors.get_json_data())
            return HttpResponse("fail")



