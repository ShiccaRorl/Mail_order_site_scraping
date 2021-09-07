import sys
import os
import time
import pyautogui as pg

# pyscreeze の設定(画像が見当たらない場合に"ImageNotFoundException"を受け取る)
import pyscreeze
from pyscreeze import ImageNotFoundException
pyscreeze.USE_IMAGE_NOT_FOUND_EXCEPTION = True

# Logを残す
sys.stdout = open("pyautogui.log", "w")

#画像ファイルから座標を取得する関数
def get_locate_from_filename(filename):
    locate = None
    while locate == None:
        time.sleep(0.1)
        #グレイスケールで検索(95%一致で判定)
        locate = pg.locateCenterOnScreen(filename, grayscale=True,confidence=0.950)
        #フルカラーで検索(遅い)
        #locate = pg.locateCenterOnScreen(filename)
    return locate

#以下、メインルーチン
if __name__ == "__main__":

    #画面サイズの取得
    screen_x,screen_y = pg.size()

    #マウスを(1,1)に移動しておく
    pg.moveTo(1, 1, duration=1)

    #画像ファイルを検索してクリック
    nsec    = 0
    timeout = 5
    while True:
        try:
            button_position = get_locate_from_filename('search.png')
            pg.click(button_position)
            break
        except ImageNotFoundException: 
            time.sleep(1)
            nsec += 1
            if nsec > timeout:
                pg.alert(text='タイムアウト', button='OK')
                break