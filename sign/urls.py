# -*- coding: utf-8 -*-
# @Time    : 17-10-24 下午9:41
# @Author  : shitouBoy
# @Email   : xy960722@gmail.com
# @File    : urls.py
# @Describe:
# @Software: PyCharm
from django.conf.urls import url
from sign import views_if

urlpatterns =[
    url(r'^add_event/', views_if.add_event,name='add_event')
]
