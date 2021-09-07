# -*- coding: utf-8 -*-

import time
import pyautogui as pg
import subprocess

#画像ファイルから座標を取得する関数
def get_locate_from_filename(filename):
    locate = None
    while locate == None:
        time.sleep(0.1)
        #グレイスケールで検索(95%一致で判定)
        locate = pg.locateCenterOnScreen(filename, grayscale=True,confidence=0.700)
        #フルカラーで検索(遅い)
        #locate = pg.locateCenterOnScreen(filename)
    return locate

def バトル関数():
    print("バトル開始")
    
    #画像ファイルを検索してクリック
    nsec    = 0
    timeout = 3

# ===========================================
    time.seleep(10)
    proc = subprocess.run("python ./mission/mission_sub.py", shell=True)
    date = proc.stdout
    print(date)
    proc = subprocess.run("python ./mission/mission_sub.py", shell=True)
    date = proc.stdout
    print(date)
    proc = subprocess.run("python ./mission/mission_sub.py", shell=True)
    date = proc.stdout
    print(date)
# ===========================================


    while True:
        try:
            button_position = get_locate_from_filename('./mission/mission09.png')
            time.sleep(2)
            pg.click(button_position)
            break
        except ImageNotFoundException: 
            time.sleep(1)
            nsec += 1
            if nsec > timeout:
                pg.alert(text='タイムアウト', button='OK')
                break
    
    while True:     
        try:
            button_position = get_locate_from_filename('./mission/mission14.png')
            time.sleep(2)
            pg.click(button_position)
            break
        except ImageNotFoundException: 
            time.sleep(1)
            nsec += 1
            if nsec > timeout:
                pg.alert(text='タイムアウト', button='OK')
                break

    while True:     
        try:
            button_position = get_locate_from_filename('./mission/mission10.png')
            pg.click(button_position)
            break
        except ImageNotFoundException: 
            time.sleep(1)
            nsec += 1
            if nsec > timeout:
                pg.alert(text='タイムアウト', button='OK')
                break

    while True:     
        try:
            button_position = get_locate_from_filename('./mission/mission12.png')
            pg.click(button_position)
            break
        except ImageNotFoundException: 
            time.sleep(1)
            nsec += 1
            if nsec > timeout:
                pg.alert(text='タイムアウト', button='OK')
                break

    while True:     
        try:
            button_position = get_locate_from_filename('./mission/mission10.png')
            pg.click(button_position)
            break
        except ImageNotFoundException: 
            time.sleep(1)
            nsec += 1
            if nsec > timeout:
                pg.alert(text='タイムアウト', button='OK')
                break

    while True: 
        try:
            button_position = get_locate_from_filename('./mission/mission15.png')
            pg.click(button_position)
            break
        except ImageNotFoundException: 
            time.sleep(1)
            nsec += 1
            if nsec > timeout:
                pg.alert(text='タイムアウト', button='OK')
                break
    while True: 
        try:
            button_position = get_locate_from_filename('./mission/mission12.png')
            pg.click(button_position)
            break
        except ImageNotFoundException: 
            time.sleep(1)
            nsec += 1
            if nsec > timeout:
                pg.alert(text='タイムアウト', button='OK')
                break
         
    print("バトル終了")


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
            print("フリークエスト")
            button_position = get_locate_from_filename('./mission/mission13.png')
            pg.click(button_position)
            break
        except ImageNotFoundException: 
            time.sleep(1)
            nsec += 1
            if nsec > timeout:
                pg.alert(text='タイムアウト', button='OK')
                break
            
                #button_position = get_locate_from_filename('./mission/mission01.png')
                #pg.click(button_position)

                #button_position = get_locate_from_filename('./mission/mission02.png')
                #pg.click(button_position)

    print("仲間選択")
    while True: 
        try:
            button_position = get_locate_from_filename('./mission/mission03.png')
            pg.click(button_position)
            break
        except ImageNotFoundException: 
            time.sleep(1)
            nsec += 1
            if nsec > timeout:
                pg.alert(text='タイムアウト', button='OK')
                break

    print("クエスト開始")
    while True: 
        try:
            button_position = get_locate_from_filename('./mission/mission04.png')
            pg.click(button_position)
            break
        except ImageNotFoundException: 
            time.sleep(1)
            nsec += 1
            if nsec > timeout:
                pg.alert(text='タイムアウト', button='OK')
                break
            
                #button_position = get_locate_from_filename('./mission/mission05.png')
                #pg.click(button_position)

    バトル関数()
        

            
                #button_position = get_locate_from_filename('./mission/mission11.png')
                #pg.click(button_position)
    while True:      
        try:
            button_position = get_locate_from_filename('./mission/mission12.png')
            pg.click(button_position)
            break
        except ImageNotFoundException: 
            time.sleep(1)
            nsec += 1
            if nsec > timeout:
                pg.alert(text='タイムアウト', button='OK')
                break
            
    while True: 
        try:
            button_position = get_locate_from_filename('./mission/mission14.png')
            pg.click(button_position)
            break
        except ImageNotFoundException: 
            time.sleep(1)
            nsec += 1
            if nsec > timeout:
                pg.alert(text='タイムアウト', button='OK')
                break

    while True: 
        try:
            button_position = get_locate_from_filename('./mission/mission15.png')
            pg.click(button_position)
            break
        except ImageNotFoundException: 
            time.sleep(1)
            nsec += 1
            if nsec > timeout:
                pg.alert(text='タイムアウト', button='OK')
                break