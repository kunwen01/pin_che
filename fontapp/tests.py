#!/usr/bin/env python
#-*- coding:utf-8 -*-

from django.test import TestCase

# Create your tests here.
import re
import zmail
from bs4 import BeautifulSoup
from datetime import date

def thirdpartyinfo():
    # 你要执行的任务函数
    server = zmail.server('kunwen01@outlook.com', 'fafentuqiang123')
    # server = zmail.server('godknows561@163.com', 'asdf123',pop_host='pop.163.com')
    # server = zmail.server('1101122765@qq.com', 'jkl;\'12345',smtp_host="smtp.exmail.qq.com",smtp_port=465)


    # Retrieve mail
    # latest_mails = server.get_mails(subject='拼车', start_time=date.today().strftime('%Y-%m-%y 00:00:00'))
    latest_mails = [server.get_latest()]
    print(latest_mails)
    for latest_mail in latest_mails:
        test = latest_mail.get('content_html')
        soup = BeautifulSoup(test[0], "lxml")
        message = soup.find('div', attrs={"dir": "ltr"}).find_all('div')
        print(message)
        str1 = "13\d{9,200}|14[5,7]\d{8,200}|15[0-3,5-9]\d{8,200}|16[6]\d{8,200}|17[0,3,5-8]\d{8,200}|18\d{9,200}|19[8,9]\d{8,200}"
        for m in message:
            m_str = m.get_text()
            phone_list = re.findall(str1, m_str)
            print(m_str)
    # return latest_mails

if __name__ == "__main__":
    print (thirdpartyinfo())

