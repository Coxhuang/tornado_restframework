# -*- coding: utf-8 -*-
"""
@Time ： 2020/5/16 19:07
@Auth ： Minhang
@File ：test_views.py
@IDE  ：PyCharm
"""

import tornado.gen
import tornado.httpserver
import tornado.options
from tornado.web import RequestHandler

class TestHandler(RequestHandler):

    @tornado.gen.coroutine
    def get(self):
        print("协程开始")
        yield self.sleep_5s() # 模拟延迟5秒处理业务代码
        print("协程结束")
        self.write("GET Success")

    def sleep_5s(self):
        import time
        time.sleep(5)
        return None

    def post(self, *args, **kwargs):

        self.write("POST Success")