#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @分享者  : 小强测试品牌 (xqtesting@qq.com)
# @官网    : http://www.xqtesting.com
# @博客	: http://www.xqtesting.com/blog.html
# @微信公众号	: 测试帮日记


'''
关联参数的讲解示例

场景如下：
模拟login2接口的响应
关联响应中的checkstatus参数
模拟book_info接口的请求
把关联到的checkstatus参数扔到请求里
'''


#模拟login2接口的响应数据
response = {"error_code": 0, "reason": "successed", "username": "xiaoqiang", "checkstatus": "on"}

#模拟关联格式，就是excel中的，如果有多个就用分号隔开
correlation = '${checkstatus}=[checkstatus]'

#字典，为后续保存数据做准备
correlationDict = {}

#去掉多余的回车换行，如果有多个关联参数则用分号隔开
correlation = correlation.replace('\n','').replace('\r','').split(';')
print("关联公式=",correlation)


for j in range(len(correlation)):
    #根据=把关联数据拆分
    param = correlation[j].split('=')
    print("param=",param)
    print("param[0]=",param[0])
    print("param[1]=", param[1])
    if len(param)==2:
        '''
        我们关注第二个元素，需要把他取出来（因为他就是我们需要的响应数据）
        从下标1开始到末尾
        那为什么后面还有split呢？看下这样的数据
        ${date}=[result][yangli]
        '''
        for key in param[1][1:-1].split(']['):
            print("key=",key)
            temp = response[key]
            print("temp=",temp)
            #因为中间处理的时候数据会有变化，所以在给一个新的值存储
            response = temp
            print('response=',response)

        #关联到的响应放到字典里，方便后续去遍历替换参数
        correlationDict[param[0]] = response
        print("correlationDict[param[0]]=", response)

    else:
        print("error")


print('最终关联的值=',correlationDict)



#模拟book_info接口的请求数据，就是excel里的
request_data = {"bookname": "小强软件测试疯狂讲义", "checkstatus": "${checkstatus}"}
request_data=str(request_data)

#在request_data中查找是否存在需要关联的数据
for keyword in correlationDict:
    #str类型才有find方法，所以在上面做了类型转换
    if request_data.find(keyword) > 0:
        request_data = (request_data.replace(keyword,str(correlationDict[keyword])))

print('最终请求数据',request_data)




'''
调通之后放到run_testcase.py的相应位置即可。
特别需要注意顺序，因为进行下一个请求之前要先替换关联的参数的
for循环找请求中否存在需要关联的数据，如果有则替换>interface_test>关联参数拆分
'''

