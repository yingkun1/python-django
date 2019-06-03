from django.shortcuts import render
from datetime import datetime

def index(request):
    context = {
        "value":"张三",
        "mytime":datetime(year=2018,month=9,day=8,hour=12,minute=30,second=20)
    }
    return render(request,"index.html",context=context),

