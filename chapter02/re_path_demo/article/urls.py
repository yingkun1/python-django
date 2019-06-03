from django.urls import re_path
from . import views

urlpatterns = [
    #r"":代表的是原生字符串(raw)
    re_path(r"^$",views.article),
    #/article/list/<year>/
    re_path(r"^list/(?P<year>\d{4})/$",views.artucle_list),
    #/article/list/<month>/
    re_path(r"^list/(?P<month>\d{2})/$",views.article_list_month),
]