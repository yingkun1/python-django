from django.http import HttpResponse
from django.core.cache import cache
from django.core.cache.backends.memcached import MemcachedCache

def index(request):
    cache.set("password1","yingkun",100)
    username1 = cache.get("username1")
    print(username1)
    return HttpResponse('index')