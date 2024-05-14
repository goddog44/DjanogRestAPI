# from django.conf.urls import url
# from APIrest import views

# urlpatterns=[
#     url(r'^department$',views.departmentAPI),
#     url(r'^department/([0-9]+)$')

# ]
from django.urls import re_path
from APIrest import views

urlpatterns = [
    re_path(r'^department/$', views.departmentAPI),
    re_path(r'^department/([0-9]+)/$', views.departmentAPI),
]
