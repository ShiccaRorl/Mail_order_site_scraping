# -*- coding: utf-8 -*-
import os,sys,re,time,subprocess
import win32api
import win32gui
import win32con
import win32process

#プロセスIDからハンドル取得
def get_hwnds_for_pid (pid):
    def callback (hwnd, hwnds):
        if win32gui.IsWindowVisible (hwnd) and win32gui.IsWindowEnabled (hwnd):
            _, found_pid = win32process.GetWindowThreadProcessId (hwnd)
            if found_pid == pid:
                hwnds.append (hwnd)
    return True

    hwnds = []
    win32gui.EnumWindows (callback, hwnds)

    return hwnds

## 起動したアプリの画面サイズ変更
child_process = subprocess.Popen(r'c:\windows\system32\notepad.exe')
time.sleep(2)
pid = child_process.pid

for hwnd in get_hwnds_for_pid(pid):
    if hwnd == 0:
        print("Windows Target Application not found!")
    else:
        #サイズ指定(リサイズ)
        win32gui.MoveWindow(hwnd, 100, 100, 500, 500, True)
        #最大化
        win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
        time.sleep(1)
        #閉じる
        win32gui.SendMessage(hwnd,win32con.WM_CLOSE,0,0)