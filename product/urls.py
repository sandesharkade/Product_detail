from django.conf.urls import url,include
from . import views
from django.contrib import admin
from .views import Product_detail,Product_list,Product_edit,Product_save,Logout
from django.contrib.auth.decorators import login_required

app_name='product'

urlpatterns=[
    url(r'^$',login_required(Product_list.as_view()),name='product_list'),
    url(r'^(?P<pk>\d+)/$',login_required(Product_detail.as_view()),name='product_detail'),
    url(r'^new/$',login_required(Product_save.as_view()),name='product_save'),
    url(r'^(?P<pk>\d+)/edit/$',login_required(Product_edit.as_view()),name='product_edit'),
    url(r'^logout$',Logout.as_view(),name='logout'),
]
