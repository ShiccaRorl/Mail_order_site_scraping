# -*- coding: utf-8 -*-

import time
import pyautogui as pg
import subprocess
import threading

class FGO():
    スクリーンショット
    モード

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

def worker0():    # モード
    # thread の名前を取得
    while True:
        # ログインモード
        if None != get_locate_from_filename("./login/login.png"):
            print("ログインモード")
        # メニューモード
        print("メニューモード")
    
        # バトルモード
        print("バトルモード")
    
        # 待ち時間モード
        print("待ち時間モード")
    
        # ログインボーナスモード
        print("ログインボーナスモード")
    
        time.sleep(1)
    
    proc = subprocess.run("python ./login/login.py", shell=True)
    date = proc.stdout
    print(date)
    
    time.sleep(5)


def worker1():    # ログイン
    # thread の名前を取得
    proc = subprocess.run("python ./login/login.py", shell=True)
    date = proc.stdout
    print(date)
    
    time.sleep(5)

def worker2():    # ログインボーナス
    # thread の名前を取得
    proc = subprocess.run("python ./login_bonus/login_bonus.py", shell=True)
    date = proc.stdout
    print(date)
    
    time.sleep(5)

def worker3():    # ディミッション
    # thread の名前を取得
    proc = subprocess.run("python ./day_mission/day_mission.py", shell=True)
    date = proc.stdout
    print(date)
    
    time.sleep(5)

def worker4():    # ウイークリーミッション
    # thread の名前を取得
    proc = subprocess.run("python ./week_mission/week_mission.py", shell=True)
    date = proc.stdout
    print(date)
    
    time.sleep(5)

def worker5():    # ミッション
    # thread の名前を取得
    proc = subprocess.run("python ./mission/mission.py", shell=True)
    date = proc.stdout
    print(date)
    
    time.sleep(5)

def worker6():    # ログアウト
    # thread の名前を取得
    proc = subprocess.run("python ./logout/logout.py", shell=True)
    date = proc.stdout
    print(date)
    
    time.sleep(5)





#以下、メインルーチン
if __name__ == "__main__":
    # スレッドに workder1 関数を渡す
    #t1 = threading.Thread(target=worker1)
    #t2 = threading.Thread(target=worker2)
    #t3 = threading.Thread(target=worker3)
    #t4 = threading.Thread(target=worker4)
    t5 = threading.Thread(target=worker5)
    # スレッドスタート
    #t1.start()
    #t2.start()
    #t3.start()
    #t4.start()
    t5.start()
    