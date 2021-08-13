# -*- coding:utf-8 -*-

# 2021/08/07
# pip install -U sqlalchemy
# pip install -U BeautifulSoup


#from config import Config
#from directory_seed import Mail_order_site

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
ROOT_PATH = 'C:/Users/user/Downloads/バックアップ/プログラム/バックアップ/保存/メルカリ'


class Rakuma_Test():
    def __init__(self):
        args = sys.argv

        try:
            self.file_path = args[1]
            self.file_out = pathlib.Path(args[1])
        except:
            print("データリフレッシュモード")
            self.file_out = pathlib.Path("")
            self.ラクマディレクトリ()

        self.main()

    def main(self):
        #self.ラクマディレクトリ()
        self.ラクマ出品一覧()

        subprocess.run("ruby zaラクマ_入力テスト.rb " +
                       str(self.file_out.parent), shell=True, text=True)
        self.ラクマ登録２重チェック()
        self.在庫0商品リスト()
        self.在庫1商品リスト()
        self.登録出来ていない商品チェック()

    def ラクマディレクトリ(self):
        i = 0
        for d in glob.glob(ROOT_PATH + "/**/*.txt"):
            d_path = pathlib.Path(d)
            print(d_path)
            if i == 0:
                with open("./ラクマディレクトリ.txt", 'w', encoding="utf-8") as f:
                    #f.write(d_path.stem + "\n")
                    f.write(d_path + "\n")
                    i = 1
            else:
                with open("./ラクマディレクトリ.txt", 'a', encoding="utf-8") as f:
                    #f.write(d_path.stem + "\n")
                    f.write(d_path + "\n")
            print(d)


    def ラクマ出品一覧(self):
        with open(self.file_path, 'r', encoding="utf-8") as f:
            self.seed1 = f.read()

        soup = BeautifulSoup(self.seed1, 'html.parser')
        data = soup.find_all("h4", attrs={"class": "media-heading"})

        # <h4 class="media-heading">新品送料込み　男女兼用　白足袋24.0ｃｍ★成人式、結婚式、卒業式 ATU005</h4>

        i = 0
        for d in data:
            print(d.text)
            if i == 0:
                print(str(self.file_out.parent))
                with open(str(self.file_out.parent) + "\\ラクマ出品一覧.txt", 'w', encoding="utf-8") as f:
                    f.write(d.text + "\n")
                    i = 1
            else:
                with open(str(self.file_out.parent) + "\\ラクマ出品一覧.txt", 'a', encoding="utf-8") as f:
                    f.write(d.text + "\n")

    def ラクマ登録２重チェック(self):
        with open(str(self.file_out.parent) + "/ラクマ出品一覧.txt", 'r', encoding="utf-8") as f:
            self.seed1 = f.read().split("\n")

        with open(str(self.file_out.parent) + "/ラクマ出品一覧Ruby.txt", 'r', encoding="utf-8") as f:
            self.seed2 = f.read().split("\n")

        # listを削除する
        for i in self.seed2:
            self.seed1.remove(i)

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

    def 登録出来ていない商品チェック(self):

        with open("./ラクマディレクトリ.txt", 'r', encoding="utf-8") as f:
            self.seed1 = f.read().split("\n")

        with open(str(self.file_out.parent) + "/ラクマ出品一覧Ruby.txt", 'r', encoding="utf-8") as f:
            self.seed2 = f.read().split("\n")

        with open(str(self.file_out.parent) + "/ラクマ出品一覧在庫0.txt", 'r', encoding="utf-8") as f:
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
            print("====登録出来ていない商品かも====")
            print(d)
            if i == 0:
                with open(str(self.file_out.parent) + "\\登録出来ていない商品かも.txt", 'w', encoding="utf-8") as f:
                    f.write(d + "\n")
                    i = 1
            else:
                with open(str(self.file_out.parent) + "\\登録出来ていない商品かも.txt", 'a', encoding="utf-8") as f:
                    f.write(d + "\n")

    def 在庫1商品リスト(self):
        with open("./ラクマディレクトリ.txt", 'r', encoding="utf-8") as f:
            self.seed1 = f.read().split("\n")

        for t in self.seed1:
            i = 0
            if "在庫1" in t:
                print("====在庫1====")
                print(t)
                if i == 0:
                    with open(str(self.file_out.parent) + "\\ラクマ出品一覧在庫1.txt", 'w', encoding="utf-8") as f:
                        f.write(t + "\n")
                        i = 1
                else:
                    with open(str(self.file_out.parent) + "\\ラクマ出品一覧在庫1.txt", 'a', encoding="utf-8") as f:
                        f.write(t + "\n")

    def 在庫0商品リスト(self):
        with open("./ラクマディレクトリ.txt", 'r', encoding="utf-8") as f:
            self.seed1 = f.read().split("\n")

        for t in self.seed1:
            print("====在庫0====")
            i = 0
            if "在庫0" in t:
                print(t)
                if i == 0:
                    with open(str(self.file_out.parent) + "\\ラクマ出品一覧在庫0.txt", 'w', encoding="utf-8") as f:
                        f.write(t + "\n")
                        i = 1
                else:
                    with open(str(self.file_out.parent) + "\\ラクマ出品一覧在庫0.txt", 'a', encoding="utf-8") as f:
                        f.write(t + "\n")

    def load(self, dir):
        with open(dir, 'r', encoding="utf-8") as f:
            self.seed1 = f.read()
        self.seed1 = self.seed1.replace("\n", "")
        self.seed1 = self.seed1.replace("\r", "")
        return self.seed1


if __name__ == '__main__':
    rakuma_test = Rakuma_Test()

    # while True:
    #    rakuma_test.main()
    #    time.sleep(10)
