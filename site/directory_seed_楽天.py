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


class Rakuten():
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


    def get_data(self):
        self.data = self.mail_order_site.get_data()
        return str(self.data.seed)

    def get_seed(self):
        self.data = self.get_data()
        return self.data.replace("charset=euc-jp", 'charset="UTF-8"')

    def test(self):
        with open("./../../mail_order_site1.html", 'w', encoding="utf-8") as f:
            f.write(str(self.get_seed()))


    def get_id(self):
        soup = self.soup.find('a', {'class': f'rms-status-order-nr'})
        return soup.text.strip()

    def get_日付(self):
        return


    def get_商品明細(self):
        soup = self.soup.find('div', {'class': f'rms-row-wrapper'})
        return soup

    def get_商品コード(self):
        soup = self.get_商品明細().find('a', {'class': f'rms-span-open-in-new'})
        return soup.text.strip()

    def get_商品名(self):
        soup = self.get_商品明細().find('a', {'class': f'rms-span-open-in-new'})
        return soup.text.strip()

    def get_数量(self):
        soup = self.get_商品明細().find('div', {'class': f'rms-table-column-line'})
        return soup.text.strip()


    def get_注文者_名前(self):
        soup = self.soup.find('span', {'class': f'fullname'})
        return soup.text.strip()

    def get_注文者_ペンネーム(self):
        return

    def get_注文者_郵便番号(self):
        soup = self.soup.find('span', {'class': f'address'})
        temp = str(soup.text).split(" ")[0]
        temp = temp.replace("〒", "")
        return temp.strip()

    def get_注文者_住所(self):
        soup = self.soup.find('span', {'class': f'address'})
        temp = soup.text.split(" ")[1]
        return temp.strip()


    def get_注文者_電話番号(self):
        soup = self.soup.find('span', {'class': f'phone'})
        return soup.text.strip()

    def get_注文者_メールアドレス(self):
        soup = self.soup.find('a', {'class': f'email'})
        return soup.text.strip()



    def get_送り先_名前(self):
        soup = self.soup.find('span', {'class': f'fullname'})
        return soup.text.strip()

    def get_送り先_ペンネーム(self):
        return

    def get_送り先_郵便番号(self):
        soup = self.soup.find('span', {'class': f'address'})
        temp = soup.text.split(" ")[0]
        temp = temp.replace("〒", "")
        return temp.strip()

    def get_送り先_住所(self):
        soup = self.soup.find('span', {'class': f'address'})
        temp = soup.text.split(" ")[0]
        temp = temp.replace("〒", "")
        return temp.strip()

    def get_送り先_電話番号(self):
        soup = self.soup.find('span', {'class': f'phone'})
        return soup.text.strip()

    def get_送り先_メールアドレス(self):
        return

    def get_購買額(self):
        soup = self.soup.find('span', {'class': f'footer-price'})
        return soup.text.strip()

    def main(self):
        self.mail_order_site = Mail_order_site()
        self.mail_order_site.siteID = 1
        self.get_data()
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