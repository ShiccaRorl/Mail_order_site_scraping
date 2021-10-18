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


t_07_読書 = config.Base.classes.LifeLog_t_07_読書

#Session = sessionmaker(bind=config.engine)
#session = Session(config.engine)

def 過去ログ(data=None):
    print(data)
    # 過去ログテーブル　の計算
    session = Session(config.engine)
    過去ログ = session.query(t_07_読書).order_by(desc(t_07_読書.日付)).limit(30)
    # ウィンドウの内容を定義する
    # 画面レイアウトを指定


    member_list = []

    #print(t)
    for i in 過去ログ:
        member_list.append([i.id, i.日付, i.タイトル, i.コメント])
    return member_list


def 本タイトル():
    # コンボボックス　本タイトルの計算
    session = Session(config.engine)
    t_07_本 = config.Base.classes.LifeLog_t_07_本
    過去タイトル = session.query(t_07_本).filter(t_07_本.やりかけ == True).order_by(desc(t_07_本.日付)).all()
    i = []
    for s in 過去タイトル:
        i.append(s.タイトル)
    過去タイトル = i
    return 過去タイトル


def max_id():
    # 過去ログテーブル　の計算
    session = Session(config.engine)
    過去ログ = session.query(t_07_読書).order_by(desc(t_07_読書.日付)).limit(30)
    #過去ログ = LifeLogT07読書.select().order_by(LifeLogT07読書.日付).limit(30)
    # 最大値の計算
    i = []
    for s in 過去ログ:
        i.append(s.id)
    return max(i) + 1

def 保存():
        values["-日付-"] = datetime.date.today()
        日付 = datetime.date.today()
        start_time = datetime.datetime.now()
        end_time = datetime.datetime.now()
        if values["-日付-"] == None:
            values["-日付-"] = datetime.date.today()
        if start_time == None:
            start_time = datetime.datetime.now()
        if end_time == None:
            end_time = datetime.datetime.now()

        try:
            session = Session(config.engine)
            if session.query(t_07_読書).filter(t_07_読書.id == values["-ID-"]).order_by(desc(t_07_読書.日付)).first() == None:
                session.query(t_07_読書).insert(id = max_id(),
                                            日付 = values["-日付-"],
                                            開始時間 = values["-開始時間-"],
                                            終了時間 = values["-終了時間-"],
                                            間時間 = values["-間時間-"],
                                            タイトル = values["-タイトル-"],
                                            ファイル名 = values["-ファイル名-"],
                                            page = values["-ページ-"],
                                            気付き1 = values["-気付き1-"],
                                            気付き2 = values["-気付き2-"],
                                            気付き3 = values["-気付き3-"],
                                            コメント = values["-コメント-"],
                )
                session.commit()
                window["-過去ログ-"].update(過去ログ())
                sg.popup_ok('保存完了')
            else:
                読書 = session.query(t_07_読書).filter(t_07_読書.id == values["-ID-"]).first()
                
                読書.日付 = values["-日付-"],
                読書.開始時間 = values["-開始時間-"],
                読書.終了時間 = values["-終了時間-"],
                読書.間時間 = values["-間時間-"],
                読書.タイトル = values["-タイトル-"],
                読書.ファイル名 = values["-ファイル名-"],
                読書.page = values["-ページ-"],
                読書.気付き1 = values["-気付き1-"],
                読書.気付き2 = values["-気付き2-"],
                読書.気付き3 = values["-気付き3-"],
                読書.コメント = values["-コメント-"],
                session.commit()
                window["-過去ログ-"].update(過去ログ())
                sg.popup_ok('保存完了')
        except:
            sg.PopupError('！エラー発生！')

def list更新():
    print("update")

def 読了():
    print("update")

def コピー():
    print("update")

def 過去ログ2():
    # == 過去ログ↓ ==
        list = values["-過去ログ-"]
        id = list[0][0]
        session = Session(config.engine)
        t = session.query(t_07_読書).filter(t_07_読書.id == id).first()
        id = t.id
        日付 = t.日付
        開始時間 = t.開始時間
        終了時間 = t.終了時間
        間時間 = t.間時間
        タイトル = t.タイトル
        ファイル名 = t.ファイル名
        ページ = t.page
        気付き1 = t.気付き1
        気付き2 = t.気付き2
        気付き3 = t.気付き3
        コメント = t.コメント

        if id == None or id == "":
            id = 0
        if 日付 == None or 日付 == "":
            日付 = ""
        if 開始時間 == None or 開始時間 == "":
            開始時間 = ""
        if 終了時間 == None or 終了時間 == "":
            終了時間 = ""
        if 間時間 == None or 間時間 == "":
            間時間 = ""
        if タイトル == None or タイトル == "":
            タイトル = ""
        if ファイル名 == None or ファイル名 == "":
            ファイル名 = ""
        if ページ == None or ページ == "":
            ページ = ""
        if 気付き1 == None or 気付き1 == "":
            気付き1 = ""
        if 気付き2 == None or 気付き2 == "":
            気付き2 = ""
        if 気付き3 == None or 気付き3 == "":
            気付き3 = ""
        if コメント == None or コメント == "":
            コメント = ""
        window["-ID-"].update(id)
        window["-日付-"].update(日付)
        window["-開始時間-"].update(開始時間)
        window["-終了時間-"].update(終了時間)
        window["-間時間-"].update(間時間)
        values["-タイトル-"] = タイトル
        values["-ファイル名-"] = ファイル名
        window["-ページ-"].update(ページ)
        window["-気付き1-"].update(気付き1)
        window["-気付き2-"].update(気付き2)
        window["-気付き3-"].update(気付き3)
        window["-コメント-"].update(コメント)
        # == 過去ログ↑ ==


id = max_id()


layout = [
  [sg.Text('通販管理')],
  [sg.Text('ID', size=(10,1)), sg.InputText(id, key="-ID-", size=(10,1))],
  [sg.Text('日付', size=(10,1)), sg.InputText('', key="-日付-", size=(20,1)), sg.Button(button_text='日付',key="日付")],
  [sg.Text('開始時間', size=(10,1)), sg.InputText('', key="-開始時間-", size=(20,1)), sg.Button(button_text='開始時間',key="開始時間")],
  [sg.Text('終了時間', size=(10,1)), sg.InputText('', key="-終了時間-", size=(20,1)), sg.Button(button_text='終了時間',key="終了時間")],
  #[sg.Text('間時間', size=(10,1)), sg.InputText('', key="-間時間-", size=(20,1)), sg.Button(button_text='間時間',key="間時間")],
  
  # コンボボックス
  #[sg.Text('タイトル', size=(10, 1)), sg.Combo(本タイトル2(), enable_events=True, key="-タイトル2-", size=(50, 5))],

  
  [sg.Text('データ取り込み', size=(10,1)), sg.Button(button_text='データ取り込み', key="-データ取り込み-")],
  [sg.Text('サイト', size=(10,1)), sg.Button(button_text='Amazon', key="-Amazon-"), sg.Button(button_text='ヤフオク', key="-ヤフオク-"), sg.Button(button_text='楽天', key="-楽天-"), sg.Button(button_text='ラクマ', key="-ラクマ-"), sg.Button(button_text='ストアーズ', key="-ストアーズ-")],
  #[sg.Text('気付き3', size=(10,1)), sg.Multiline(default_text="", size=(50, 5), key="-気付き3-")],
  [sg.Text('コメント', size=(10,1)), sg.Multiline(default_text="", size=(50, 5), key="-コメント-"), sg.Button(button_text='保存', key="-保存-"), sg.Button(button_text='読了', key="-読了-"), sg.Button(button_text="コピー", key="-コピー-"), sg.Button(button_text='閉じる', key="-閉じる-")],

  [sg.Text('過去ログ', size=(10,1)), sg.Listbox(過去ログ(), enable_events=True, size=(100, 10), key='-過去ログ-')],
  ]

# ウィンドウを作成する
window = sg.Window('読書時間管理', layout, resizable=True)

# == 時間↓ ==
start_time = Timebox()
end_time = Timebox()

# イベントループを使用してウィンドウを表示し、対話する
while True:
    event, values = window.read()
# ユーザーが終了したいのか、ウィンドウが閉じられたかどうかを確認してください
    if event == sg.WINDOW_CLOSED or event == '終了' or event == "閉じるb":
        break
    elif event == "日付":
        window["-日付-"].update(start_time.in_to_text(datetime.date.today()))
        日付 = datetime.date.today()

    elif event == "開始時間":
        window["-開始時間-"].update(start_time.in_to_text(datetime.datetime.now()))

    elif event == "終了時間":
        window["-終了時間-"].update(end_time.in_to_text(datetime.datetime.now()))

    elif event == "間時間":
        print(end_time.in_time(values["-終了時間-"]))
        print(start_time.in_time(values["-開始時間-"]))

        ma_datetime = (end_time.in_time(values["-終了時間-"]) - start_time.in_time(values["-開始時間-"]))
        if (end_time.in_time(values["-終了時間-"]) - start_time.in_time(values["-開始時間-"])).seconds < 60*60*6:
            ma_datetime = ("1970/01/01 00:00:00")

        # window["-間時間-"].update(end_time.in_time(values["-終了時間-"]) - start_time.in_time(values["-開始時間-"]))
        window["-間時間-"].update(ma_datetime)
        # == 時間↑ ==

    elif event == "-過去ログ-" or event == "-読み込み-":
        過去ログ2()
    elif event == "-保存-":
        保存()


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