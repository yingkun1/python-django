from django.urls import path
from . import views

app_name = "article"

urlpatterns= [
    path('',views.index,name="index"),
    path('delete/',views.delete_view,name="delete"),
    path('one_to_many/',views.one_to_many_view),
    path('one_to_one/',views.one_to_one_view),
    path('many_to_many/',views.many_to_many_view),
]