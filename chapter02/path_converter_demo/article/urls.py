from django.urls import re_path,path
from . import views

urlpatterns = [
    path('',views.article),
    path('list/<cate:categories>/',views.article_list,name="list"),
    #\w:0-9,a-z,A-Z,_
    # re_path(r'list/(?P<categories>\w+|(\w+\+\w+)+)/',views.article_list),
    path('detail/<int:article_id>',views.article_detail,name='detail'),
]