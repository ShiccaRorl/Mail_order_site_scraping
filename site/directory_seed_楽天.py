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
        self.setup()
        
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
        
        


    def get_data2(self):
        self.data = self.get_data()
        return str(self.data.seed)

    def get_seed2(self):
        self.data = self.get_data()
        return self.data.replace("charset=euc-jp", 'charset="UTF-8"')

    def test(self):
        with open("./../../mail_order_site1.html", 'w', encoding="utf-8") as f:
            f.write(str(self.get_seed()))


    def get_id(self):
        try:
            soup = self.soup.find('a', {'class': 'rms-status-order-nr'})
            temp = soup.text.strip()
        except:
            temp = ""
        return temp

    def get_日付(self):
        try:
            temp = self.soup.find('a', {'class': 'rms-content-order-details-block-history-table'})
            
            temp = re.search(r"<td>注文日時</td> <td>(.*?)</td>" , temp)
        except:
            temp = ""
        return temp


    def get_商品明細(self):
        try:
            soup = self.soup.find('div', {'class': 'rms-row-wrapper'})
        except:
            soup = ""
        return soup

    def get_商品コード(self):
        try:
            soup = self.get_商品明細().find('a', {'class': f'rms-span-open-in-new'})
            temp = soup.text.strip()
        except:
            temp = ""
        return temp

    def get_商品名(self):
        try:
            soup = self.get_商品明細().find('a', {'class': f'rms-span-open-in-new'})
            temp = soup.text.strip()
        except:
            temp= ""
        return temp

    def get_数量(self):
        try:
            soup = self.get_商品明細().find('div', {'class': f'rms-table-column-line'})
            temp = soup.text.strip()
        except:
            temp = ""
        return temp


    def get_注文者_名前(self):
        try:
            soup = self.soup.find('span', {'class': f'fullname'})
            temp = soup.text.strip()
        except:
            temp = ""
        return temp

    def get_注文者_ペンネーム(self):
        try:
            temp = ""
            return temp
        except:
            temp = ""
        return temp

    def get_注文者_郵便番号(self):
        try:
            soup = self.soup.find('span', {'class': f'address'})
            temp = re.split("\s", str(soup.text))[0]
            temp = temp.replace("〒", "")
            temp = temp.strip()
        except:
            temp = ""
        return temp

    def get_注文者_住所(self):
        try:
            soup = self.soup.find('span', {'class': f'address'})
            temp = re.split("\s", str(soup.text))[1]
            temp = temp.strip()
        except:
            temp = ""
        return temp


    def get_注文者_電話番号(self):
        try:
            soup = self.soup.find('span', {'class': f'phone'})
            temp = soup.text.strip()
        except:
            temp = ""
        return temp

    def get_注文者_メールアドレス(self):
        try:
            soup = self.soup.find('a', {'class': f'email'})
            temp = soup.text.strip()
        except:
            temp = ""
        return temp



    def get_送り先_名前(self):
        try:
            soup = self.soup.find('span', {'class': f'fullname'})
            temp = soup.text.strip()
        except:
            temp = ""
        return temp

    def get_送り先_ペンネーム(self):
        try:
            print()
        except:
            temp = ""
        return temp

    def get_送り先_郵便番号(self):
        try:
            soup = self.soup.find('span', {'class': f'address'})
            temp = soup.text.split(" ")[0]
            temp = temp.replace("〒", "")
            temp = temp.strip()
        except:
            temp = ""
        return temp

    def get_送り先_住所(self):
        try:
            soup = self.soup.find('span', {'class': f'address'})
            temp = soup.text.split(" ")[0]
            temp = temp.replace("〒", "")
            temp = temp.strip()
        except:
            temp = ""
        return temp

    def get_送り先_電話番号(self):
        try:
            soup = self.soup.find('span', {'class': f'phone'})
            temp = soup.text.strip()
        except:
            temp = ""
        return temp

    def get_送り先_メールアドレス(self):
        try:
            print()
        except:
            temp = ""
        return temp

    def get_購買額(self):
        try:
            soup = self.soup.find('span', {'class': f'footer-price'})
            temp = soup.text.strip()
        except:
            temp = ""
        return temp

    def main(self):
        self.siteID = 1
        #self.get_data()
        self.soup = BeautifulSoup(self.get_seed(), "html.parser")
        self.test()
        


      
        #print(self.test())
        print("")
        print("id")
        print(self.get_id())
        print("")
        print("日付")
        print(self.get_日付())
        print("")
        print("商品明細")
        print(self.get_商品明細())
        print("")
        print("商品コード")
        print(self.get_商品コード())
        print("")
        print("商品名")
        print(self.get_商品名())
        print("")
        print("数量")
        print(self.get_数量())
        print("")
        print("注文者_名前")
        print(self.get_注文者_名前())
        print("")
        print("注文者_ペンネーム")
        print(self.get_注文者_ペンネーム())
        print("")
        print("注文者_郵便番号")
        print(self.get_注文者_郵便番号())
        print("")
        print("注文者_住所")
        print(self.get_注文者_住所())
        print("")
        print("注文者_電話番号")
        print(self.get_注文者_電話番号())
        print("")
        print("注文者_メールアドレス")
        print(self.get_注文者_メールアドレス())
        print("")
        print("送り先_郵便番号")
        print(self.get_送り先_郵便番号())
        print("")
        print("送り先_名前")
        print(self.get_送り先_名前())
        print("")
        print("送り先_ペンネーム")
        print(self.get_送り先_ペンネーム())
        print("")
        print("送り先_住所")
        print(self.get_送り先_住所())
        print("")
        print("送り先_電話番号")
        print(self.get_送り先_電話番号())
        print("")
        print("送り先_メールアドレス")
        print(self.get_送り先_メールアドレス())



if __name__ == '__main__':
    rakuten = Rakuten()
    rakuten.main()
    """
    print(yahoo_auction.get_id())
    print(yahoo_auction.get_日付())
    print(yahoo_auction.get_商品コード())
    print(yahoo_auction.get_商品名())
    print(yahoo_auction.get_数量())
    print(yahoo_auction.get_注文者_名前())
    print(yahoo_auction.get_注文者_ペンネーム())
    print(yahoo_auction.get_注文者_郵便番号())
    print(yahoo_auction.get_注文者_住所())
    print(yahoo_auction.get_注文者_電話番号())
    print(yahoo_auction.get_注文者_メールアドレス())
    print(yahoo_auction.get_送り先_郵便番号())
    print(yahoo_auction.get_送り先_名前())
    print(yahoo_auction.get_送り先_ペンネーム())
    print(yahoo_auction.get_送り先_住所())
    print(yahoo_auction.get_送り先_電話番号())
    print(yahoo_auction.get_送り先_メールアドレス())
    print(yahoo_auction.get_送り先_住所())
    """