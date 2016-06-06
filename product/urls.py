from django.conf.urls import url,include
from . import views
from django.contrib import admin

urlpatterns=[

    url(r'^$',views.product_list,name='product_list'),
    url(r'^product/new/$',views.product_save,name='product_save'),
    url(r'^product/(?P<pk>\d+)/$', views.product_detail, name='product_detail'),
    url(r'^product/(?P<pk>\d+)/edit/$',views.product_edit,name='product_edit')
    ]
