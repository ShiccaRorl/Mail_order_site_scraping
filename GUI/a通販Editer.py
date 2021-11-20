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


from config import Config, Timebox
# pip install sqlalchemy
# pip install psycopg2
# pip install PySimpleGUI


#help(sg.Table)

config = Config()


sale_sele = config.Base.classes.sale_sele

def max_id():
    # 過去ログテーブル　の計算
    session = Session(config.engine)
    過去ログ = session.query(sale_sele).order_by(desc(sale_sele.created_at)).limit(30)
    #過去ログ = LifeLogT07読書.select().order_by(LifeLogT07読書.日付).limit(30)
    # 最大値の計算
    i = []
    try:
        for s in 過去ログ:
            i.append(s.id)
        return max(i) + 1
    except:
        return 1


id = max_id()


def 取引リスト():
    return ['test', 'test']

def 消費税():
    return 0.1

def 過去ログ():
    return ['test','test']

def 過去ログ2():
    return ['test','test']

def 新規保存():
    print()

def 保存():
    print()

左 = sg.Column([
    [sg.Text('通販Editer')],
    [sg.Text('取引リスト')],
    [sg.Listbox(取引リスト(), enable_events=True, size=(50, 200), key='-取引リスト-')],
])

ヘッダー = sg.Column([
  [sg.Text('送り状')],
  [sg.Text('ID', size=(10,1)), sg.InputText(id, key="-ID-", size=(10,1))],
  [sg.Text('日付', size=(10,1)), sg.InputText('', key="-日付-", size=(20,1)), sg.Button(button_text='日付',key="日付")],

  [sg.Text('商品id', size=(10,1)), sg.InputText('', key="-商品id-", size=(20,1))],
  [sg.Text('商品名前', size=(10,1)), sg.InputText('', key="-商品名前-", size=(20,1))],
  [sg.Text('下代', size=(10,1)), sg.InputText('', key="-下代-", size=(20,1))],
  # コンボボックス
  [sg.Text('消費税', size=(10, 1)), sg.Combo(消費税(), enable_events=True, key="-消費税-", size=(50, 5))],
])

購入者 = sg.Column([
  [sg.Text('購入者')],
  [sg.Text('名前', size=(10, 1)), sg.InputText('', key="-名前-", size=(20,1))],
  [sg.Text('ペンネーム', size=(10, 1)), sg.InputText('', key="-ペンネーム-", size=(20, 1))],
  [sg.Text('住所', size=(10,1)), sg.Multiline('', key="-住所-", size=(50, 5))],
  [sg.Text('メールアドレス', size=(10,1)), sg.InputText('', key="-メールアドレス-", size=(20,1))],

])

送付先 = sg.Column([
  [sg.Text('購入者')],
  [sg.Text('名前', size=(10, 1)), sg.InputText('', key="-名前-", size=(20,1))],
  [sg.Text('ペンネーム', size=(10, 1)), sg.InputText('', key="-ペンネーム-", size=(20, 1))],
  [sg.Text('住所', size=(10,1)), sg.Multiline('', key="-住所-", size=(50, 5))],
  [sg.Text('メールアドレス', size=(10,1)), sg.InputText('', key="-メールアドレス-", size=(20,1))],
])

フッター = sg.Column([
  [sg.Text('コメント', size=(10,1)), sg.Multiline(default_text="", size=(50, 5), key="-コメント-"), sg.Button(button_text='新規保存', key="-新規保存-"), sg.Button(button_text='保存', key="-保存-"), sg.Button(button_text='読了', key="-読了-"), sg.Button(button_text='閉じる', key="-閉じる-")],
  [sg.Text('過去ログ', size=(10,1)), sg.Listbox(過去ログ(), enable_events=True, size=(200, 10), key='-過去ログ-'), sg.Button(button_text='読み込み', key="-読み込み-")],
  ])

個人情報 = sg.Column([
    [購入者, 送付先],
])

L = [
    [sg.Pane([ヘッダー])],
    [sg.Pane([左, 個人情報])],
    [sg.Pane([フッター])],
    ]

# ウィンドウを作成する
window = sg.Window('通販Editor', L, resizable=True)

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

    elif event == "-過去ログ-":
        過去ログ2()
    elif event == "-新規保存-":
        新規保存()
    elif event == "-保存-":
        保存()


    elif event == "-読了-":
        window["-読了-"].update("読了")
    elif event == "-閉じる-":
        break

    print(event, values)
    # Output a message to the window
    #window['-出力-'].update('ハロー ' + values['-入力-'] + "! PySimpleGUI をお試しいただきありがとうございます")

# 画面から削除して終了
window.close()