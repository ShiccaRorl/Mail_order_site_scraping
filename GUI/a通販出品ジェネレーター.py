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

import webbrowser
import subprocess

# help(sg.Table)

config = Config()

id = 1

seeds = config.Base.classes.seeds_seeds

上 = sg.Column([
    [sg.Text('通販登録補助管理', size=(13, 1))],
    [sg.Text('ソース', size=(10, 1)), sg.Multiline(default_text="", key="-ソース-", size=(70, 7))],
    [sg.Text('柄あり', size=(10, 1)), sg.Checkbox("固定", key="-固定-")],
    [sg.Text('バリエーションあり', size=(10, 1)), sg.Checkbox("固定", key="-固定-")],
])

左 = sg.Column([
    [sg.Text('商品', size=(13, 1))],
    [sg.Text('商品コード', size=(10, 1)), sg.Checkbox("固定", key="-固定-"), sg.InputText('', key="-商品コード-", size=(40, 1)), ],
    [sg.Text('商品名', size=(10, 1)), sg.Checkbox("固定", key="-固定-"), sg.InputText('', key="-商品名-", size=(40, 1)), ],
    [sg.Text('税抜き価格', size=(10, 1)), sg.Checkbox("固定", key="-固定-"), sg.InputText('', key="-税抜き価格-", size=(40, 1)), ],
    [sg.Text('税送料込み', size=(10, 1)), sg.Checkbox("固定", key="-固定-"), sg.InputText('', key="-税送料込み-", size=(40, 1)), ],
    [sg.Text('ラクマ価格', size=(10, 1)), sg.Checkbox("固定", key="-固定-"), sg.InputText('', key="-ラクマ価格-", size=(40, 1)), ],
    [sg.Text('税率', size=(10, 1)), sg.Checkbox("固定", key="-固定-"), sg.InputText('', key="-税率-", size=(40, 1)), ],
    [sg.Text('', size=(13, 1))],

    [sg.Text('発送方法', size=(13, 1))],
    [sg.Text('ストアクリエイター', size=(10, 1)), sg.Checkbox("固定", key="-固定-"), sg.InputText('', key="-商品名-", size=(40, 1)), ],
    [sg.Text('アマゾン', size=(10, 1)), sg.Checkbox("固定", key="-固定-"), sg.InputText('', key="-商品名-", size=(40, 1)), ],
    [sg.Text('楽天', size=(10, 1)), sg.Checkbox("固定", key="-固定-"), sg.InputText('', key="-商品名-", size=(40, 1)), ],
    [sg.Text('メルカリ', size=(10, 1)), sg.Checkbox("固定", key="-固定-"), sg.InputText('', key="-商品名-", size=(40, 1)), ],
    [sg.Text('ラクマ', size=(10, 1)), sg.Checkbox("固定", key="-固定-"), sg.InputText('', key="-商品名-", size=(40, 1)), ],
    [sg.Text('', size=(13, 1))],

    [sg.Text('商品説明', size=(10, 1))],
    [sg.Text('サイズ', size=(10, 1)), sg.Checkbox("固定", key="-固定-"), sg.InputText('', key="-サイズ-", size=(40, 1)), ],
    [sg.Text('品質', size=(10, 1)), sg.Checkbox("固定", key="-固定-"), sg.InputText('', key="-品質-", size=(40, 1)), ],
    [sg.Text('生産国', size=(10, 1)), sg.Checkbox("固定", key="-固定-"), sg.InputText('', key="-生産国-", size=(40, 1)), ],
    [sg.Text('', size=(10, 1)), sg.Button(button_text='保存', key="-保存-")],
])

下 = sg.Column([
    [sg.Text('', size=(10, 1)), sg.Button(button_text='ラクマtest', key="-ラクマ在庫管理-")],
    [sg.Text('過去ログ', size=(10, 1)), sg.Listbox([0, 0], enable_events=True, size=(70, 7), key='-過去ログ-'),
     sg.Button(button_text='ディバック', key="-ディバック-")],
])

右 = sg.Column([
    [sg.Text('操作', size=(10, 1)), sg.Button(button_text='上にずらす', key="-上にずらす-")],
    [sg.Text('', size=(10, 1)), sg.Button(button_text='下にずらす', key="-下にずらす-")],
    [sg.Text('操作', size=(10, 1))],
    [sg.Text('', size=(10, 1)), sg.Button(button_text='Amazon', key="-Amazon-")],
    [sg.Text('', size=(10, 1)), sg.Button(button_text='ストアクリエイター', key="-ストアクリエイター-")],
    [sg.Text('', size=(10, 1)), sg.Button(button_text='楽天', key="-楽天-")],
    [sg.Text('', size=(10, 1)), sg.Button(button_text='ストアーズ', key="-ストアーズ-")],
    [sg.Text('', size=(10, 1)), sg.Button(button_text='ラクマ', key="-ラクマ-")],
    [sg.Text('', size=(10, 1)), sg.Button(button_text='メルカリ', key="-メルカリ-")],
])

main = [
    [sg.Pane([上], orientation='h')],
    [sg.Pane([左, 右], orientation='h')],
    [sg.Pane([下], orientation='h')],
]

# ウィンドウを作成する
window = sg.Window('通販登録補助管理', main, resizable=True)

# イベントループを使用してウィンドウを表示し、対話する
while True:
    event, values = window.read()
    # ユーザーが終了したいのか、ウィンドウが閉じられたかどうかを確認してください
    if event == sg.WINDOW_CLOSED or event == '終了' or event == "閉じる":
        break
    elif event == "-過去ログ-" or event == "-読み込み-":
        過去ログ2()
    elif event == "-通販Editer-":
        subprocess.Popen(["python", "./a通販Editer.py"], shell=True)
    elif event == "-Amazon-":
        webbrowser.open("https://www.google.com/search?client=firefox-b-d&q=" + values["-検索文字列-"])
        subprocess.Popen(["python", "./通販登録補助/Amazon.py"], shell=True)
    elif event == "-ストアクリエイター-":
        webbrowser.open("https://www.google.com/search?client=firefox-b-d&q=" + values["-検索文字列-"])
        subprocess.Popen(["python", "./通販登録補助/ストアクリエイター.py"], shell=True)
    elif event == "-楽天-":
        webbrowser.open("https://www.google.com/search?client=firefox-b-d&q=" + values["-検索文字列-"])
        subprocess.Popen(["python", "./通販登録補助/楽天.py"], shell=True)
    elif event == "-ラクマ-":
        subprocess.Popen(["python", "./通販登録補助/ラクマ.py"], shell=True)
    elif event == "-ストアーズ-":
        webbrowser.open("https://www.google.com/search?client=firefox-b-d&q=" + values["-検索文字列-"])
        subprocess.Popen(["python", "./通販登録補助/ストアーズ.py"], shell=True)

    elif event == "-メルカリ-":
        webbrowser.open("https://www.google.com/search?client=firefox-b-d&q=" + values["-検索文字列-"])
        subprocess.Popen(["python", "./通販登録補助/メルカリ.py"], shell=True)

    elif event == "-ラクマ在庫管理-":
        # webbrowser.open("https://www.google.com/search?client=firefox-b-d&q=" + values["-検索文字列-"])
        subprocess.Popen(["python", "./在庫管理/aラクマ_GUI.py"], shell=True)

    elif event == "-読了-":
        window["-読了-"].update("読了")
    elif event == "-閉じる-":
        break

    print(event, values)
    # Output a message to the window
    # window['-出力-'].update('ハロー ' + values['-入力-'] + "! PySimpleGUI をお試しいただきありがとうございます")

# 画面から削除して終了
window.close()
