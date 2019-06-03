from django.shortcuts import render

def index(request):
    context = {
        "username":"zhiliao",
    }
    return render(request,"index.html",context=context)

def conpany(request):
    return render(request,"company.html")

def school(request):
    return render(request,"school.html")