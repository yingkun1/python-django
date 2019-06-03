from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse

def index(request):
    username = request.GET.get('username')
    if not username:
        return redirect(reverse("errors:403"))
    return HttpResponse("success")

