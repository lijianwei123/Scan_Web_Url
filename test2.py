# -*- coding: utf-8 -*- 

'''
参考:
http://www.snakezero.com/index.php/archives/35/

http://www.cnblogs.com/wuchang/archive/2010/04/04/1704456.html


http://zoomq.qiniudn.com/ZQScrapBook/ZqFLOSS/data/20100812111528/

api:
http://timgolden.me.uk/pywin32-docs/win32_modules.html

py2exe
http://www.cnblogs.com/jans2002/archive/2006/09/30/519393.html
'''


from ctypes import *

import win32gui

user32 = windll.user32
kernel32 = windll.kernel32

class RECT(Structure):
 _fields_ = [
     ("left", c_ulong),
     ("top", c_ulong),
     ("right", c_ulong),
     ("bottom", c_ulong)
 ]

class GUITHREADINFO(Structure):
 _fields_ = [
     ("cbSize", c_ulong),
     ("flags", c_ulong),
     ("hwndActive", c_ulong),
     ("hwndFocus", c_ulong),
     ("hwndCapture", c_ulong),
     ("hwndMenuOwner", c_ulong),
     ("hwndMoveSize", c_ulong),
     ("hwndCaret", c_ulong),
     ("rcCaret", RECT)
 ]

def moveCursorInCurrentWindow(x, y):
 # Find the focussed window.
    guiThreadInfo = GUITHREADINFO(cbSize=sizeof(GUITHREADINFO))
    user32.GetGUIThreadInfo(0, byref(guiThreadInfo))
    focussedWindow = guiThreadInfo.hwndFocus

    # Find the screen position of the window.
    windowRect = RECT()
    user32.GetWindowRect(focussedWindow, byref(windowRect))
    
    #wnd = win32gui.GetForegroundWindow()
    print win32gui.GetWindowText(focussedWindow)
    
    # Finally, move the cursor relative to the window.
    user32.SetCursorPos(windowRect.left + x, windowRect.top + y)

if __name__ == '__main__':
    # Quick test.
    moveCursorInCurrentWindow(500, 800)