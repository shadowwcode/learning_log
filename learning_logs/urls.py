# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
 定义 learning_logs 的URL模式
"""
from django.conf.urls import url

from . import views

urlpatterns = [
    # 主页
    url(r'^$', views.index, name='index'),
]
