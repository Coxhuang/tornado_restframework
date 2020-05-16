# -*- coding: utf-8 -*-
"""
@Time ： 2020/5/16 18:16
@Auth ： Minhang
@File ：urls.py
@IDE  ：PyCharm
"""
from app_test import urls as test_urls

urlpatterns = [
    ("Test","/api/test/",test_urls),
]
