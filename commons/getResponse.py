import requests
import json
'''
requests模块中，r.json()为Requests中内置的JSON解码器
其中只有response返回为json格式时，用r.json()打印出响应的内容，
如果response返回不为json格式，使用r.json()会报错

例如
if status_code==200:
            self.assertEqual('successed', json_r['reason'], "是状态吗")
'''

class HttpRequestResponse:
    def get(self, url, params=None, headers=None):
        print('GET请求url--', url)
        print('GET请求参数--', params)
        try:
            r = requests.get(url, params=params, headers=headers)
            status_code=r.status_code
            print('GET响应状态码--', status_code)
            json_r = r.json()
            print('GET响应结果--', json_r)
            time=r.elapsed.total_seconds()
            print('GET响应时间--',time)
            return json_r,status_code,time
        except Exception as e:
            print('GET请求报错--', e)

    def post_form(self, url, data, headers=None):
        print('POST_FORM请求url--', url)
        print('POST_FORM请求参数--', data)
        try:
            r = requests.post(url, data=data, headers=headers)
            status_code=r.status_code
            print('POST_FORM响应状态码--', status_code)
            json_r = r.json()
            print('POST_FORM响应结果--', json_r)
            time=r.elapsed.total_seconds()
            print('POST_FORM响应时间--',time)
            return json_r,status_code,time
        except Exception as e:
            print('POST_FORM请求报错--', e)

    def post_json(self, url, data, headers=None):
        print('POST_JSON请求url--', url)
        print('POST_JSON请求参数--', data)
        try:
            r = requests.post(url, json=data, headers=headers)
            status_code=r.status_code
            print('POST_JSON响应状态码--', status_code)
            json_r = r.json()
            print('POST_JSON响应结果--', json_r)
            time=r.elapsed.total_seconds()
            print('POST_JSON响应时间--',time)
            return json_r,status_code,time
        except Exception as e:
            print('POST_JSON请求报错--', e)
'''
# get
new_get = HttpRequestResponse()
url = 'http://localhost:12306/book_info'
params = {
    "bookname": "接口来自moco",
    "checkstatus": "on"
}
get_json = new_get.get(url, params=params)
print("get_json---", get_json)

# post_form
newForm = HttpRequestResponse()
url = "http://localhost:12306/login1"
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}
data = {
    "username": "xiaoming",
    "pwd": "123456"
}
form_json=newForm.post_form(url,data=data,headers=headers)
print("form_json---",form_json)

#post_json
newJson = HttpRequestResponse()
url = "http://localhost:12306/login2"
headers = {
    "Content-Type": "application/json"
}
data = {
    "username": "xiaoqiang",
    "pwd": "123456"
}
json_json=newJson.post_json(url,data,headers)
print("json_json---",json_json)






 def test_m4(self):
        import sys
        sys.path.append('..')
        from tools.getResponse import HttpRequestResponse

        # get
        new_get = HttpRequestResponse()
        url = 'http://localhost:12306/book_info'
        params = {
            "bookname": "接口来自moco",
            "checkstatus": "on"
        }
        get_json = new_get.get(url, params=params)
        print("get_json---", get_json)
        self.assertEqual('successed',get_json['reason'],"是状态吗")


'''