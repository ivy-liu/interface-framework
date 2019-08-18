
import unittest
import json


import os
import sys

# 相对路径的import
# sys.path.append("../")
# 绝对路径的import
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")
# from common.utils import *
from commons.getResponse import HttpRequestResponse

class MyTest(unittest.TestCase):
    def test_m1(self):
        url = "http://localhost:12306"
        path = "/login1"

        full_url = url+path
        print("POST请求完整url=", full_url)
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {
            "username": "xiaoming",
            "pwd": "123456"
        }

        print("POST请求参数=", data)

        r = requests.post(full_url, data=data, headers=headers)
        print("POST响应状态码=", r.status_code)
        # 'Content-Type': 'application/json; charset=gbk'
        print("POST响应头=", r.headers)
        print("POST响应结果（json类型）=", r.text)
        print("POST接口的响应时间=", r.elapsed.total_seconds(), '秒')
        print('r1-', r)

    def test_m2(self):
        url = "http://localhost:12306"
        path = "/login2"

        full_url = url+path
        print("POST请求完整url=", full_url)
        headers = {
            "Content-Type": "application/json"
        }
        data = {
            "username": "xiaoqiang",
            "pwd": "123456"
        }

        print("POST请求参数=", data)

        r = requests.post(full_url, json=data, headers=headers)
        print("POST响应状态码=", r.status_code)
        # 'Content-Type': 'application/json; charset=gbk'
        print("POST响应头=", r.headers)
        print("POST响应结果（json类型）=", r.text)
        print("POST接口的响应时间=", r.elapsed.total_seconds(), '秒')
        print('r2-', r)

    def test_m3(self):
        url = "http://localhost:12306"
        path = "/book_info"

        full_url = url+path
        print("GET请求完整url=", full_url)

        params = {
            "bookname": "接口来自moco",
            "checkstatus": "on"
        }
        print("GET请求参数=", params)

        # 以json形式提交要写，不写默认以form形式提交
        headers = {}

        r = requests.get(full_url, params=params, headers=headers)
        print("GET响应状态码=", r.status_code)
        print('r3-', r)

    def test_m4(self):

        # get
        new_get = HttpRequestResponse()
        url = 'http://localhost:12306/book_info'
        params = {
            "bookname": "接口来自moco",
            "checkstatus": "on"
        }
        get_json = new_get.get(url, params=params)
        print("get_json---", get_json)
        self.assertEqual('successed', get_json['reason'], "是状态吗")
