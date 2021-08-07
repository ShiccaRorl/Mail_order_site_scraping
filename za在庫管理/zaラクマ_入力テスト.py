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

    def main(self):
    
        args = sys.argv
        file_path = args[1]
        
        if file_path == nil:
            print("引数が足りません")
        
    
        i = 0
        for d in glob.glob(ROOT_PATH + "/*.txt"):
            if i == 0:
                with open("ラクマディレクトリ.txt", 'w', encoding="utf-8") as f:
                    f.write(d)
                    i = 1
            else:
                with open("ラクマディレクトリ.txt", 'a', encoding="utf-8") as f:
                    f.write(d)
            print(d)

            

        
        with open(file_path, 'r', encoding="utf-8") as f:
            self.seed1 = f.read()

        soup = BeautifulSoup(self.seed1, 'html.parser')
        data = soup.find_all("h4", attrs={"class": "media-heading"})

        #<h4 class="media-heading">新品送料込み　男女兼用　白足袋24.0ｃｍ★成人式、結婚式、卒業式 ATU005</h4>

        i = 0
        for d in data:
            if i == 0:
                with open("ラクマ出品一覧.txt", 'w', encoding="utf-8") as f:
                    f.write(d)
                    i = 1
            else:
                with open("ラクマ出品一覧.txt", 'a', encoding="utf-8") as f:
                    f.write(d)
    
    
    def load(self, dir):
        with open(dir, 'r', encoding="utf-8") as f:
            self.seed1 = f.read()
        self.seed1 = self.seed1.replace("\n", "")
        self.seed1 = self.seed1.replace("\r", "")
        return self.seed1




if __name__ == '__main__':
    rakuma_test = Rakuma_Test()
    
    #while True:
    #    rakuma_test.main()
    #    time.sleep(10)
        
