from django.shortcuts import render,render_to_response
from django.template.loader import render_to_string
from django.http import HttpResponse

def index(request):
    # html = render_to_string("index.html")
    # return HttpResponse(html)
    return render(request,'index.html')