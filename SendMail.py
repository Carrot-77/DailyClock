#!/usr/bin/env python
# coding=utf-8


from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.utils import parseaddr, formataddr

import smtplib
import time
import json

def _format_addr(s):  #用于格式化一个邮件地址，使其变为
    name, addr = parseaddr(s)  
    return formataddr((Header(name, 'utf-8').encode(), addr))

def get_user(filename):
        with open(filename, "r") as f:
            data = json.load(f)
        return data

class SendMail:
    def __init__(self):
        send_user = get_user("/home/carrot/DailyClock/data/mail.json")
        self.from_addr = send_user[0]['user']  #输入发件人Email地址
        password = send_user[0]['passwd']  #密码
        
        # SMTP邮箱服务器
        smtp_server = 'smtp.qq.com'
        
        email_info = '平安行动打卡脚本崩了，绝对是学校的问题，今天记得手动打卡QAQ'
        self.msg = MIMEText(email_info, 'plain', 'utf-8')
        
        self.msg['From'] = _format_addr('DailyClock <%s>' % self.from_addr) 
        self.msg['Subject'] = Header('DailyClock', 'utf-8').encode()
        
        self.server = smtplib.SMTP(smtp_server, 587) #开了端口587
        # server.set_debuglevel(1)  #打印出和SMTP服务器交互的所有信息
        self.server.login(self.from_addr, password)  #登录
    
    def sendmail(self, to_addr):
        self.msg['To'] = _format_addr('Receive <%s>' % to_addr)
        self.server.sendmail(self.from_addr, [to_addr], self.msg.as_string()) 
        #第二个变量可以传入一个list发送给多个人，第三个变量是一个str类型的邮件正文
        
    def destroy(self):
        self.server.quit()


if __name__ == '__main__':
    sm = SendMail()
    sm.sendmail('1012982871@qq.com')
    sm.destroy()
