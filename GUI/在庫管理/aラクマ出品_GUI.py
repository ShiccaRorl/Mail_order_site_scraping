# -*- coding:utf-8 -*-

import PySimpleGUI as sg
import datetime
import math
import subprocess


from sqlalchemy.ext.automap import automap_base
from sqlalchemy import *
from sqlalchemy import func
from sqlalchemy.orm import *
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


#from config import Config, Timebox
# pip install sqlalchemy
# pip install psycopg2
# pip install PySimpleGUI

from config import Config
#help(sg.Table)

#config = Config()


#sale_sele = config.Base.classes.sale_sele
"""
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
"""

def 取引リスト():
    return ['test', 'test']



ヘッダー = sg.Column([
    [sg.Text('ラクマEditer')],
    [sg.InputText('', key="-データ取り込みtxt1-", size=(20, 1)), sg.FilesBrowse('データ取り込み1', key='-FILES1-', file_types=(("ラクマHtmlファイル", "*.html"),)), sg.Button(button_text='解析',key="-解析1-")],
    [sg.InputText('', key="-データ取り込みtxt2-", size=(20, 1)), sg.FilesBrowse('データ取り込み2', key='-FILES2-', file_types=(("ラクマHtmlファイル", "*.html"),)), sg.Button(button_text='解析',key="-解析2-")],
    [sg.Text('並び替え')],
    [sg.Button(button_text='そのまま',key="-そのまま-"), sg.Button(button_text='B品順',key="-B品順-"),
     sg.Button(button_text='在庫1',key="-在庫1-"), sg.Button(button_text='売れ筋??',key="-売れ筋-"), sg.Button(button_text='ソート',key="-ソート-"),],
    [sg.Text('商品リスト', size=(10,1)), sg.InputText('', key="-商品コード-", size=(10, 1))],
])

中央 = sg.Column([
  #[sg.Text('ラクマEditer')],
  #[sg.Text('ID', size=(10,1)), sg.InputText(id, key="-ID-", size=(10,1))],
  [sg.Text('日付', size=(10,1)), sg.InputText(datetime.date.today(), key="-日付-", size=(10,1)), sg.Button(button_text='日付',key="-日付-")],
  #[sg.Text('ファイルデータベース取り込み', size=(10,1)), sg.Button(button_text='更新',key="-更新-")],
  [sg.Button(button_text='<=====',key="左"), sg.Button(button_text='フォルダ開く',key="-フォルダ開く-"), sg.Button(button_text='=====>',key="右"),],
])




フッター = sg.Column([
  #[sg.Text('コメント', size=(10,1)), sg.Multiline(default_text="", size=(50, 5), key="-コメント-"), sg.Button(button_text='新規保存', key="-新規保存-"), sg.Button(button_text='保存', key="-保存-"), sg.Button(button_text='読了', key="-読了-"), sg.Button(button_text='閉じる', key="-閉じる-")],
  #[sg.Text('過去ログ', size=(10,1)), sg.Listbox(過去ログ(), enable_events=True, size=(200, 10), key='-過去ログ-'), sg.Button(button_text='読み込み', key="-読み込み-")],
  ])

L = [
    [sg.Pane([ヘッダー])],
    [sg.Pane([中央])],
    [sg.Pane([フッター])],
    ]

# ウィンドウを作成する
window = sg.Window('ラクマEditor', L, resizable=True)

# == 時間↓ ==
#timebox = Timebox()

# イベントループを使用してウィンドウを表示し、対話する
while True:
    event, values = window.read()
    # ユーザーが終了したいのか、ウィンドウが閉じられたかどうかを確認してください
    if event == sg.WINDOW_CLOSED or event == '終了' or event == "閉じるb":
        break
    
    elif event == "-FILES1-":
        dir_pach = "./在庫管理/"
        subprocess.Popen(["zaラクマ_入力テスト.CMD", values['FILES1']], cwd = dir_pach, shell=True)
    
    elif event == "-FILES2-":
        dir_pach = "./在庫管理/"
        subprocess.Popen(["python", "./za_Rakuma_test.py", values['FILES2']], cwd = dir_pach, shell=True)
    
    elif event == "-閉じる-":
        break

    elif event == "-フォルダ開く-":
        subprocess.Popen(["explorer", r"開くフォルダのpath"], shell=True)
    print(event, values)
    # Output a message to the window
    #window['-出力-'].update('ハロー ' + values['-入力-'] + "! PySimpleGUI をお試しいただきありがとうございます")

# 画面から削除して終了
window.close()