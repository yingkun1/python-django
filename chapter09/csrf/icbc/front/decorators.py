from .models import User
from django.shortcuts import render,reverse,redirect

def login_required(func):
    def wrapper(request,*args,**kwargs):
        # user_id = request.session.get('user_id')
        # exists = User.objects.filter(id=user_id).exists()
        if request.front_user:
            return func(request,*args,**kwargs)
        else:
            return redirect(reverse('login'))
    return wrapper