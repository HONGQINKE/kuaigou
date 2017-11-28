import os 
import unittest
from datetime import datetime
from HTMLTestRunner import HTMLTestRunner
import sys

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

sys.path.append('./db_fixture')
from db_fixture import test_data

def new_file(test_dir):
    lists = os.listdir(test_dir)
    lists.sort(key=lambda fn:os.path.getmtime(test_dir+'/'+fn))
    file_path = os.path.join(test_dir,lists[-1])
    return file_path

def send_email(newfile):
    f=open(newfile,'rb')
    mail_body = f.read()
    f.close()

    smtpserver = 'smtp.qq.com'
    user = '815653824@qq.com'
    password = 'ppzrtqqgiauabbff'
    sender = '815653824@qq.com'
    receiver = ['815653824@qq.com']
    subject = 'Auto Test Report From Liuhong'
   
    msg = MIMEMultipart('mixed')
     
    msg_html1 = MIMEText(mail_body,'html','utf-8')
    msg.attach(msg_html1)
    msg_html = MIMEText(mail_body,'html','utf-8')
    msg_html["Content-Disposition"] = 'attachment;filename="TestReport.html"'
    msg.attach(msg_html)
  
    msg['From'] = '815653824@qq.com'
    msg['To'] = ";".join(receiver)
    msg['Subject']=Header(subject,'utf-8')

    #连接发送邮件
    try:
        smtp=smtplib.SMTP_SSL()
        smtp.connect(smtpserver,465)
        smtp.login(user, password)
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()
        return True
        print("send success")
    except Exception:
        print('failed ')

if __name__ == '__main__':
    print('====AutoTest Start====')
    
    #test_data.init_data()
    #test_data.init_datab()
    test_dir = './test_case'
    test_report_dir = './report'

    discover = unittest.defaultTestLoader.discover(test_dir,pattern='*_test.py')
    now = datetime.now().strftime('%Y-%m-%d_%H_%M_%S_')
    filename = test_report_dir + '/' + now + 'result.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream=fp,title='KuaiGou Test Report',description='Result')
    runner.run(discover)
    fp.close()
    
    new_report = new_file(test_report_dir)
    print(new_report)

    send_email(new_report)

    print('====AutoTest Over====')


