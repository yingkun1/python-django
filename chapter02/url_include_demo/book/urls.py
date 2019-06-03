from django.urls import path
from . import views

# app_name = 'book'

urlpatterns = [
    #book/
    path('',views.book),
    path('detail/<book_id>/',views.book_detail),
    path('list/',views.book_list)
]