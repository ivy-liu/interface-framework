

import os
import sys
import unittest
import time
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from src.run_testcase import RunTestCase
from commons.sendEmail import SendMail
testcase_file='testcase\\testcase_study.xlsx'#用例地址

test=RunTestCase()
test.run(testcase_file)
# ${checkstatus}=[checkstatus]

t = time.strftime('%Y-%m-%d',time.localtime())#取年月日




# 设置变量并调用发送邮件
from1 = '发送出去的邮箱@163.com这里改上面smtp地址也要改，要记得' #发送出去的邮箱
to = '接收的邮箱' #接收的邮箱
# 接收的邮件内容
title = t+' 接口测试结果'
content = 'content正文 金马奖 金鸡奖 杨天宝'
# attach = 'D:\\python_code\\re_Automation\\excel_demo.xlsx'#附件-文件
# pic = 'D:\\python_code\\re_Automation\\md_pic\\logging.FileHandler.png'#附件-图片
print('-执行email-')

# try:
#     smtpObj = SendMail()
#     smtpObj.send_mail(from1, to, title, content, type='plain', attach=testcase_file, pic=pic)
#     print("邮件发送成功")
# except smtplib.SMTPException as ex:
#     print("Error: 无法发送邮件",ex)


