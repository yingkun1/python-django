from django.http import HttpResponse

def book(request):
    return HttpResponse("图书首页")

def book_detail(request,book_id):
    text = "图书的id是:%s" % book_id
    return HttpResponse(text)

def book_list(request):
    return HttpResponse("图书列表页面")
