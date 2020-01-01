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
    # server = zmail.server('godknows561@163.com', 'asdf123',config='163')
    # server = zmail.server('1101122765@qq.com', 'jkl;\'12345',smtp_host="smtp.exmail.qq.com",smtp_port=465)


    # Retrieve mail
    latest_mails = server.get_mails(subject='拼车', start_time=date.today().strftime('%Y-%m-%y 00:00:00'))
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
    return latest_mails

from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

import poplib

# 输入邮件地址, 口令和POP3服务器地址:
email = 'godknows561@163.com'
password = 'asdf123'
pop3_server = 'pop.163.com'

def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset

def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value

def print_info(msg, indent=0):
    if indent == 0:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header=='Subject':
                    value = decode_str(value)
                else:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
            print('%s%s: %s' % ('  ' * indent, header, value))
    if (msg.is_multipart()):
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print('%spart %s' % ('  ' * indent, n))
            print('%s--------------------' % ('  ' * indent))
            print_info(part, indent + 1)
    else:
        content_type = msg.get_content_type()
        if content_type=='text/plain' or content_type=='text/html':
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
            print('%sText: %s' % ('  ' * indent, content + '...'))
        else:
            print('%sAttachment: %s' % ('  ' * indent, content_type))

# 连接到POP3服务器:
server = poplib.POP3(pop3_server)
# 可以打开或关闭调试信息:
server.set_debuglevel(1)
# 可选:打印POP3服务器的欢迎文字:
print(server.getwelcome().decode('utf-8'))
# 身份认证:
server.user(email)
server.pass_(password)
# stat()返回邮件数量和占用空间:
print('Messages: %s. Size: %s' % server.stat())
# list()返回所有邮件的编号:
resp, mails, octets = server.list()
# 可以查看返回的列表类似[b'1 82923', b'2 2184', ...]
print(mails)
# 获取最新一封邮件, 注意索引号从1开始:
index = len(mails)
resp, lines, octets = server.retr(index)
# lines存储了邮件的原始文本的每一行,
# 可以获得整个邮件的原始文本:
msg_content = b'\r\n'.join(lines)
# 稍后解析出邮件:
# msg = Parser().parsestr(msg_content)
print(msg_content)
# 可以根据邮件索引号直接从服务器删除邮件:
# server.dele(index)
# 关闭连接:
server.quit()
if __name__ == "__main__":
    # print (thirdpartyinfo())
    pass
