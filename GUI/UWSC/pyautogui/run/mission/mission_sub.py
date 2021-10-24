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
    while True:
        try:
            button_position = get_locate_from_filename('./mission/mission06.png')
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
            button_position = get_locate_from_filename('./mission/mission07.png')
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
            button_position = get_locate_from_filename('./mission/mission07.png')
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
            button_position = get_locate_from_filename('./mission/mission07.png')
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
            button_position = get_locate_from_filename('./mission/mission08.png')
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
            button_position = get_locate_from_filename('./mission/mission08.png')
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
            button_position = get_locate_from_filename('./mission/mission08.png')
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
            button_position = get_locate_from_filename('./mission/mission16.png')
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
            button_position = get_locate_from_filename('./mission/mission16.png')
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
            button_position = get_locate_from_filename('./mission/mission16.png')
            pg.click(button_position)
            break
        except ImageNotFoundException: 
            time.sleep(1)
            nsec += 1
            if nsec > timeout:
                pg.alert(text='タイムアウト', button='OK')
                break
# ===========================================
