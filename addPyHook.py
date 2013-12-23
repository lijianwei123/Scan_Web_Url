#!/usr/bin/env python  
# -*- coding: utf-8 -*- 

'''
pyHook 监控windows下 鼠标  键盘事件   
api: http://pyhook.sourceforge.net/doc_1.5.0/
tutorial: http://sourceforge.net/apps/mediawiki/pyhook/index.php?title=PyHook_Tutorial
'''


import pythoncom  #需要安装 pywin32库   http://sourceforge.net/projects/pywin32/files/pywin32/Build%20218/
import pyHook  #http://sourceforge.net/projects/pyhook/
import time
import os
import sys
import win32api
import win32con

sys.path.append(".")

import test

def onMouseEvent(event):
      # 监听鼠标事件
#     print "MessageName:", event.MessageName
#     print "Message:", event.Message
#     print "Time:", event.Time
#     print "Window:", event.Window
#     print "WindowName:", event.WindowName
#     print "Position:", event.Position
#     print "Wheel:", event.Wheel
#     print "Injected:", event.Injected
#     print "---"
    
    #test.test()
    
    
    return True

def onKeyboardEvent(event):
    #监听键盘事件
#     print 'MessageName:',event.MessageName
#     print 'Message:',event.Message
#     print 'Time:',event.Time
#     print 'Window:',event.Window
#     print 'WindowName:',event.WindowName
#     print 'Ascii:', event.Ascii, chr(event.Ascii)
#     print 'Key:', event.Key
#     print 'KeyID:', event.KeyID
#     print 'ScanCode:', event.ScanCode
#     print 'Extended:', event.Extended
#     print 'Injected:', event.Injected
#     print 'Alt', event.Alt
#     print 'Transition', event.Transition
#     print '---'
    
    if str(event.Key) == 'Z':
        hm.UnhookKeyboard()
    
    return True

if __name__ == "__main__":
    hm = pyHook.HookManager()
    
    #鼠标事件
    hm.MouseAll = onMouseEvent
    hm.HookMouse()
    
    #键盘事件
    #hm.KeyDown = onKeyboardEvent
    #hm.HookKeyboard()
        
    pythoncom.PumpMessages()
    
#     import win32ui
#      wnd = win32ui.GetForegroundWindow()
#      print wnd.GetWindowText()

    #win32api.PostQuitMessage() 关闭程序
    #win32api.MessageBox(win32con.NULL, 'Python 你好！', '你好', win32con.MB_OK)
