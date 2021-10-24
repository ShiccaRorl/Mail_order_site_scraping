# -*- coding:utf-8 -*-

import PySimpleGUI as sg
import datetime

from config import Config
import webbrowser
import subprocess

# pip install sqlalchemy
# pip install psycopg2
# pip install PySimpleGUI

from sqlalchemy.ext.automap import automap_base
from sqlalchemy import * 
from sqlalchemy.orm import *
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


import subprocess

config = Config()
t_人事 = config.Base.classes.human_resources_t_人事

def ユーザーs():
    # 過去ログテーブル　の計算
    session = Session(config.engine)
    ユーザーs = session.query(t_人事).order_by(t_人事.id).all()

    # ウィンドウの内容を定義する
    # 画面レイアウトを指定


    member_list = []

    #print(t)
    for i in ユーザーs:
        member_list.append([i.id, i.名前, i.ログイン状態])
    return member_list

header = ['ID', '名前', "ログイン状態"]


T1 = sg.Column([
[sg.Text('ユーザーs', size=(10, 1)), sg.Listbox(ユーザーs(), size=(15, 10), key="-ユーザーs-"), ],
])

layout = sg.Column([
  [sg.Text('ログイン')],
  [sg.Text('パスワード', size=(10,1)), sg.InputText('', key="-パスワード-", size=(20,1), password_char="●")],
  [sg.Button(button_text='ログイン',key="ログイン"), sg.Button(button_text="ログアウト", key="ログアウト")],
  [sg.Text("状態", key="-状態-")],
  ])

L = [
    [sg.Pane([T1, layout], orientation='h')]
    ]

# ウィンドウを作成する
window = sg.Window('ログイン', L, resizable=True)

# イベントループを使用してウィンドウを表示し、対話する
while True:
    event, values = window.read()
# ユーザーが終了したいのか、ウィンドウが閉じられたかどうかを確認してください
    if event == sg.WINDOW_CLOSED or event == '終了' or event == "-閉じる-":
        break
            
    elif event == "ログイン":
        # コマンド

        try:
            data = values["-ユーザーs-"]
            #print(data[0][0])
            id = data[0][0]

            session = Session(config.engine)
            pw = session.query(t_人事).where(t_人事.id == id).first()

            print(id)
            pw = pw.パスワード
            pw2 = values["-パスワード-"]
            print(pw2)
            if pw == pw2:
                window["-状態-"].update("承認成功")
                subprocess.Popen(["python", "./aメニュー.py", f"{id}"], shell=True)
            else:
                window["-状態-"].update("承認失敗")
            
        except:
            sg.PopupError('！エラー発生！')

    print(event, values)
    # Output a message to the window
    #window['-出力-'].update('ハロー ' + values['-入力-'] + "! PySimpleGUI をお試しいただきありがとうございます")

# 画面から削除して終了
window.close()