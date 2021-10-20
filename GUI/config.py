# -*- encoding: utf-8 -*-

import configparser

import PySimpleGUI as sg
import datetime

from sqlalchemy import * 
from sqlalchemy.orm import *
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# pip install psycopg2
# pip install sqlalchemy

# ファイルの存在チェック用モジュール
import os
import errno


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
        #self.engine = create_engine(f'{self.driver}://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}')
        
        #self.Base = declarative_base(bind=self.engine)
        self.Base.prepare(self.engine, reflect=True)

        """
        # peewee
        self.db = PostgresqlDatabase(
            'LifeLog',  # Required by Peewee.
            user='root',  # Will be passed directly to psycopg2.
            password='root',  # Ditto.
            host='192.168.10.8',  # Ditto.
            port='5432',
        )
        
        #self.db = PostgresqlDatabase('LifeLog', user='root')
        self.db = PostgresqlExtDatabase(
        database='LifeLog',
        user='root',
        password="root",
        host="192.168.10.8",
        port=5432,
        register_hstore=False)
        """
        
class Timebox():
    def __init__(self):
        self.day = datetime.date.today()
        self.start_datetime = datetime.datetime.now()
        self.end_datetime = datetime.datetime.now()
        self.ma_time = self.end_datetime - self.start_datetime

    def in_to_text_day(self, day):
        # 日付データをテキストに成形して戻す Datetime→文字列
        self.day = day
        return day.strftime('%Y/%m/%d %H:%M:%S')

    def in_to_text_start(self,datetime):
        # 日付データをテキストに成形して戻す Datetime→文字列
        self.start_datetime = datetime
        return datetime.strftime('%Y/%m/%d %H:%M:%S')

    def in_to_text_end(self,datetime):
        # 日付データをテキストに成形して戻す Datetime→文字列
        self.end_datetime = datetime
        return datetime.strftime('%Y/%m/%d %H:%M:%S')

    def in_time(self, data_moji):
        # 文字列をdatetimeに変換する 文字列→Datetime
        print(data_moji)
        try:
            self.end_datetime = datetime.datetime.strptime(data_moji, '%Y/%m/%d %H:%M:%S')
        except:
            print("文字列が違います。")
            return None
        return self.end_datetime

    def out_timedelta(self):
        # 文字列を時間にして引き算
        self.day.replace('-', '/').replace('+00:00', '')
        self.start_datetime.replace('-', '/').replace('+00:00', '')
        self.end_datetime.replace('-', '/').replace('+00:00', '')
            
        try:
            print(timebox.start_datetime)
            print(timebox.end_datetime)

            self.ma_time = timebox.end_datetime - timebox.start_datetime
            if self.ma_time.seconds < 60*60*6:
                self.ma_time = ("1970/01/01 00:00:00")

            return self.ma_time
        except:
            sg.PopupError('！日付計算エラー！')

if __name__ == '__main__':
    config = Config()
    timebox = Timebox()
    print(timebox.in_time("2021/10/11 03:38:00"))
    print(timebox.out_time("2021/10/11 03:38:00"))
    print(timebox.out_timedelta("03:00:00"))