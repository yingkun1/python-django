from django.urls import path,re_path,include
from api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'xxxxx',views.View4View)

urlpatterns = [
    # path('users/',views.UsersView.as_view(),name="users"),
    re_path(r"^(?P<version>[v1|v2]+)/users/$",views.UsersView.as_view(),name="users"),
    re_path(r"^(?P<version>[v1|v2]+)/django/$", views.DjangoView.as_view(), name="django"),
    re_path(r"^(?P<version>[v1|v2]+)/parser/$", views.ParserView.as_view(), name="parser"),
    re_path(r"^(?P<version>[v1|v2]+)/roles/$", views.RolesView.as_view(), name="roles"),
    re_path(r"^(?P<version>[v1|v2]+)/userinfo/$", views.UserInfoView.as_view(), name="userinfo"),
    re_path(r"^(?P<version>[v1|v2]+)/group/(?P<pk>\d+)$", views.GroupView.as_view(), name="group"),
    re_path(r"^(?P<version>[v1|v2]+)/usergroup/$", views.UserGroupView.as_view(), name="usergroup"),
    re_path(r"^(?P<version>[v1|v2]+)/pager1/$", views.Pager1View.as_view(), name="pager1"),
    re_path(r"^(?P<version>[v1|v2]+)/view1/$", views.View1View.as_view(), name="view1"),
    re_path(r"^(?P<version>[v1|v2]+)/view2/$", views.View2View.as_view({'get':'list'}), name="view2"),
    re_path(r"^(?P<version>[v1|v2]+)/view2\.(?P<format>\w+)/$", views.View2View.as_view({'get':'list'}), name="view2"),
    # re_path(r"^(?P<version>[v1|v2]+)/view3/$", views.View3View.as_view({'get':'list','post':'create'}), name="view3"),
    re_path(r"^(?P<version>[v1|v2]+)/view4/(?P<pk>\d+)/$", views.View4View.as_view({'get':'retrieve','delete':'destroy','put':'update','patch':'partial_update'})),
    re_path(r"^(?P<version>[v1|v2]+)/view4/(?P<pk>\d+)\.(?P<format>\w+)/$", views.View4View.as_view({'get':'retrieve','delete':'destroy','put':'update','patch':'partial_update'})),
    re_path(r'^(?P<version>[v1|v2]+)/',include(router.urls)),
    re_path(r"^(?P<version>[v1|v2]+)/test/$",views.TestView.as_view(),name="test"),
]