from django.shortcuts import render

def index(request):
    context = {
        "persons":[
            "张三",
            "李四",
            "王五",
        ]
    }
    return render(request,"index.html",context=context)