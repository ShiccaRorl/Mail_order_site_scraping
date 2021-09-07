import os,sys,re,time,subprocess
import win32api, win32gui, win32con, win32process

def get_pid(title):
    hwnd = win32gui.FindWindow(None, title)
    threadid,pid = win32process.GetWindowThreadProcessId(hwnd)
    return pid

def get_hwnds(pid):
    def callback(hwnd, hwnds):
        if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
            _, found_pid = win32process.GetWindowThreadProcessId(hwnd)
            if found_pid == pid:
                hwnds.append(hwnd)
        return True
    hwnds = []
    win32gui.EnumWindows(callback, hwnds)
    return hwnds 

def clkitem(win_title,itemid):
    #ウインドウタイトルで探す
    hwnd = win32gui.FindWindow(0, win_title)

    #ウインドウのアイテムをリスト化
    inplay_children = []
    def is_win_ok(hwnd, *args):
        s = win32gui.GetWindowText(hwnd)
        inplay_children.append(hwnd)
    win32gui.EnumChildWindows(hwnd, is_win_ok, None)

    #アイテムIDの番号を指定し、アイテム/ボタンのハンドルを取得
    button_hwnd = inplay_children[itemid]

    #ウインドウをアクティブにする
    win32gui.SetForegroundWindow(hwnd)
    #指定したボタンをクリック（押下->解除を送信)
    win32api.PostMessage(button_hwnd, win32con.WM_LBUTTONDOWN, 0, 0)
    win32api.PostMessage(button_hwnd, win32con.WM_LBUTTONUP, 0, 0)

#ウインドウIDからプロセスIDを取得
pid = get_pid(u"電卓")

#電卓の1つめのボタンをクリック
clkitem(u"電卓",1)

#プロセスIDからハンドルを取得して操作[GETCTLHND]と同等
for hwnd in get_hwnds(pid):
    if hwnd == 0:
        print(u"ウインドウが見つからない")
    else:
        #サイズ指定(リサイズ)
        win32gui.MoveWindow(hwnd, 100, 100, 500, 500, True)
        #最大化
        win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
        time.sleep(1)
        #閉じる
        win32gui.SendMessage(hwnd,win32con.WM_CLOSE,0,0)