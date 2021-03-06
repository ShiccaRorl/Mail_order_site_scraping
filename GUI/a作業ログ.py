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
#from peewee import *
#from LifeLog_models import *


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

def 本タイトル2():
    # コンボボックス　本タイトルの計算
    session = Session(config.engine)
    t_07_本 = config.Base.classes.LifeLog_t_07_本
    過去タイトル = session.query(t_07_本.タイトル, func.count(t_07_本.タイトル)).group_by(t_07_本.タイトル).all()
    i = []
    for s in 過去タイトル:
        i.append(s.タイトル)
    過去タイトル = i
    return 過去タイトル

def 本ファイル名():
    # コンボボックス　本ファイル名の計算
    session = Session(config.engine)
    t_206_warez倉庫 = config.Base.classes.LifeLog_t_206_warez倉庫
    過去ファイル名 = session.query(t_206_warez倉庫).filter(t_206_warez倉庫.やりかけ == True).order_by(desc(t_206_warez倉庫.閲覧日)).all()
    i = []
    for s in 過去ファイル名:
        i.append(s.ファイル名)
    過去ファイル名 = i
    return 過去ファイル名

def max_id():
    # 過去ログテーブル　の計算
    session = Session(config.engine)
    過去ログ = session.query(t_07_読書).order_by(desc(t_07_読書.日付)).limit(30)
    #過去ログ = LifeLogT07読書.select().order_by(LifeLogT07読書.日付).limit(30)
    # 最大値の計算
    i = []
    try:
        for s in 過去ログ:
            i.append(s.id)
        return max(i) + 1
    except:
        return 1

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
        print("保存")
        print(values["-ID-"])
        try:
            session = Session(config.engine)
            if session.query(t_07_読書).filter(t_07_読書.id == values["-ID-"]).first() == None:
                print("insert")
                session.add(t_07_読書(id = max_id(),
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
                ))
                session.commit()
                window["-過去ログ-"].update(過去ログ())
                sg.popup_ok('保存完了')
            else:
                print("updata")
                読書 = session.query(t_07_読書).filter(t_07_読書.id == values["-ID-"]).first()
                
                読書.id = values["-ID-"],
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

def 新規保存():
    try:
        session = Session(config.engine)
        session.add(t_07_読書(id = max_id(),
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
                ))
        session.commit()
        sg.popup_ok('保存完了')
        window["-過去ログ-"].update(過去ログ())
    except:
        sg.PopupError('！エラー発生！')
        window["-過去ログ-"].update(過去ログ())
    


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
  [sg.Text('テンプレート管理')],
  [sg.Text('ID', size=(10,1)), sg.InputText(id, key="-ID-", size=(10,1))],
  [sg.Text('日付', size=(10,1)), sg.InputText('', key="-日付-", size=(20,1)), sg.Button(button_text='日付',key="日付")],
  [sg.Text('開始時間', size=(10,1)), sg.InputText('', key="-開始時間-", size=(20,1)), sg.Button(button_text='開始時間',key="開始時間")],
  [sg.Text('終了時間', size=(10,1)), sg.InputText('', key="-終了時間-", size=(20,1)), sg.Button(button_text='終了時間',key="終了時間")],
  [sg.Text('間時間', size=(10,1)), sg.InputText('', key="-間時間-", size=(20,1)), sg.Button(button_text='間時間',key="間時間")],
  
  # コンボボックス
  [sg.Text('タイトル', size=(10, 1)), sg.Combo(本タイトル2(), enable_events=True, key="-タイトル2-", size=(50, 5))],

  [sg.Text('タイトル', size=(10, 1)), sg.Listbox(本タイトル(), enable_events=True, key="-タイトル-", size=(50, 5)), 
  sg.Text('ファイル名', size=(10,1)), sg.Listbox(本ファイル名(), enable_events=True, key="-ファイル名-", size=(50, 5))],
  
  [sg.Text('ページ', size=(10,1)), sg.InputText(default_text="", key="-ページ-")],
  [sg.Text('気付き1', size=(10,1)), sg.Multiline(default_text="", size=(50, 5), key="-気付き1-")],
  [sg.Text('気付き2', size=(10,1)), sg.Multiline(default_text="", size=(50, 5), key="-気付き2-")],
  [sg.Text('気付き3', size=(10,1)), sg.Multiline(default_text="", size=(50, 5), key="-気付き3-")],
  [sg.Text('コメント', size=(10,1)), sg.Multiline(default_text="", size=(50, 5), key="-コメント-"), sg.Button(button_text='新規保存', key="-新規保存-"), sg.Button(button_text='保存', key="-保存-"), sg.Button(button_text='読了', key="-読了-"), sg.Button(button_text='閉じる', key="-閉じる-")],
  [sg.Text('過去ログ', size=(10,1)), sg.Listbox(過去ログ(), enable_events=True, size=(200, 10), key='-過去ログ-'), sg.Button(button_text='読み込み', key="-読み込み-")],
  ]

# ウィンドウを作成する
window = sg.Window('テンプレート管理', layout, resizable=True)

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