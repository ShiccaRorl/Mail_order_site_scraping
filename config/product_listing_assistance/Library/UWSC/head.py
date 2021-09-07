# -*- coding: utf-8 -*-
import os,sys,re,time,subprocess
import pyautogui
import win32com.client



# (画面幅)
def G_SCREEN_W():
    screen_x,screen_y = pyautogui.size()
    return screen_x

# (画面高)
def G_SCREEN_H():
    screen_x,screen_y = pyautogui.size()
    return screen_y

# (画面色数)
def G_SCREEN_C():
    im  = pyautogui.screenshot()
    colordepth = im.dtype
    return colordepth

# (WindowsのPATH)
def GET_WIN_DIR():
    return os.environ['windir']

# (System32のPATH)
def GET_SYS_DIR():
    sysdir = os.environ['SystemRoot'] + '¥System32'
    return sysdir

# (カレントPATH)
def GET_CUR_DIR():
    return os.getcwd()

# (文字コード変換)
def ASC(str):
    return str.encode('UTF-8')

# CHR(文字コード変換)
def CHR(str):
    return str.encode('ASCII')

# (マウスカーソル移動)
def MMV(x,y,deley):
    msec = deley / 1000
    time.sleep(msec)
    pyautogui.moveTo(x,y)
    
# (マウス操作)
def BTN(key,sta,x,y,deley):
    msec = deley / 1000
    time.sleep(msec)
    if sta == 0:
        if key == 'LEFT':
            pyautogui.click(x, y)
        if key == 'RIGHT':
            pyautogui.rightClick(x, y)
        if key == 'MIDDLE':
            pyautogui.middleClick(x, y)
        if key == 'WHEEL':
            pyautogui.scroll(sta, x, y)
        if key == 'TOUCH':
            pyautogui.click(x,y)
    if sta == 1:
        if key == 'LEFT':
            pyautogui.mouseDown(x, y, button='left')
        if key == 'RIGHT':
            pyautogui.mouseDown(x, y, button='right')
        if key == 'MIDDLE':
            pyautogui.mouseDown(x, y, button='middle')
        if key == 'WHEEL':
            pyautogui.scroll(sta, x, y)
        if key == 'TOUCH':
            pyautogui.mouseDown(x, y, button='left')
    if sta == 2:
        if key == 'LEFT':
            pyautogui.mouseUp(x, y, button='left')
        if key == 'RIGHT':
            pyautogui.mouseUp(x, y, button='right')
        if key == 'MIDDLE':
            pyautogui.mouseUp(x, y, button='middle')
        if key == 'WHEEL':
            pyautogui.scroll(sta, x, y)
        if key == 'TOUCH':
            pyautogui.mouseUp(x, y, button='left')
    if sta > 2:
        pyautogui.scroll(sta, x, y)
    if sta < 0:
        pyautogui.scroll(sta, x, y)
        
# (キー操作)
def KBD(key,sta,deley):
    msec = deley / 1000
    time.sleep(msec)
    if sta == 0:
        pyautogui.press(key)
    if sta == 1:
        pyautogui.keyDown(key)
    if sta == 2:
        pyautogui.keyUp(key)
        
# CHKIMG (画像マッチング)
def CHKIMG(filename,maskcolor,rx1,ry1,rx2,ry2,num,conf):
    #返値はtuple型
    if len(conf) > 11:
        CFG = 0.95
    else:
        CFG = 0.98
    counter = 0        
    for pos in pyautogui.locateAllOnScreen(filename,region=(rx1,ry1,rx2,ry2),confidence=CFG):
        lpos = pos
        if counter == num:
            break
        counter += 1
    return lpos

# (メッセージボックス)
def MSGBOX(mes,btype):
    if btype == 'BTN_OK':
        result = pyautogui.alert(text=mes,title='',button='OK')
    if btype == 'BTN_NO':
        result = pyautogui.alert(text=mes,title='',button='NO')
    if btype == 'BTN_YES':
        result = pyautogui.confirm(text=mes, title='', buttons=['Yes', 'No'])
    if btype == 'BTN_CANCEL':
        result = pyautogui.confirm(text=mes, title='', buttons=['OK', 'Cancel'])
    if btype == 'BTN_ABORT':
        result = pyautogui.alert(text=mes,title='',button='ABORT')
    if btype == 'BTN_RETRY':
        result = pyautogui.alert(text=mes,title='',button='RETRY')
    if btype == 'BTN_IGNORE':
        result = pyautogui.alert(text=mes,title='',button='IGNORE')
    return result

# (入力ボックス)
def INPUT(mes,defv,hide):
    if hide == 0:
        result = pyautogui.prompt(text=mes, title='',default=defv)
    if hide == 1:
        result = pyautogui.password(text=mes, title='', default=defv, mask='*')
    return result

# (スクリーンショット)
def SAVEIMAGE(filename,x1,y1,x2,y2):
    pyautogui.screenshot(filename,region=(x1,y1,x2,y2))
    
