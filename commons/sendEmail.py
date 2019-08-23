# email
from email.mime.application import MIMEApplication
import email.mime.text
import email.mime.multipart

import smtplib
import base64


# 引入相关模块，主要是处理发送邮件和附件的
# 类


class SendMail:
    def send_mail(self, from1, to, title, content, type='plain', attach=None, pic=None):
        # 生成包含多个邮件体的对象
        msg = email.mime.multipart.MIMEMultipart()
        msg['from'] = from1
        msg['to'] = to
        msg['subject'] = title
        # 邮件正文
        txt = email.mime.text.MIMEText(content, type)
        msg.attach(txt)

        # 文件附件
        if attach != None:
            part = MIMEApplication(open(attach, 'rb').read())
            part.add_header('Content-Disposition','attachment', filename=attach)

            msg.attach(part)

        # jpg图片附件
        if pic != None:
            picpart = MIMEApplication(open(pic, 'rb').read())
            picpart.add_header('Content-Disposition', 'attachment', filename=pic)
            msg.attach(picpart)

            #不造说啥了，上面这个发送出去文件查看异常，后来改成了下面这个好了，原来的代码也没毛病了，备用吧
            # from email.mime.text import MIMEText
            # from email.mime.image import MIMEImage   
            # file_pic=open(pic, 'rb')
            # picpart = MIMEImage(file_pic.read())
            # file_pic.close()
            # picpart.add_header('Content-ID', 'imageid')
            # msg.attach(picpart)

        # 发送邮件

        # 连接服务器，SMTP地址+端口
        smtp = smtplib.SMTP('smtp.163.com', '25')
        # 一般这样
        #     帐户:***@163.com
        # POP3服务器：pop.163.com 端口:110
        # SMTP服务器：smtp.163.com 端口:25
        # smtp=smtplib.SMTP_SSL('smtp.qq.com','465')
        # 设置为调试模式，console 中显示
        smtp.set_debuglevel(1)
        # 登录，用户名+密码，密码可能需要填写授权码
        smtp.login('要发送邮箱的用户名', '密码')#邮箱的用户名，密码
        # 发送，from+to+内容
        smtp.sendmail(from1, to, str(msg))
        # 退出
        smtp.quit()


# 设置变量并调用发送邮件
from1 = '发送出去的邮箱@163.com这里改上面smtp地址也要改，要记得' #发送出去的邮箱
to = '接收的邮箱' #接收的邮箱
# 接收的邮件地址
title = '19-54 title python 全栈自动化测试 文件 行不行 图片'
content = 'content正文 金马奖 金鸡奖 杨天宝'
attach = 'D:\\python_code\\re_Automation\\excel_demo.xlsx'#附件-文件
pic = 'D:\\python_code\\re_Automation\\md_pic\\logging.FileHandler.png'#附件-图片
print('-执行-')

try:
    smtpObj = SendMail()
    smtpObj.send_mail(from1, to, title, content, type='plain', attach=attach, pic=pic)
    print("邮件发送成功")
except smtplib.SMTPException as ex:
    print("Error: 无法发送邮件",ex)