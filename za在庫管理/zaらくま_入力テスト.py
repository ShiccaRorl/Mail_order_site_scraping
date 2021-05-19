# -*- coding:utf-8 -*-

# 2021/04/25
# pip install -U sqlalchemy


#from config import Config
#from directory_seed import Mail_order_site

import datetime
import time
import os
import random
import re
import glob

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


class Rakuma_Test():
    def __init__(self):
        #self.config = Config()
        #Base = automap_base()
        # engine, suppose it has two tables 'user' and 'address' set up
        #self.engine = create_engine(self.config.db_path)
        # 個人情報の塊なのでGITの外に設置

        # reflect the tables
        #Base.prepare(self.engine, reflect=True)

        # mapped classes are now created with names by default
        # matching that of the table name.

        #self.seeds = Base.classes.seeds
        #self.site = Base.classes.site
        #self.sale = Base.classes.sale

        #self.siteID = 2
        
        self.err_文字列 = "ゆうパケット"
    def main(self):
        for d in glob.glob("C:/Users/user/Downloads/rakuma_入力テスト*"):
            print(d)
            data = self.load(d)
            if self.err_文字列 in data:
                print(f"{d}  エラーがあります。")
            else:
                self.削除する(d)
            
            



    def 削除する(self, dir):
        print(f"{dir} 削除します")
        os.remove(dir)


        
    def load(self, dir):
        with open(dir, 'r', encoding="utf-8") as f:
            self.seed1 = f.read()
        self.seed1 = self.seed1.replace("\n", "")
        self.seed1 = self.seed1.replace("\r", "")
        return self.seed1




if __name__ == '__main__':
    rakuma_test = Rakuma_Test()
    while True:
        rakuma_test.main()
        time.sleep(10)
        
