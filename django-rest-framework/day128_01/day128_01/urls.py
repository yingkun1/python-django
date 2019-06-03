"""day128_01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/',views.users,name="users"),
    path('students/',views.StudentView.as_view(),name="students"),
    # path('add_order/',views.add_order,name="add_order"),
    # path('get_order/',views.get_order,name="get_order"),
    # path('delete_order/',views.delete_order,name="delete_order"),
    # path('update_order/',views.update_order,name="update_order"),
    # path('order/',views.order,name="order"),
    # path('order/',views.OrderView.as_view(),name="order"),
    path('dog/',views.DogView.as_view(),name="dog"),
]
