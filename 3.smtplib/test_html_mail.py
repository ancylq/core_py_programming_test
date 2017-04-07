#!/usr/bin/env python
# coding:utf-8

import smtplib
from email.mime.text import MIMEText

mailto_list = ['ancylq@163.com']
mail_from = 'xiaoqianqianwx@163.com'
mail_host = 'smtp.163.com'
mail_user = 'xiaoqianqianwx@163.com'
mail_pass = 'lq2006.SHE'

def send_mail(sub, content):
    msg = MIMEText(content, _subtype='plain', _charset='utf-8') # _subtype='html'
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
