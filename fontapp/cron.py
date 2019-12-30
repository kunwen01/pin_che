#!/usr/bin/env python
#-*- coding:utf-8 -*-

import re


import re
import zmail
from bs4 import BeautifulSoup
from django.utils import timezone

from .models import ThirdParty

def thirdpartyinfo():
    # 你要执行的任务函数
    server = zmail.server('kunwen01@outlook.com', 'fafentuqiang123')

    # Retrieve mail
    latest_mails = server.get_mails(subject='拼车', start_time=timezone.now().date().strftime('%Y-%m-%y 00:00:00'))
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
            if len(phone_list) > 0:
                test1 = ThirdParty(phone=phone_list[0], content=m_str)
                test1.save()
        return m_str


if __name__ == "__main__":
    print (thirdpartyinfo())