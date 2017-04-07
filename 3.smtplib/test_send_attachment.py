#!/usr/bin/env python
# coding:utf-8

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

mailto_list = ['ancylq@163.com']
mail_from = 'xiaoqianqianwx@163.com'
mail_host = 'smtp.163.com'
mail_user = 'xiaoqianqianwx@163.com'
mail_pass = 'lq2006.SHE'

def send_mail(sub, content):
    
    # 创建一个带附件的实例
    msg = MIMEMultipart()
    
    # 构造附件，多个附件就多个构造附件
    att1 = MIMEText(open('./attachment.txt', 'rb').read(), 'base64', 'gb2312')
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = u'attachment; filename="人员名单.txt"'.encode('gb2312')#这里的filename可以任意写，写什么名字，邮件中显示什么名字
    msg.attach(att1)
    
    content = MIMEText(u'附件中，请查收', 'plain', 'gb2312')
    msg.attach(content)
    
    msg['Subject'] = sub
    msg['From'] = mail_from
    msg['To'] = ','.join(mailto_list)
    try:
        server = smtplib.SMTP()
        server.connect(mail_host)
        server.login(mail_user, mail_pass)
        print msg.as_string()
        server.sendmail(mail_from, mailto_list, msg.as_string())
        server.close()
        return True
    except Exception as e:
        print e
        return False
    
if __name__ == '__main__':
    if send_mail('开会', 'this is a test email'): # send_mail('hello', '<h1>this is a test mail </h1>')
        print '发送成功'
