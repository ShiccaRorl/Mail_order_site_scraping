# -*- coding:utf-8 -*-

# 2021/10/06

import PySimpleGUI as sg
import datetime
import subprocess

layout = [
  [sg.Text('メニュー管理')],
  [sg.Button(button_text='通販データ取り込み',key="通販データ取り込み"), sg.Button(button_text='通販',key="通販")],
  #[sg.Button(button_text='通販',key="-通販-")],
  [sg.Button(button_text='通販登録補助',key="-通販登録補助-"), sg.Button(button_text='ラクマ専用',key="ラクマ専用")],
  #[sg.Button(button_text='プログラム',key="プログラム"), sg.Button(button_text='検索文字列',key="検索文字列")],
  [sg.Button(button_text='在庫管理',key="-在庫管理-")],
  [sg.Button(button_text='通販経理',key="-通販経理-"),],


  [sg.Button(button_text='プロジェクト',key="プロジェクト"), sg.Button(button_text='やりたい事リスト',key="-やりたい事リスト-")],
  [sg.Button(button_text='メール送信',key="メール送信"), sg.Button(button_text='作業ログ',key="作業ログ")],
  ]

# ウィンドウを作成する
window = sg.Window('メニュー管理', layout, resizable=True)

id = 1

# イベントループを使用してウィンドウを表示し、対話する
while True:
    event, values = window.read()
# ユーザーが終了したいのか、ウィンドウが閉じられたかどうかを確認してください
    if event == sg.WINDOW_CLOSED or event == '終了' or event == "-閉じる-":
        break
    elif event == "-通販-":
        subprocess.Popen(["python", f"./a通販.py", f"{id}"], shell=True)
    
    elif event == "通販データ取り込み":
        #dir_data = "./通販データ取り込み/"
        #subprocess.Popen(["取り込み.cmd"], cwd=dir_data, shell=True)
        subprocess.Popen(["取り込み.cmd"], shell=True)
        #subprocess.Popen(["zaラクマ_入力テスト.CMD"], cwd=dir_data, shell=True)
    
    
        

    elif event == "-通販登録補助-":
        subprocess.Popen(["python", f"./a通販登録補助.py", f"{id}"], shell=True)

    elif event == "-在庫管理-":
        subprocess.Popen(["python", f"./a在庫管理.py", f"{id}"], shell=True)
        
    elif event == "ラクマ専用":
        #dir_data = "C:\\Users\\user\\Downloads\\バックアップ\\プログラム\\Chrome拡張\\Mail_order_site_scraping\\GUI\\在庫管理\\"
        dir_data = "./在庫管理/"
        subprocess.Popen(["python", f"./aラクマ出品_GUI.py", f"{id}"], cwd=dir_data, shell=True)
        #subprocess.Popen(["zaラクマ_入力テスト.CMD"], cwd=dir_data, shell=True)
    elif event == "-通販経理-":
        print("")

    elif event == "-やりたい事リスト-":
        subprocess.Popen(["python", "./aやりたい事リスト.py", f"{id}"], shell=True)

    elif event == "-メール送信-":
        subprocess.Popen(["python", "./aメール送信.py", f"{id}"], shell=True)

    elif event == "-作業ログ-":
        subprocess.Popen(["python", "./a作業ログ.py", f"{id}"], shell=True)

    elif event == "-メニューログ-":
        print("")

    elif event == "-閉じる-":
        break
    print(event, values)
    # Output a message to the window
    #window['-出力-'].update('ハロー ' + values['-入力-'] + "! PySimpleGUI をお試しいただきありがとうございます")

# 画面から削除して終了
window.close()