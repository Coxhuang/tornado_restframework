# -*- coding: utf-8 -*-
"""
@Time ： 2020/5/16 19:07
@Auth ： Minhang
@File ：url.py
@IDE  ：PyCharm
"""

from urls import urlpatterns


class MyUrlsPath(object):

    def __init__(self):
        pass

    def register_url(self):
        """
        注册url
        :return: url list
        """
        ret_list = []
        for app_url_list in urlpatterns:
            app_url = app_url_list[1]
            api_url_urlpatterns = app_url_list[2].urlpatterns
            for api_url_list in api_url_urlpatterns:
                api_url = api_url_list[1]
                api_view = api_url_list[2]

                if app_url[-1] == "/":
                    pass
                else:
                    app_url += "/"
                if api_url[0] == "/":
                    api_url = api_url[1::]

                ret_list.append((app_url+api_url,api_view))

        return ret_list

url_obj = MyUrlsPath()