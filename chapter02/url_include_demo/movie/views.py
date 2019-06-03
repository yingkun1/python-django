from django.http import HttpResponse

def movie(request):
    return HttpResponse("电影首页")

def movie_list(request):
    return HttpResponse("电影列表页")