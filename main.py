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


def throw_phone():
    #模拟按键
    SimulationKey.press('ctrl', 'alt', 'esc')
    
    print clipboard.getText()

hot = pyhk.pyhk()

hot.addHotkey(['Alt', '3'], throw_phone);

hot.start()