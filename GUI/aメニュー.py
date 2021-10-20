# -*- coding:utf-8 -*-

# 2021/10/06

import PySimpleGUI as sg
import datetime

"""
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import * 
from sqlalchemy.orm import *
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
"""

from config import Config
#import webbrowser
import subprocess
import sys

# pip install sqlalchemy
# pip install psycopg2
# pip install PySimpleGUI

args = sys.argv
id = args[1]

if id == None:
    exit

#help(sg.Table)

config = Config()

#t_103_ライフログ = config.Base.classes.LifeLog_t_103_ライフログ

#Session = sessionmaker(bind=config.engine)
#session = Session(config.engine)

class Menu_Log:
    def __init__(self):
        self.config = Config()
        self.id = max_id()
        self.start_time = datetime.datetime.now()
        self.end_time = datetime.datetime.now()
        self.プログラム名 = ""

    def start_time(self):
        self.start_time = datetime.datetime.now()

    def end_time(self):
        self.end_time = datetime.datetime.now()

    def プログラム名(self, name):
        self.プログラム名 = name
"""
    def 保存(self):
        t_103_ライフログ = self.config.Base.classes.LifeLog_t_103_ライフログ
        session = Session(self.config.engine)

        print("insert")
        if values["-日付-"] == None:
            values["-日付-"] = datetime.date.today()
        if self.start_time == None:
            self.start_time = datetime.datetime.now()
        if self.end_time == None:
            self.end_time = datetime.datetime.now()
        session.add(t_103_ライフログ(id = self.id,
                                        日付 = datetime.date.today(),
                                        開始時間 = self.start_time,
                                        終了時間 = self.end_time,
                                        プログラム名 = self.プログラム名,
        ))
        session.commit()
"""
"""
def メニューログ(data=None):
        print(data)
        # 過去ログテーブル　の計算
        session = Session(config.engine)
        過去ログ = session.query(t_103_ライフログ).order_by(asc(t_103_ライフログ.開始時間)).limit(30)

        # ウィンドウの内容を定義する
        # 画面レイアウトを指定


        member_list = []

        #print(t)
        for i in 過去ログ:
            member_list.append([i.id, i.開始時間, i.終了時間, i.プログラム名])
        return member_list

header = ['ID', '開始時間', '終了時間', "プログラム名"]


def max_id():
    # 過去ログテーブル　の計算
    過去ログ = session.query(t_103_ライフログ).order_by(desc(t_103_ライフログ.開始時間)).limit(30)
    # 最大値の計算
    i = []
    for s in 過去ログ:
        i.append(s.id)
    return max(i) + 1


id = max_id()
"""
layout = [
  [sg.Text('メニュー管理')],
  [sg.Button(button_text='通販',key="通販")],
  [sg.Button(button_text='プログラム',key="プログラム"), sg.Button(button_text='検索文字列',key="検索文字列")],
  #[sg.Button(button_text='映画',key="映画")],
  #[sg.Button(button_text='読書',key="読書"), sg.Button(button_text='本',key="本")],


  [sg.Button(button_text='プロジェクト',key="プロジェクト"), sg.Button(button_text='やりたい事リスト',key="やりたい事リスト")],
  [sg.Button(button_text='メール送信',key="メール送信")],
  [sg.Button(button_text='メニューログ',key="メニューログ")],
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
    elif event == "通販":
        subprocess.Popen(["python", f"./a通販.py", f"{id}"], shell=True)

    elif event == "プログラム":
        subprocess.Popen(["python", f"./aProgram.py", f"{id}"], shell=True)

    elif event == "検索文字列":
        #検索文字列menu_log = Menu_Log()
        #検索文字列menu_log.プログラム名("検索文字列")
        #検索文字列menu_log.start_time()
        subprocess.Popen(["python", f"./a検索文字列.py", f"{id}"], shell=True)
        #検索文字列menu_log.end_time()
        #検索文字列menu_log.保存()

    elif event == "プロジェクト":
        print("")

    elif event == "やりたい事リスト":
        subprocess.Popen(["python", f"./aやりたい事リスト.py", f"{id}"], shell=True)

    elif event == "メール送信":
        subprocess.Popen(["python", f"./aメール送信.py", f"{id}"], shell=True)

    elif event == "メニューログ":
        print("")

    elif event == "-閉じる-":
        break
    print(event, values)
    # Output a message to the window
    #window['-出力-'].update('ハロー ' + values['-入力-'] + "! PySimpleGUI をお試しいただきありがとうございます")

# 画面から削除して終了
window.close()