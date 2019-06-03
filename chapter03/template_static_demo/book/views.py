from django.shortcuts import render

def book(request):
    return render(request,"book.html")
