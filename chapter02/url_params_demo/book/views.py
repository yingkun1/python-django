from django.http import HttpResponse

def book(request):
    return HttpResponse("图书首页")

def book_deatil(request,book_id,category_id):
    #可以从数据库中根据book_id提取这个图书的信息
    text = "您获取的图书id是:%s,图书分类是:%s" % (book_id,category_id)
    return HttpResponse(text)

def book_author(request):
    author_id = request.GET.get('id')
    text = "作者的id:%s" % author_id
    return HttpResponse(text)

def publisher_detail(request,publisher_id):
    text = "出版社的id是:%s" % publisher_id
    return HttpResponse(text)

