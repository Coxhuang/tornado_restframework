# -*- coding: utf-8 -*-
"""
@Time ： 2020/5/16 18:11
@Auth ： Minhang
@File ：tornado_restframework.py
@IDE  ：PyCharm
"""

import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
from tornado.options import define, options
from utils.common.urls.url import url_obj
from urllib.parse import urljoin

define("port", default=8000, type=int)  # 设置一个监听地址,全局变量

if __name__ == "__main__":
    tornado.options.parse_command_line() # 允许命令行启动程序
    print(url_obj.register_url())
    app = tornado.web.Application(
        url_obj.register_url(),
        websocket_ping_interval = 3, # WebSocket ping探活包发送间隔秒数
        websocket_ping_timeout=10,
        debug = True,
        )
    http_server = tornado.httpserver.HTTPServer(app) # 将应用处理逻辑 传递给HTTPServer 服务
    http_server.listen(options.port)  # 配置监听地址到 HTTPServe
    tornado.ioloop.IOLoop.current().start() # 启动应用




