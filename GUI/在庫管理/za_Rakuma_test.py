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
            self.ラクマディレクトリ()
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
        #self.商品番号取得()
        print("ラクマ出品一覧出力")

        subprocess.run("ruby zaラクマ_入力テスト.rb " + str(self.file_out.parent), shell=True, text=True)

        print("二重登録された時のリスト")
        self.ラクマ登録２重チェック()
        
        print("全体の在庫０リスト")
        self.在庫0商品リスト()
        
        print("全体の在庫1リスト")
        self.在庫1商品リスト()
        
        print("全体 - （在庫0　+　出品されているリスト）")
        self.登録出来ていない商品チェック()
        
        print("出品されているB品")
        self.出品されているB品のリスト()
        
        print("出品されている在庫1")
        self.出品されている在庫1のリスト()
        
        print("出品されているリストに在庫0が含まれている時のリスト")
        self.出品されているのに在庫0のリスト()
        subprocess.run("ruby zaラクマ_入力テスト.rb " + str(self.file_out.parent), shell=True, text=True)
        # if self.file_out2 != None:
        #    self.出品の比較する()

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
        try:
            with open(self.file_path, 'r', encoding="utf-8") as f:
                self.seed1 = f.read()

            data = []
            soup = BeautifulSoup(self.seed1, 'html.parser')
            data_soup = soup.find_all("div", attrs={"class": "media-body"})
            for i in data_soup:
                if i == None:
                    print("")
                else:
                    #print(i.find("span", attrs={"class": "waiting"}))
                    t = i.find("span", attrs={"class": "waiting"})
                    #print(t)
                    if t == None:
                        print("")
                    else:
                        try:
                            #print(t)
                            m = t.text
                            #print(m)
                            if m == '出品中':
                                #print("出品中")
                                data.append(i.find("h4", attrs={"class": "media-heading"}))
                            elif m == "売却済み":
                                print("売却済み")
                            else:
                                print("それ以外")
                        except:
                            print("")
            #data = data.find("h4", attrs={"class": "media-heading"})
            
            # <div class="media-body">
            # <h4 class="media-heading">新品送料込み　男女兼用　白足袋24.0ｃｍ★成人式、結婚式、卒業式 ATU005</h4>
            
            i = 0
            for d in data:
                # print(d.text)
                #print(str(self.file_out.parent) + "\\ラクマ出品一覧.txt")
                if i == 0:
                    with open(str(self.file_out.parent) + "\\ラクマ出品一覧.txt", 'w', encoding="utf-8") as f:
                        f.write(d.text + "\n")
                        i = 1
                else:
                    with open(str(self.file_out.parent) + "\\ラクマ出品一覧.txt", 'a', encoding="utf-8") as f:
                        f.write(d.text + "\n")
        except:
            print("ラクマ出品一覧err")
            self.logger.debug('ラクマ出品一覧err')

    def ラクマ登録２重チェック(self):
        try:
            with open(str(self.file_out.parent) + "/ラクマ出品一覧.txt", 'r', encoding="utf-8") as f:
                self.seed1 = f.read().split("\n")

            with open(str(self.file_out.parent) + "/ラクマ出品一覧Ruby.txt", 'r', encoding="utf-8") as f:
                self.seed2 = f.read().split("\n")

            # listを削除する
            for i in self.seed2:
                self.seed1.remove(i)

            print(self.seed1)
            if self.seed1 == []:
                print("２重チェック無し")
            else:
                i = 0
                for d in self.seed1:
                    print("====２重チェック====")
                    print(d)
                    if i == 0:
                        with open(str(self.file_out.parent) + "\\ラクマ出品一覧２重登録.txt", 'w', encoding="utf-8") as f:
                            f.write(d + "\n")
                            i = 1
                    else:
                        with open(str(self.file_out.parent) + "\\ラクマ出品一覧２重登録.txt", 'a', encoding="utf-8") as f:
                            f.write(d + "\n")
        except:
            print("ラクマ登録２重チェックerr")
            self.logger.debug('ラクマ登録２重チェックerr')

    def 登録出来ていない商品チェック(self):
        try:
            with open("./ラクマディレクトリ.txt", 'r', encoding="utf-8") as f:
                self.seed1 = f.read().split("\n")

            with open(str(self.file_out.parent) + "\\ラクマ出品一覧.txt", 'r', encoding="utf-8") as f:
                self.seed2 = f.read().split("\n")

            with open("./ラクマ出品一覧在庫0.txt", 'r', encoding="utf-8") as f:
                self.seed3 = f.read().split("\n")

            print(self.seed1[0])
            print(self.seed2[0])
            print(self.seed3[0])
            try:
                for i in self.seed2:
                    self.seed1.remove(i)

                for i in self.seed3:
                    self.seed1.remove(i)
            except:
                print("対象がないです")

            i = 0
            for d in self.seed1:
                # print("====登録出来ていない商品かも====")
                # print(d)
                d_path = pathlib.Path(d)
                d = d_path.name
                d = d.replace(".txt", "")
                if i == 0:
                    with open(str(self.file_out.parent) + "\\登録出来ていない商品かも.txt", 'w', encoding="utf-8") as f:
                        f.write(d + "\n")
                        i = 1
                else:
                    with open(str(self.file_out.parent) + "\\登録出来ていない商品かも.txt", 'a', encoding="utf-8") as f:
                        f.write(d + "\n")
        except:
            print("登録出来ていない商品チェックerr")
            self.logger.debug('登録出来ていない商品チェックerr')

    def 在庫1商品リスト(self):
        try:
            with open("./ラクマディレクトリ.txt", 'r', encoding="utf-8") as f:
                self.seed1 = f.read().split("\n")

            i = 0
            for t in self.seed1:
                if "在庫1" in t:
                    # print("====在庫1====")
                    # print(t)
                    d_path = pathlib.Path(t)
                    d = d_path.name
                    d = d.replace(".txt", "")
                    if i == 0:
                        with open("./ラクマ出品一覧在庫1.txt", 'w', encoding="utf-8") as f:
                            f.write(d + "\n")
                            i = 1
                    else:
                        with open("./ラクマ出品一覧在庫1.txt", 'a', encoding="utf-8") as f:
                            f.write(d + "\n")
        except:
            print("在庫1商品リストerr")
            self.logger.debug('在庫1商品リストerr')

    def 在庫0商品リスト(self):
        try:
            with open("./ラクマディレクトリ.txt", 'r', encoding="utf-8") as f:
                self.seed1 = f.read().split("\n")

            i = 0
            for t in self.seed1:
                if "在庫0" in t:
                    #print("====在庫0====")
                    #print(t)
                    d_path = pathlib.Path(t)
                    d = d_path.name
                    d = d.replace(".txt", "")
                    if i == 0:
                        with open("./ラクマ出品一覧在庫0.txt", 'w', encoding="utf-8") as f:
                            f.write(d + "\n")
                            i = 1
                    else:
                        with open("./ラクマ出品一覧在庫0.txt", 'a', encoding="utf-8") as f:
                            f.write(d + "\n")
        except:
            print("在庫0商品リストerr")
            self.logger.debug('在庫0商品リストerr')

    def load(self, dir):
        with open(dir, 'r', encoding="utf-8") as f:
            self.seed1 = f.read()
        self.seed1 = self.seed1.replace("\n", "")
        self.seed1 = self.seed1.replace("\r", "")
        return self.seed1

    def 出品されているのに在庫0のリスト(self):
        try:
            with open(str(self.file_out.parent) + "/ラクマ出品一覧.txt", 'r', encoding="utf-8") as f:
                self.seed1 = f.read().split("\n")

            with open("./ラクマ出品一覧在庫0.txt", 'r', encoding="utf-8") as f:
                self.seed2 = f.read().split("\n")

            data = []
            for i in self.seed1:
                for s in self.seed2:
                    if i == s:
                        data.append(i)

            i = 0
            for d in data:

                # print("====出品されているのに在庫0のリスト====")
                # print(d)

                if i == 0:
                    with open(str(self.file_out.parent) + "\\出品されているのに在庫0のリスト.txt", 'w', encoding="utf-8") as f:
                        f.write(d + "\n")
                        i = 1
                else:
                    with open(str(self.file_out.parent) + "\\出品されているのに在庫0のリスト.txt", 'a', encoding="utf-8") as f:
                        f.write(d + "\n")
        except:
            print("出品されているのに在庫0のリストerr")
            self.logger.debug('出品されているのに在庫0のリストerr')

    def 出品されているB品のリスト(self):
        with open(str(self.file_out.parent) + "/ラクマ出品一覧.txt", 'r', encoding="utf-8") as f:
            self.seed1 = f.read().split("\n")
        
        data = []
        for i in self.seed1:
            if "B品" in i:
                data.append(i)
                
        i = 0
        for d in data:

            if i == 0:
                with open("./出品されている在庫B品のリスト.txt", 'w', encoding="utf-8") as f:
                    f.write(d + "\n")
                    i = 1
            else:
                with open("./出品されている在庫B品のリスト.txt", 'a', encoding="utf-8") as f:
                    f.write(d + "\n")
                
    
        try:
            with open(str(self.file_out.parent) + "/ラクマ出品一覧.txt", 'r', encoding="utf-8") as f:
                self.seed1 = f.read().split("\n")

            with open("./出品されている在庫B品のリスト.txt", 'r', encoding="utf-8") as f:
                self.seed2 = f.read().split("\n")

            data = []
            for i in self.seed1:
                for s in self.seed2:
                    if i == s:
                        data.append(i)

            i = 0
            for d in data:

                if i == 0:
                    with open(str(self.file_out.parent) + "\\出品されているB品のリスト.txt", 'w', encoding="utf-8") as f:
                        f.write(d + "\n")
                        i = 1
                else:
                    with open(str(self.file_out.parent) + "\\出品されているB品のリスト.txt", 'a', encoding="utf-8") as f:
                        f.write(d + "\n")
        except:
            print("出品されているB品のリストのリストerr")
            self.logger.debug('出品されているB品のリストerr')
    
    
    def 出品されている在庫1のリスト(self):
        try:
            with open(str(self.file_out.parent) + "/ラクマ出品一覧.txt", 'r', encoding="utf-8") as f:
                self.seed1 = f.read().split("\n")

            with open("./ラクマ出品一覧在庫1.txt", 'r', encoding="utf-8") as f:
                self.seed2 = f.read().split("\n")

            data = []
            for i in self.seed1:
                for s in self.seed2:
                    if i == s:
                        data.append(i)

            i = 0
            for d in data:

                if i == 0:
                    with open(str(self.file_out.parent) + "\\出品されている在庫1のリスト.txt", 'w', encoding="utf-8") as f:
                        f.write(d + "\n")
                        i = 1
                else:
                    with open(str(self.file_out.parent) + "\\出品されている在庫1のリスト.txt", 'a', encoding="utf-8") as f:
                        f.write(d + "\n")
        except:
            print("出品されている在庫1のリストerr")
            self.logger.debug('出品されている在庫1のリストerr')

    def 出品されているB品と在庫1以外のリスト():
        print("出品されているB品と在庫1以外のリスト。つまり普通のリスト。")
        with open(str(self.file_out.parent) + "/ラクマ出品一覧.txt", 'r', encoding="utf-8") as f:
            self.seed1 = f.read().split("\n")

        with open(str(self.file_out.parent) + "/出品されている在庫1のリスト.txt", 'r', encoding="utf-8") as f:
            self.seed2 = f.read().split("\n")
            
        with open(str(self.file_out.parent) + "/出品されているB品のリスト.txt", 'r', encoding="utf-8") as f:
            self.seed3 = f.read().split("\n")
            

        for i in self.seed2:
            self.seed1.remove(i)

        for i in self.seed3:
            self.seed1.remove(i)

        i = 0
        for d in self.seed1:
            if i == 0:
                with open(str(self.file_out.parent) + "\\出品されている普通のリスト.txt", 'w', encoding="utf-8") as f:
                    f.write(d + "\n")
                    i = 1
            else:
                with open(str(self.file_out.parent) + "\\出品されている普通のリスト.txt", 'a', encoding="utf-8") as f:
                    f.write(d + "\n")

    def 商品コードが認識されなかったリスト(self):
            print("")

    def 出品の比較する(self):
        try:
            # 比較_元
            with open(str(self.file_out.parent) + "/ラクマ出品一覧.txt", 'r', encoding="utf-8") as f:
                self.seed1 = f.read().split("\n")

            # 比較先
            with open(str(self.file_out2.parent) + "/ラクマ出品一覧.txt", 'r', encoding="utf-8") as f:
                self.seed2 = f.read().split("\n")

            data = []
            for i in self.seed1:
                for s in self.seed2:
                    if i == s:
                        data.append(i)

            i = 0
            for d in data:

                # print("====出品の比較する====")
                # print(d)

                if i == 0:
                    with open(str(self.file_out2.parent) + "\\出品の比較する.txt", 'w', encoding="utf-8") as f:
                        f.write(d + "\n")
                        i = 1
                else:
                    with open(str(self.file_out2.parent) + "\\出品の比較する.txt", 'a', encoding="utf-8") as f:
                        f.write(d + "\n")
        except:
            print("出品の比較するerr")
            self.logger.debug('出品の比較するerr')

    def get_logger(logger_name, log_file, f_fmt='%(message)s'):
        """ロガーを取得"""
        # ロガー作成
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG)

        # ファイルハンドラ作成
        file_handler = logging.FileHandler(
            log_file, mode='a', encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(logging.Formatter(f_fmt))

        # ロガーに追加
        logger.addHandler(file_handler)

        return logger

    def 商品番号取得(self):
        with open(str(self.file_out.parent) + "/ラクマ出品一覧.txt", 'r', encoding="utf-8") as f:
            self.seed1 = f.read().split("\n")
        
        a = 0
        for i in self.seed1:
            b = len(i.split("\s"))
            s = i.split("\s")[-1] # 文字列スペース区切りの一番最後
            #t = i.split("\s")[-2] # 文字列スペース区切りの二番目を取得
            c = len(i.split(")"))
            m = i.split(")")[-1] # 文字列カッコ区切りの一番最後
            
            if a == 0:
                with open(str(self.file_out.parent) + "/商品コード.txt", 'w', encoding="utf-8") as f:
                    f.write(str(b) + "\t" + str(c) + "\t" + s + "\t" +  m + "\t" + i + "\n")
                    a = 1
            else:
                with open(str(self.file_out.parent) + "/商品コード.txt", 'a', encoding="utf-8") as f:
                    f.write(str(b) + "\t" + str(c) + "\t" + s + "\t" +  m + "\t" + i + "\n")


if __name__ == '__main__':
    rakuma_test = Rakuma_Test()

    # while True:
    #    rakuma_test.main()
    #    time.sleep(10)
