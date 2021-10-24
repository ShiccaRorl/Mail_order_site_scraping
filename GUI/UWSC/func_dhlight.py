import win32gui

##デスクトップのハイライト
def dhlight(x1, y1, x2, y2):
    hwnd=win32gui.WindowFromPoint((x1,y1))
    hdc=win32gui.GetDC(hwnd)
    rc=(x1, y1, x2, y2)
    win32gui.DrawFocusRect(hdc, rc)
    win32gui.ReleaseDC(hwnd,hdc)

if __name__ == '__main__':
    ##pyautoguiのlocateOnScreenと組み合わせて使う感じですね
    ##ただし、locateOnScreenはBox(left, top, width, height)を返すので
    pos_x,pos_y,size_w,size_h  = pyautogui.locateOnScreen('target.png')
    x1 = pos_x
    y1 = pos_y
    x2 = pos_x + size_w
    y2 = pos_y + size_h
    dhlight(x1, y1, x2, y2)
    ##と書けば、target.pngが見つかったところに点線で矩形が表示されます。