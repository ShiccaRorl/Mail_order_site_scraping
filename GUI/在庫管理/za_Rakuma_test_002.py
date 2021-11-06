# -*- coding:utf-8 -*-

# 2021/08/07
# pip install -U sqlalchemy
# pip install -U BeautifulSoup


#from config import Config
#from directory_seed import Mail_order_site

from logging import getLogger, StreamHandler, DEBUG
from bs4 import BeautifulSoup

import datetime
import time
import os
import random
import re
import glob
import sys
import subprocess
import pathlib
import logging

"""
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

#from bs4 import BeautifulSoup
#import subprocess

Base = automap_base()

# engine, suppose it has two tables 'user' and 'address' set up
#engine = create_engine("sqlite:///db.sqlite3")

# reflect the tables
#Base.prepare(engine, reflect=True)

# mapped classes are now created with names by default
# matching that of the table name.

#session = Session(engine)
"""

# 現本から取り込む
#ROOT_PATH = 'C:\\Users\\user\\Downloads\\バックアップ\\プログラム\\バックアップ\\保存\\メルカリ'
#ROOT_PATH = 'R:\\L\\Program\\eclipse\\Python\\Affiliate_RssReadr_7\\www\\DMM_アニメ\\62gbr00015'
ROOT_PATH = '\\\DESKTOP-FK98SN0\\Users\\Public\\Documents\\吉本さんPCから移動したファイル\\メルカリラクマ出品画像\\メルカリ'


class Rakuma_Test():
    def __init__(self):
        args = sys.argv

        try:
            print(len(args))
            if len(args) == 1:
                self.file_path = args[0]
                self.file_out = pathlib.Path(args[0])
                self.ラクマディレクトリ()

            elif len(args) == 2:
                self.file_path = args[1]
                self.file_out = pathlib.Path(args[1])

            elif len(args) == 3:
                self.file_path2 = args[2]
                self.file_out2 = pathlib.Path(args[2])

        except:
            print("データリフレッシュモード")
            self.file_out = pathlib.Path("")
            self.file_out2 = pathlib.Path("")
            # self.ラクマディレクトリ()

        self.logger = getLogger(self.file_path)
        handler = StreamHandler()
        handler.setLevel(DEBUG)
        self.logger.setLevel(DEBUG)
        self.logger.addHandler(handler)
        self.logger.propagate = False

        self.logger.debug('始め')

        self.main()

    def main(self):
        # self.ラクマディレクトリ()
        self.ラクマ出品一覧()
        print("ラクマ出品一覧出力")


    def ラクマディレクトリ(self):
        print(ROOT_PATH + "\\**\\*.txt")
        try:
            i = 0
            for d in glob.glob(ROOT_PATH + "\\**\\*.txt", recursive=True):
                d = d.replace("\\", "/")
                d_path = pathlib.Path(d)
                # print(d_path)
                if i == 0:
                    with open("./ラクマディレクトリ.txt", 'w', encoding="utf-8") as f:
                        f.write(d + "\n")
                        i = 1
                else:
                    with open("./ラクマディレクトリ.txt", 'a', encoding="utf-8") as f:
                        f.write(d + "\n")
        except:
            print("ラクマディレクトリerr")
            self.logger.debug('ラクマディレクトリerr')


    def ラクマ出品一覧(self):
        #try:
            with open(self.file_path, 'r', encoding="utf-8") as f:
                self.seed1 = f.read()

            data = []
            soup = BeautifulSoup(self.seed1, 'html.parser')
            data_soup = soup.find_all("div", attrs={"class": "media-body"})
            for i in data_soup:
                if i != None:
                    t = i.find("span", attrs={"class": "waiting"})
                    if t != None:
                        #try:
                            print(t)
                            m = t.text()
                            if m == "出品中":
                                print("出品中")
                                data.append(i.find("h4", attrs={"class": "media-heading"}))
                            elif m == "売却済み":
                                print("売却済み")
                            else:
                                print("err")
                        #except:
                                #print("")
            #data = data.find("h4", attrs={"class": "media-heading"})
            
            # <div class="media-body">
            # <h4 class="media-heading">新品送料込み　男女兼用　白足袋24.0ｃｍ★成人式、結婚式、卒業式 ATU005</h4>
            
            i = 0
            for d in data:
                # print(d.text)
                print(str(self.file_out.parent) + "\\ラクマ出品一覧.txt")
                if i == 0:
                    with open(str(self.file_out.parent) + "\\ラクマ出品一覧.txt", 'w', encoding="utf-8") as f:
                        f.write(d.text + "\n")
                        i = 1
                else:
                    with open(str(self.file_out.parent) + "\\ラクマ出品一覧.txt", 'a', encoding="utf-8") as f:
                        f.write(d.text + "\n")
        #except:
            print("ラクマ出品一覧err")
            self.logger.debug('ラクマ出品一覧err')



if __name__ == '__main__':
    rakuma_test = Rakuma_Test()

    # while True:
    #    rakuma_test.main()
    #    time.sleep(10)
