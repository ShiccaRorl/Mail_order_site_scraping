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


class Yahoo_auction():
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
        with open("./../../mail_order_site2.html", 'w', encoding="utf-8") as f:
            f.write(str(self.get_seed()))


    def get_id(self):
        return

    def get_日付(self):
        # td3_0 > table > tbody > tr:nth-child(5) > td:nth-child(2) > small
        # td3_1 > table > tbody > tr:nth-child(5) > td:nth-child(2) > small
        return

    def get_商品コード(self):
        # td3_0 > table > tbody > tr:nth-child(4) > td:nth-child(2) > small > a
        # td3_1 > table > tbody > tr:nth-child(4) > td:nth-child(2) > small > a
        return

    def get_商品名(self):
        # td3_0 > table > tbody > tr:nth-child(4) > td:nth-child(2) > small > a
        # td3_1 > table > tbody > tr:nth-child(4) > td:nth-child(2) > small > a
        return

    def get_数量(self):
        # td3_1 > table > tbody > tr:nth-child(6) > td:nth-child(2) > small
        return

    def get_落札者_名前(self):
        # td4_0 > table > tbody > tr:nth-child(5) > td:nth-child(2)

        return

    def get_落札者_ペンネーム(self):
        return

    def get_落札者_郵便番号(self):
        return

    def get_落札者_住所(self):

        return

    def get_落札者_電話番号(self):

        return

    def get_落札者_メールアドレス(self):
        # td4_0 > table > tbody > tr:nth-child(6) > td:nth-child(2) > small
        return

    def get_送り先_郵便番号(self):
        return

    def get_送り先_名前(self):
        # td4_0 > table > tbody > tr:nth-child(2) > td:nth-child(2) > small
        # td4_1 > table > tbody > tr:nth-child(2) > td:nth-child(2) > small
        return

    def get_送り先_ペンネーム(self):
        return

    def get_送り先_住所(self):
        # td4_0 > table > tbody > tr:nth-child(3) > td:nth-child(2) > small
        return

    def get_送り先_電話番号(self):
        # td4_0 > table > tbody > tr:nth-child(4) > td:nth-child(2) > small
        return

    def get_送り先_メールアドレス(self):

        return

    def get_送り先_住所(self):

        return

    def main(self):
        self.mail_order_site = Mail_order_site()
        self.mail_order_site.siteID = 2
        self.get_data()
        self.soup = BeautifulSoup(self.get_seed(), "html.parser")
        self.test()
        
        i = 0
        tdss = TDss()
        while i <= 30:

            soup3 = self.soup.find('td', {'id': f'td3_{i}'})
            td3 = Td3(soup3)
            
            soup4 = self.soup.find('td', {'id': f'td4_{i}'})
            td4 = Td4(soup4)

            soup5 = self.soup.find('td', {'id': f'td5_{i}'})
            td5 = Td5(soup5)

            tdss.add_td([td3, td4, td5])
            i = i + 1
        
        #print(tdss.tds[0][0].test())
        print(tdss.tds[0][0].get_id())
        print(tdss.tds[0][0].get_日付())
        print(tdss.tds[0][0].get_商品コード())
        print(tdss.tds[0][0].get_商品名())
        print(tdss.tds[0][0].get_数量())
        
        print(tdss.tds[1][1].test())
        print(tdss.tds[1][1].get_落札者_名前())
        print(tdss.tds[1][1].get_落札者_ペンネーム())
        print(tdss.tds[1][1].get_落札者_郵便番号())
        print(tdss.tds[1][1].get_落札者_住所())
        print(tdss.tds[1][1].get_落札者_電話番号())
        print(tdss.tds[1][1].get_落札者_メールアドレス())
        print(tdss.tds[1][1].get_送り先_郵便番号())
        print(tdss.tds[1][1].get_送り先_名前())
        print(tdss.tds[1][1].get_送り先_ペンネーム())
        print(tdss.tds[1][1].get_送り先_住所())
        print(tdss.tds[1][1].get_送り先_電話番号())
        print(tdss.tds[1][1].get_送り先_メールアドレス())
        print(tdss.tds[1][1].get_送り先_住所())

        
class TDss():
    def __init__(self):
        self.tds = []
        
    def add_td(self, td):
        self.tds.append(td)


class Td3():
    def __init__(self, soup):
        self.soup = soup

    def get_all(self):
        return self.soup.find_all("small")
        
    def test(self):
        s = 0
        print("対応表_表示")
        for i in self.get_all():
            print(f"=={s}==")
            print(i)
            print("")
            s = s + 1

    def get_id(self):
        return self.soup.find_all("small")[1].text.replace(" （商品ページ）", "").strip()

    def get_日付(self):
        temp = self.soup.find_all("small")[9].text.replace("月", "/")
        temp = temp.replace("日", "/")
        temp = temp.replace("時", ":")
        temp = temp.replace("分", "")
        return temp.strip()
    
    def get_商品名(self):
        return self.soup.find_all("small")[7].text.strip()
    
    def get_商品コード(self):
        return self.soup.find_all("small")[7].text.strip()
    
    def get_数量(self):
        return int(self.soup.find_all("small")[11].text.replace("個", "").strip())
    
    
class Td4():
    def __init__(self, soup):
        self.soup = soup

    def get_all(self):
        return self.soup.find_all("small")
        
    def test(self):
        s = 0
        print("対応表_表示")
        for i in self.get_all():
            print(f"=={s}==")
            print(i)
            print("")
            s = s + 1

    def get_落札者_名前(self):
        return self.soup.find_all("small")[9].text.strip()
    
    def get_落札者_ペンネーム(self):
        return
    
    def get_落札者_郵便番号(self):
        return
    
    def get_落札者_住所(self):
        return
    
    def get_落札者_電話番号(self):
        return
    
    def get_落札者_メールアドレス(self):
        return self.soup.find_all("small")[11].text.strip()

    
    def get_送り先_名前(self):
        return self.soup.find_all("small")[3].text.strip()
    
    def get_送り先_ペンネーム(self):
        return
    
    def get_送り先_郵便番号(self):
        temp = self.soup.find_all("small")[5].text.split(" ")[0]
        return temp.strip()
    
    def get_送り先_住所(self):
        temp = self.soup.find_all("small")[5].text.split(" ")[1]
        return temp.strip()
    
    def get_送り先_電話番号(self):
        return self.soup.find_all("small")[7].text.strip()
    
    def get_送り先_メールアドレス(self):
        return





class Td5():
    def __init__(self, soup):
        self.soup = soup

    def get_all(self):
        return self.soup.find_all("small")
        
    def test(self):
        s = 0
        print("対応表_表示")
        for i in self.get_all():
            print(f"=={s}==")
            print(i)
            print("")
            s = s + 1
            

if __name__ == '__main__':
    yahoo_auction = Yahoo_auction()
    yahoo_auction.main()
    print(yahoo_auction.get_id())
    print(yahoo_auction.get_日付())
    print(yahoo_auction.get_商品コード())
    print(yahoo_auction.get_商品名())
    print(yahoo_auction.get_数量())
    print(yahoo_auction.get_落札者_名前())
    print(yahoo_auction.get_落札者_ペンネーム())
    print(yahoo_auction.get_落札者_郵便番号())
    print(yahoo_auction.get_落札者_住所())
    print(yahoo_auction.get_落札者_電話番号())
    print(yahoo_auction.get_落札者_メールアドレス())
    print(yahoo_auction.get_送り先_郵便番号())
    print(yahoo_auction.get_送り先_名前())
    print(yahoo_auction.get_送り先_ペンネーム())
    print(yahoo_auction.get_送り先_住所())
    print(yahoo_auction.get_送り先_電話番号())
    print(yahoo_auction.get_送り先_メールアドレス())
    print(yahoo_auction.get_送り先_住所())
