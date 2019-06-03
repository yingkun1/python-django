from django.urls import path
from . import views
app_name = "errors"

urlpatterns=[
    path('405.html',views.view_405,name='405'),
    path('403.html',views.view_403,name='403'),
]