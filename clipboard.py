#!/usr/bin/env python  
# -*- coding: utf-8 -*- 

'''
参考http://my.oschina.net/jeffyu/blog/62032
操作windows clipboard
'''

import  win32clipboard as w
import win32con

#获取内容
def getText():
    w.OpenClipboard()
    d = w.GetClipboardData(win32con.CF_TEXT)
    w.CloseClipboard()
    return d

#设置内容
def setText(aString):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_TEXT, aString)
    w.CloseClipboard()
    
if __name__ == '__main__':
    print getText()