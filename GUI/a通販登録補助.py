# -*- coding:utf-8 -*-

import PySimpleGUI as sg
import datetime
import math

from sqlalchemy.ext.automap import automap_base
from sqlalchemy import *
from sqlalchemy import func
from sqlalchemy.orm import *
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import subprocess

from config import Config, Timebox
# pip install sqlalchemy
# pip install psycopg2
# pip install PySimpleGUI


#help(sg.Table)

config = Config()

id = 1

seeds = config.Base.classes.seeds_seeds

id = max_id()


layout = [
  [sg.Text('通販登録補助管理', size=(13,1))],
  [sg.Text('ソース', size=(10,1)), sg.Multiline(default_text="", key="-ソース-", size=(10, 5))],
  [sg.Text('柄あり', size=(10,1)), ],
  [sg.Text('バリエーションあり', size=(10,1)),],
  
  [sg.Text('商品', size=(13,1))],
  [sg.Text('商品コード', size=(10,1)), sg.InputText('', key="-商品コード-", size=(20,1)), ],
  [sg.Text('商品名', size=(10,1)), sg.InputText('', key="-商品名-", size=(20,1)), ],
  [sg.Text('税抜き価格', size=(10,1)), sg.Button(button_text='Amazon', key="-Amazon-"), sg.Button(button_text='ストアクリエイター', key="-ストアクリエイター-"), sg.Button(button_text='楽天', key="-楽天-"), sg.Button(button_text='ラクマ', key="-ラクマ-"), sg.Button(button_text='ストアーズ', key="-ストアーズ-"), sg.Button(button_text='メルカリ', key="-メルカリ-")],
  [sg.Text('税送料込み', size=(10,1)), sg.Button(button_text='通販Editer', key="-通販Editer-")],

　　[sg.Text('発送方法', size=(13,1))],
  [sg.Text('ヤフオク', size=(10,1)), sg.Button(button_text='最適化', key="-最適化-")],
  [sg.Text('アマゾン', size=(10,1)), sg.Multiline(default_text="", size=(50, 5), key="-コメント-"), sg.Button(button_text='保存', key="-保存-"), sg.Button(button_text='閉じる', key="-閉じる-")],
　　[sg.Text('楽天', size=(10,1))],
　　[sg.Text('メルカリ', size=(10,1))],
　　[sg.Text('ラクマ', size=(10,1))],

　　[sg.Text('商品説明', size=(13,1))],
　　[sg.Text('ラクマ', size=(10,1))],

  [sg.Text('過去ログ', size=(10,1)), sg.Listbox(過去ログ(), enable_events=True, size=(100, 10), key='-過去ログ-')],
  ]

# ウィンドウを作成する
window = sg.Window('通販登録補助管理', layout, resizable=True)

# == 時間↓ ==
timebox = Timebox()

# イベントループを使用してウィンドウを表示し、対話する
while True:
    event, values = window.read()
# ユーザーが終了したいのか、ウィンドウが閉じられたかどうかを確認してください
    if event == sg.WINDOW_CLOSED or event == '終了' or event == "閉じるb":
        break
    elif event == "日付":
        window["-日付-"].update(timebox.in_to_text_day(datetime.date.today()))
        日付 = datetime.date.today()

    elif event == "開始時間":
        window["-開始時間-"].update(timebox.in_to_text_start(datetime.datetime.now()))

    elif event == "終了時間":
        window["-終了時間-"].update(timebox.in_to_text_end(datetime.datetime.now()))

    elif event == "間時間":
        window["-日付-"].update(values["-日付-"].replace('-', '/').replace('+00:00', ''))
        window["-開始時間-"].update(values["-開始時間-"].replace('-', '/').replace('+00:00', ''))
        window["-終了時間-"].update(values["-終了時間-"].replace('-', '/').replace('+00:00', ''))
            
        try:
            # window["-間時間-"].update(end_time.in_time(values["-終了時間-"]) - start_time.in_time(values["-開始時間-"]))
            window["-間時間-"].update(timebox.ma_time)
        except:
            sg.PopupError('！日付計算エラー！')
        # == 時間↑ ==

    elif event == "-過去ログ-" or event == "-読み込み-":
        過去ログ2()
    elif event == "-データ取り込み-":
        データ取り込み()
    elif event == "-通販Editer-":
        subprocess.Popen(["python", "a通販Editer.py"], shell=True)
    elif event == "-Amazon-":
        Amazon()
    elif event == "-ストアクリエイター-":
        ストアクリエイター()
    elif event == "-楽天-":
        楽天()
    elif event == "-ラクマ-":
        ラクマ()
        
    elif event == "-ストアーズ-":
        ストアーズ()

    elif event == "-メルカリ-":
        メルカリ()    
    
    elif event == "-読了-":
        window["-読了-"].update("読了")
    elif event == "-閉じる-":
        break
    elif event == "-コピー-":
        window["-ID-"].update(max_id())
        window["-タイトル_id-"].update(values["-タイトル-"])
        window["-ファイル名_id-"].update("-ファイル名-")

    print(event, values)
    # Output a message to the window
    #window['-出力-'].update('ハロー ' + values['-入力-'] + "! PySimpleGUI をお試しいただきありがとうございます")

# 画面から削除して終了
window.close()