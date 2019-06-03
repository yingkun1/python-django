from django.shortcuts import render
from django.middleware.clickjacking import XFrameOptionsMiddleware

def index(request):
    return render(request,"index.html")