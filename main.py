#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pyhk  #http://www.schurpf.com/python/python-hotkey-module/
import os
import sys
import time

import clipboard
import win32api
import win32con


import SimulationKey

import SendKeys # 安装 http://pythonxy.googlecode.com/files/SendKeys-0.3_py27.exe

#sendkeys 示例  http://msdn.microsoft.com/zh-cn/library/system.windows.forms.sendkeys.send%28v=vs.110%29.aspx

import urllib
import urllib2


def throw_phone():
    org_clip_data = clipboard.getText()
    
    #模拟按键
    #SimulationKey.press('left_menu')
    SendKeys.SendKeys("^c") #复制文字
    
    #把文字提交到服务端
    postText(clipboard.getText())
    
    #还原
    clipboard.setText(org_clip_data)
    
def postText(text):
    if not text.strip():
        return False
    else:
        form_data = {"text": convertUtf8(text)};
        return post(**form_data)
        
def post(**kargs):
    url = "http://localhost/record.php"
    req = urllib2.Request(url, urllib.urlencode(kargs))
    resp = urllib2.urlopen(req)
    return resp.read()

def convertUtf8(s):
    encoding = mb_detect_encoding(s)
    if isinstance(s, unicode):
        return s.encode("utf-8")
    else:
        return s.decode(encoding).encode("utf-8")


def mb_detect_encoding(text, encoding_list=['gb2312', 'utf-8']):
    '''Return first matched encoding in encoding_list, otherwise return None.
    See [url]http://docs.python.org/2/howto/unicode.html#the-unicode-type[/url] for more info.
    See [url]http://docs.python.org/2/library/codecs.html#standard-encodings[/url] for encodings.'''
    for best_enc in encoding_list:
        try:
            unicode(text, best_enc)
        except:
            best_enc = None
        else:
            break
    return best_enc

hot = pyhk.pyhk()

hot.addHotkey(['3'], throw_phone);

hot.start()