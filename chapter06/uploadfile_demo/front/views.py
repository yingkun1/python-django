from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

class IndexView(View):
    def get(self,request):
        return render(request,"index.html")

    def post(self,request):
        myfile = request.FILES.get('myfile')
        with open("somefile","wb") as fp:
            for chunck in myfile.chunks():
                fp.write(chunck)
        return HttpResponse("success")
