#!/usr/bin/python
# -*- coding: utf-8 -*-

''' 添加右键菜单  '''

import _winreg
import sys
import os
import traceback

prog_name = 'throw to phone!'

prog_path = r'C:\Program Files\Internet Explorer\IEXPLORE.EXE'

try:
    key = _winreg.OpenKey(_winreg.HKEY_CLASSES_ROOT, r'*\\Shell')
except  WindowsError, e:
    #说明 Shell 不存在
    key = _winreg.OpenKey(_winreg.HKEY_CLASSES_ROOT, r'*')
    key = _winreg.CreateKey(key, 'Shell')
finally:
    pass
     
_winreg.SetValue(key, prog_name, _winreg.REG_SZ, prog_name + '(&I)')
  
prog_key = _winreg.OpenKey(key, prog_name)
  
_winreg.SetValue(prog_key, 'command', _winreg.REG_SZ, prog_path + ' %1 ')
  
_winreg.CloseKey(prog_key)
 
_winreg.CloseKey(key)

