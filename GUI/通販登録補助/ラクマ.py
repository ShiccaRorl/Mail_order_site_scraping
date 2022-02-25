# -*- encoding: utf-8 -*-

# 007 2022/02/08 テンプレートのテンプレートを作ることにした。
#     2022/02/09 coreを追加した。configに。
#     2022/02/09 GUIにするのに、二日かかってしまった。やっぱりシンプルが一番
# 008 2022/02/11 一から始めたいと思います。
import PySimpleGUI as sg
import datetime
import configparser
import math
import os
import re
import time

from sqlalchemy.ext.automap import automap_base
from sqlalchemy import *
from sqlalchemy import func
from sqlalchemy.orm import *
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import subprocess

#from config import Config
import time


class Config:
    def __init__(self):

        # --------------------------------------------------
        # read_file()関数によるiniファイルの読み込み
        # --------------------------------------------------
        config_ini = configparser.ConfigParser()
        config_ini_path = './config.ini'

        # iniファイルが存在するかチェック
        if os.path.exists(config_ini_path):
            # iniファイルが存在する場合、ファイルを読み込む
            with open(config_ini_path, encoding='utf-8') as fp:

                config_ini.read_file(fp)

                read_default = config_ini['DEFAULT']

                self.driver = read_default.get('driver')
                self.username = read_default.get('username')
                self.password = read_default.get('password')
                self.host = read_default.get('host')
                self.port = read_default.get('port')
                self.database = read_default.get('database')
                # self.db_path_access1 = self.db_path_access1.replace('"', '')

                read_SQLite3 = config_ini['SQLite3']
                self.path = read_SQLite3.get('path')
        else:
            print("iniファイルがない")

        # DB関係

        self.Base = automap_base()
        # postgresql://scott:tiger@localhost/mydatabase

        # 接続文字列
        self.engine = create_engine(f'sqlite:///{self.path}', echo=True)
        # self.engine = create_engine(f'{self.driver}://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}')

        # self.Base = declarative_base(bind=self.engine)
        self.Base.prepare(self.engine, reflect=True)
# pip install sqlalchemy
# pip install psycopg2
# pip install PySimpleGUI

# 一応動くバージョン

# DB 接続文字列


class 基本設定:
    def __init__(self, main_table):
        self.メインテーブル = main_table
        self.サブテーブル = None
        self.config = Config()


    def set_main_table(self, table):
        print("main table")
        self.メインテーブル = table

    def set_sub_table(self, table):
        self.サブテーブル = table


class 基本コマンド(基本設定):
    def __init__(self, main_table):
        super().__init__(main_table)

    def 過去ログ(self):
        # 過去ログテーブル　の計算
        session = Session(self.config.engine)
        過去ログ = session.query(self.メインテーブル).order_by(desc(self.メインテーブル.id)).all()
        # ウィンドウの内容を定義する
        # 画面レイアウトを指定

        member_list = []

        # print(t)
        for i in 過去ログ:
            member_list.append([i.id, i.コメント])
        session.close()
        return member_list

    def 削除(self):
        t = sg.popup_ok_cancel('削除します')
        print(t)
        if t == "OK":
            sg.popup_ok_cancel(t)
            id = self.values["-ID-"]

            session = Session(self.config.engine)
            s = session.query(self.メインテーブル).filter(self.メインテーブル.id == int(id)).first()
            if s != None:
                session.delete(s)

                session.commit()
                sg.popup('削除しました。')
                session.close()
            self.window["-過去ログ-"].update(self.過去ログ())
        elif t == "Cancel":
            sg.popup_ok_cancel(t)
            print("Cancel")
        else:
            sg.popup(t)

    def space_filter(self, data):
        data = data.replace(' ', '')
        data = data.replace('　', '')
        return data

    def max_id(self):
        # 過去ログテーブル　の計算
        session = Session(self.config.engine)
        ids = session.query(self.メインテーブル).all()
        # 最大値の計算
        i = []
        try:
            for s in ids:
                i.append(s.id)
            session.close()
            return max(i) + 1
        except:
            return 1

    def 過去ログ2(self):
        # == 野菜一覧↓ ==
        try:
            list = self.values["-過去ログ-"]
            id = list[0][0]

            session = Session(self.config.engine)
            t = session.query(self.メインテーブル).filter(self.メインテーブル.id == int(id)).first()

            self.window["-ID-"].update(t.id)
            try:
                self.window["-日付-"].update(t.日付)
            except:
                print()
            try:
                self.window["-開始時間-"].update(re.split("\.", str(t.開始時間))[0].replace("+00:00", ""))
            except:
                print()
            try:
                self.window["-終了時間-"].update(re.split("\.", str(t.終了時間))[0].replace("+00:00", ""))
            except:
                print()
            try:
                self.window["-間時間-"].update(re.split("\.", str(t.終了時間 - t.開始時間))[0].replace("+00:00", ""))
            except:
                print()

        except:
            sg.PopupError('！過去ログエラー！')
            self.window["-過去ログ-"].update(self.過去ログ())
        session.close()

    def 保存(self):
        print("保存")
        print(self.values["-ID-"])
        try:
            session = Session(self.config.engine)
            if session.query(self.メインテーブル).filter(self.メインテーブル.id == int(self.values["-ID-"])).first() == None:
                print("insert")
                i = self.メインテーブル()
                i.日付 = self.values["-日付-"]
                i.開始時間 = self.timebox.in_start_text_to_time(self.values["-開始時間-"])
                i.終了時間 = self.timebox.in_end_text_to_time(self.values["-終了時間-"])
                i.間時間 = self.timebox.in_間_text_to_time(self.values["-間時間-"])

                i.本_CODE = self.values["-本CODE-"]
                i.タイトル = self.values["-本タイトル2-"]
                i.page = int(self.values["-ページ-"])
                i.気付き1 = self.space_filter(self.values["-気付き1-"])
                i.気付き2 = self.space_filter(self.values["-気付き2-"])
                i.気付き3 = self.space_filter(self.values["-気付き3-"])

                i.コメント = values["-コメント-"]
                session.add(i)
                session.commit()
                session.close()
                self.window["-過去ログ-"].update(self.過去ログ())
                sg.popup_ok('保存完了')

            else:
                print("updata")
                i = session.query(self.メインテーブル).filter(self.メインテーブル.id == int(self.values["-ID-"])).first()

                i.日付 = self.values["-日付-"]
                i.開始時間 = self.timebox.in_start_text_to_time(self.values["-開始時間-"])
                i.終了時間 = self.timebox.in_end_text_to_time(self.values["-終了時間-"])
                i.間時間 = self.timebox.in_間_text_to_time(self.values["-間時間-"])

                i.本_CODE = self.values["-本CODE-"]
                i.タイトル = self.values["-本タイトル2-"]
                i.page = int(self.values["-ページ-"])
                i.気付き1 = self.space_filter(self.values["-気付き1-"])
                i.気付き2 = self.space_filter(self.values["-気付き2-"])
                i.気付き3 = self.space_filter(self.values["-気付き3-"])

                i.コメント = self.values["-コメント-"]
                session.add(i)
                session.commit()
                session.close()
                self.window["-過去ログ-"].update(self.過去ログ())
                sg.popup_ok('保存完了')

        except:
            sg.PopupError('！エラー発生！')

    def 新規保存(self):
        try:
            session = Session(self.config.engine)
            i = self.メインテーブル()
            i.id = self.max_id()
            i.日付 = self.values["-日付-"]
            i.開始時間 = self.timebox.in_start_text_to_time(self.values["-開始時間-"])
            i.終了時間 = self.timebox.in_end_text_to_time(self.values["-終了時間-"])
            i.間時間 = self.timebox.in_間_text_to_time(self.values["-間時間-"])

            i.本_CODE = self.values["-本CODE-"]
            i.タイトル = self.values["-本タイトル2-"]
            i.page = int(self.values["-ページ-"])
            i.気付き1 = self.space_filter(self.values["-気付き1-"])
            i.気付き2 = self.space_filter(self.values["-気付き2-"])
            i.気付き3 = self.space_filter(self.values["-気付き3-"])

            i.コメント = self.values["-コメント-"]
            session.add(i)
            session.commit()
            session.close()
            sg.popup_ok('保存完了')
            self.window["-過去ログ-"].update(self.過去ログ())
        except:
            session.close()
            sg.PopupError('新規保存エラー発生！')
        self.window["-過去ログ-"].update(self.過去ログ())

    def 本タイトル(self):
        # リストボックス　本タイトルの計算
        session = Session(self.config.engine)
        t_07_本 = self.config.Base.classes.LifeLog_t_07_本
        過去タイトル = session.query(t_07_本).filter(t_07_本.やりかけ == True).order_by(desc(t_07_本.閲覧日)).all()
        i = []
        for s in 過去タイトル:
            if s == None or s == []:
                print()
            else:
                i.append([s.本_CODE, s.タイトル, s.買った, s.amazonプライム])
        過去タイトル = i
        return 過去タイトル

    def 本タイトル2(self):
        # コンボボックス　本タイトルの計算
        session = Session(self.config.engine)
        t_07_本 = self.config.Base.classes.LifeLog_t_07_本
        過去タイトル = session.query(t_07_本.タイトル, func.count(t_07_本.タイトル)).group_by(t_07_本.タイトル).all()
        i = []
        for s in 過去タイトル:
            i.append(s.タイトル)
        過去タイトル = i
        print(i)
        return 過去タイトル

    def id順(self):
        session = Session(self.config.engine)
        t_07_本 = self.config.Base.classes.LifeLog_t_07_本
        過去タイトル = session.query(t_07_本).order_by(t_07_本.id).all()
        i = []
        for s in 過去タイトル:
            if s == "" or s == None:
                print()
            else:
                i.append([s.本_CODE, s.タイトル])
        過去タイトル = i
        self.window["-本タイトル-"].update(過去タイトル)
        return 過去タイトル

    def 図書館(self):
        session = Session(self.config.engine)
        t_07_本 = self.config.Base.classes.LifeLog_t_07_本
        過去タイトル = session.query(t_07_本).filter(t_07_本.借り物 == True, t_07_本.やりかけ == True).order_by(t_07_本.id).all()
        i = []
        for s in 過去タイトル:
            if s == "" or s == None:
                print()
            else:
                i.append([s.本_CODE, s.タイトル])
        過去タイトル = i
        self.window["-本タイトル-"].update(過去タイトル)
        return 過去タイトル

    def Amazon(self):
        session = Session(self.config.engine)
        t_07_本 = self.config.Base.classes.LifeLog_t_07_本
        過去タイトル = session.query(t_07_本).filter(t_07_本.amazonプライム == True, t_07_本.やりかけ == True).order_by(t_07_本.id).all()
        i = []
        for s in 過去タイトル:
            if s == "" or s == None:
                print()
            else:
                i.append([s.本_CODE, s.タイトル])
        過去タイトル = i
        self.window["-本タイトル-"].update(過去タイトル)
        return 過去タイトル


class 基本レイアウト(基本コマンド):
    def __init__(self, main_table):
        super().__init__(main_table)

    def get_layout(self):
        main1 = [
            # コンボボックス
            [sg.Text('ラクマエディター', size=(30, 1), font=('Noto Serif CJK JP', 15)), ],

            [sg.Text('タイトル', size=(30, 1)), sg.InputText('', key="-タイトル-", size=(40, 1))],
            [sg.Text('テキスト', size=(10, 1), ), sg.Text("", size=(5, 3), key="-テキスト-"), ],

            [sg.Checkbox('柄有り', size=(20, 1),), ],
            [sg.Checkbox('バリエーション有り', size=(20, 1))],
            [sg.Button("保存",key="-保存-")],
            [sg.Text('過去ログ', size=(10,1)), sg.Listbox([0,0], enable_events=True, size=(70, 7), key='-過去ログ-'),]
        ]

        self.L = [
            # タブ化
            #[[sg.TabGroup([[sg.Tab('Timer', main1), sg.Tab('Settings', main2)]])]]
            main1
        ]
        return self.L


class 基本イベント(基本レイアウト):
    def __init__(self, main_table):
        super().__init__(main_table)
        self.メインテーブル = main_table


    def get_event(self):
        レイアウト = 基本レイアウト(self.メインテーブル)
        self.L = レイアウト.get_layout()
        # ウィンドウを作成する
        self.window = sg.Window(f'ラクマエディター', self.L,)

        # イベントループを使用してウィンドウを表示し、対話する
        while True:
            event, self.values = self.window.read(timeout=100, timeout_key='-timeout-')
            # ユーザーが終了したいのか、ウィンドウが閉じられたかどうかを確認してください
            if event == sg.WINDOW_CLOSED or event == '終了' or event == "-閉じる-":
                break
            elif event == "-過去ログ-":
                self.過去ログ2()
            elif event == "-新規保存-":
                self.新規保存()
            elif event == "-保存-":
                self.保存()

            elif event == "-空id検索-":
                self.空id検索()
            elif event == "-削除-":
                self.削除()

            elif event == "-本タイトル-":
                self.window["-本CODE-"].update(self.values["-本タイトル-"][0][0])
                self.window["-本タイトル2-"].update(self.values["-本タイトル-"][0][1])
            elif event == "-id順-":
                self.id順()




            elif event == "-モード-":
                self.window["-モード-"].update()
            elif event == "-只今の時間-":
                self.window["-只今の時間-"].update(datetime.datetime.now())
            elif event == "-次のフェーズまで-":
                self.window["-次のフェーズまで-"].update()
            elif event == "-切り替え-":
                self.start_timer = time.time()
                if self.mode == None or self.mode == "" or self.mode == []:
                    self.mode = "覚醒"
                if self.mode == "睡眠":
                    self.window["-モード-"].update("覚醒")
                    self.mode = "覚醒"
                    # データベースに保存する
                elif self.mode == "覚醒":
                    self.window["-モード-"].update("睡眠")
                    self.mode = "睡眠"
                    # データベースに保存する
                else:
                    print("???")

            elif event == "-Debug-":
                subprocess.Popen(["C:/Program Files/Notepad++/notepad++.exe", f"./aAnime.py", f"{id}"], shell=True)

            elif event == "-閉じる-":
                break

            elif event in '-timeout-':
                time_value = time.strftime('%H:%M:%S')
                self.window["-只今の時間-"].update(time_value)

                timer = time.time() - self.start_timer
                if self.max_timer == None or self.max_timer == "" or self.max_timer == []:
                    self.max_timer = 30 * 60 * 60
                try:
                    sa = self.max_timer - timer
                    self.window["-次のフェーズまで-"].update(sa.strftime('%H:%M:%S'))
                except:
                    pass
            time.sleep(1)
            print(event, self.values)
            # Output a message to the window
            # window['-出力-'].update('ハロー ' + values['-入力-'] + "! PySimpleGUI をお試しいただきありがとうございます")

        # 画面から削除して終了
        self.window.close()


class まとめ:
    def __init__(self, main_table):
        self.event = 基本イベント(main_table)

    def set_メインテーブル(self, table_name):
        self.event.set_main_table(table_name)

    def set_サブテーブル(self, table_name):
        self.set_sub_table(table_name)

    def run(self):
        # self.layouts.get_layout()
        self.event.get_event()


if __name__ == '__main__':
    config = Config()
    generator = config.Base.classes.generator_generator
    まとめ = まとめ(generator)

    まとめ.run()
