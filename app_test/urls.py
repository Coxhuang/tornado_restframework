# -*- coding: utf-8 -*-
"""
@Time ： 2020/5/16 19:05
@Auth ： Minhang
@File ：urls.py
@IDE  ：PyCharm
"""

from app_test.api_layer.test.test_views import TestHandler


urlpatterns = [
    ("Test","/demo1/",TestHandler),
    ("Test","/demo2/",TestHandler),
]