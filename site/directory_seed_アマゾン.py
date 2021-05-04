# -*- coding:utf-8 -*-

# 2021/04/25
# pip install -U sqlalchemy


from config import Config
from directory_seed import Mail_order_site

import datetime
import time
import os
import random
import re
import glob

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from bs4 import BeautifulSoup

Base = automap_base()

# engine, suppose it has two tables 'user' and 'address' set up
#engine = create_engine("sqlite:///db.sqlite3")

# reflect the tables
#Base.prepare(engine, reflect=True)

# mapped classes are now created with names by default
# matching that of the table name.

#session = Session(engine)


class Rakuten(Mail_order_site):
    def __init__(self):
        self.config = Config()
        Base = automap_base()
        # engine, suppose it has two tables 'user' and 'address' set up
        self.engine = create_engine(self.config.db_path)
        # 個人情報の塊なのでGITの外に設置

        # reflect the tables
        Base.prepare(self.engine, reflect=True)

        # mapped classes are now created with names by default
        # matching that of the table name.

        self.seeds = Base.classes.seeds
        self.site = Base.classes.site
        self.sale = Base.classes.sale

        self.siteID = 0


    def get_data2(self):
        self.data = self.get_data()
        return str(self.data.seed)

    def get_seed2(self):
        self.data = self.get_data2()
        return self.data.replace("charset=euc-jp", 'charset="UTF-8"')

    def test(self):
        with open("./../../mail_order_site0.html", 'w', encoding="utf-8") as f:
            f.write(str(self.get_seed()))
        print(self.get_id())
        print(self.get_日付())
        print(self.get_商品コード)
        print(self.get_商品名)
        print(self.get_数量)
        
        print(self.get_落札者_郵便番号)
        print(self.get_落札者_住所)
        print(self.get_落札者_名前)
        print(self.get_落札者_ペンネーム)
        print(self.get_落札者_電話番号)
        print(self.get_落札者_メールアドレス)
        
        print(self.get_送り先_郵便番号)
        print(self.get_送り先_住所)
        print(self.get_送り先_名前)
        print(self.get_送り先_ペンネーム)
        print(self.get_送り先_電話番号)
        print(self.get_送り先_メールアドレス)
        
        print(self.get_購入金額)
        print(self.get_送料)
        print(self.get_合計金額)
        

    def get_id(self):
        #MYO-app > div > div.a-row.a-spacing-medium > div.a-column.a-span10 > div > div:nth-child(2) > div.a-row.a-spacing-mini > div > span.a-text-bold
        #<span data-test-id="order-id-value" dir="ltr" class="a-text-bold">250-6258991-0758247</span>
        temp = ""
        try:
            temp = self.soup.find('span', {'class': f'a-text-bold'}).txet
        except:
            temp = ""
        return temp

    def get_日付(self):
        #MYO-app > div > div.a-row.a-spacing-medium > div.a-column.a-span10 > div > div.a-row.a-spacing-small.a-spacing-top-small > div.a-column.a-span7 > div > div > div > div > div > div.a-column.a-span7 > table > tbody > tr:nth-child(3) > td.a-color-.a-text-left.a-align-bottom > span
        #<span data-test-id="order-summary-purchase-date-value">2021年4月27日(火) 11:45 JST</span>
        temp = ""
        try:
            temp = self.soup.find('span', {'data-test-id': f'order-summary-purchase-date-value'}).txet
            temp = temp.replace("年", "/")
            temp = temp.replace("月", "/")
            temp = temp.replace("日", "")
            temp = temp.replace("(", "")
            temp = temp.replace(")", "")
            temp = temp.replace("月", "")
            temp = temp.replace("火", "")
            temp = temp.replace("水", "")
            temp = temp.replace("木", "")
            temp = temp.replace("金", "")
            temp = temp.replace("土", "")
            temp = temp.replace("日", "")

        except:
            temp = ""
        return temp

    def get_商品コード(self):
        temp = ""
        try:
            print()
        except:
            temp = ""
        return temp

    def get_商品名(self):
        temp = ""
        try:
            print()
        except:
            temp = ""
        return temp

    def get_数量(self):
        temp = ""
        try:
            print()
        except:
            temp = ""
        return temp


    def get_落札者_郵便番号(self):
        temp = ""
        try:
            print()
        except:
            temp = ""
        return temp

    def get_落札者_住所(self):
        temp = ""
        try:
            print()
        except:
            temp = ""
        return temp

    def get_落札者_名前(self):
        temp = ""
        try:
            print()
        except:
            temp = ""
        return temp

    def get_落札者_ペンネーム(self):
        temp = ""
        try:
            print()
        except:
            temp = ""
        return temp

    def get_落札者_電話番号(self):
        temp = ""
        try:
            print()
        except:
            temp = ""
        return temp

    def get_落札者_メールアドレス(self):
        # td4_0 > table > tbody > tr:nth-child(6) > td:nth-child(2) > small
        temp = ""
        try:
            print()
        except:
            temp = ""
        return temp


    def get_送り先_郵便番号(self):
        temp = ""
        try:
            print()
        except:
            temp = ""
        return temp

    def get_送り先_住所(self):
        # td4_0 > table > tbody > tr:nth-child(3) > td:nth-child(2) > small
        temp = ""
        try:
            print()
        except:
            temp = ""
        return temp
    
    def get_送り先_名前(self):
        # td4_0 > table > tbody > tr:nth-child(2) > td:nth-child(2) > small
        # td4_1 > table > tbody > tr:nth-child(2) > td:nth-child(2) > small
        temp = ""
        try:
            print()
        except:
            temp = ""
        return temp

    def get_送り先_ペンネーム(self):
        temp = ""
        try:
            print()
        except:
            temp = ""
        return temp

    def get_送り先_電話番号(self):
        # td4_0 > table > tbody > tr:nth-child(4) > td:nth-child(2) > small
        temp = ""
        try:
            print()
        except:
            temp = ""
        return temp



    def get_購入金額(self):
        temp = ""
        try:
            print()
        except:
            temp = ""
        return temp

    def get_送料(self):
        temp = ""
        try:
            print()
        except:
            temp = ""
        return temp

    def get_合計金額(self):
        # td4_0 > table > tbody > tr:nth-child(4) > td:nth-child(2) > small
        temp = ""
        try:
            print()
        except:
            temp = ""
        return temp

 
    def main(self):
        self.mail_order_site = Mail_order_site()
        self.mail_order_site.siteID = 0
        self.get_data()
        self.soup = BeautifulSoup(self.get_seed(), "html.parser")
        self.test()
        

            

if __name__ == '__main__':
    rakuten = Rakuten()
    rakuten.main()

