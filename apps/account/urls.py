# -*- coding: utf-8 -*-  
# __author__:ZHANGJIN
# __time__:2019/1/17 20:30
from django.conf.urls import url

from apps.account import views

urlpatterns = [
    url('login/', views.login_view, name='login'),
    url('register/', views.login_view, name='register'),
    url('logout/', views.login_view, name='logout'),
    url('logout/', views.login_view, name='logout'),
    url('active/', views.active_account, name='active'),
    url('update/', views.update_view, name='update')
]
