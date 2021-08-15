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
import subprocess


Base = automap_base()

# engine, suppose it has two tables 'user' and 'address' set up
#engine = create_engine("sqlite:///db.sqlite3")

# reflect the tables
#Base.prepare(engine, reflect=True)

# mapped classes are now created with names by default
# matching that of the table name.

#session = Session(engine)


class Yahoo_auction(Mail_order_site):
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

        self.siteID = 2

    def get_data2(self):
        self.data = self.get_data()
        return str(self.data.seed)

    def get_seed2(self):
        self.data = self.get_data2()
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
        all = []
        session = Session(bind=self.engine)
        all = session.query(self.seeds).filter(
            self.seeds.siteID == self.siteID and self.seeds.analysis_completed == 0).all()
        for t in all:
            # print(i)

            self.setup()
            self.siteID = 2
            # self.get_seed()
            self.soup = BeautifulSoup(t.seed, "html.parser")
            self.test()

            i = 0
            self.tdss = TDss()
            while i <= int(self.config.yahoo_auction_page):

                soup3 = self.soup.find('td', {'id': f'td3_{i}'})
                td3 = Td3(soup3)

                soup4 = self.soup.find('td', {'id': f'td4_{i}'})
                td4 = Td4(soup4)

                soup5 = self.soup.find('td', {'id': f'td5_{i}'})
                td5 = Td5(soup5)

                self.tdss.add_td([td3, td4, td5])
                i = i + 1
                print(i)
                time.sleep(1)
            # self.tdss.test() # test mode
            self.db()
            self.update_analysis_completed(t.id)
            print(t.id)
            time.sleep(1)

    def db(self):

        i = 0
        while i <= int(self.config.yahoo_auction_page):
            session = Session(bind=self.engine)
            if session.query(self.seed).filter(self.seed.code == self.tdss.tds[i][0].get_id()).first() == None:
                # 新規追加

                if self.tdss.tds[i][1].get_落札者_名前() == "" or self.tdss.tds[i][1].get_落札者_名前() == "落札者データの表示期間が終了しました。":
                    print(f"{i} 欠損データ")

                    i = i + 1
                else:
                    print("")
                    print(f"{i} 新規追加")
                    print(self.tdss.tds[i][0].get_id())
                    try:
                        self.code = self.tdss.tds[i][0].get_id()
                        self.siteID = self.siteID
                        self.create_at = datetime.datetime.now()
                        self.update_at = datetime.datetime.now()

                        self.日付 = self.tdss.tds[i][0].get_日付()
                        self.商品コード = self.tdss.tds[i][0].get_商品コード()
                        self.商品名 = self.tdss.tds[i][0].get_商品名()
                        self.数量 = self.tdss.tds[i][0].get_数量()

                        self.購入者_名前 = self.tdss.tds[i][1].get_落札者_名前()
                        self.購入者_ペンネーム = self.tdss.tds[i][1].get_落札者_ペンネーム()
                        self.購入者_郵便番号 = self.tdss.tds[i][1].get_落札者_郵便番号()
                        self.購入者_住所 = self.tdss.tds[i][1].get_落札者_住所()
                        self.購入者_電話番号 = self.tdss.tds[i][1].get_落札者_電話番号()
                        self.購入者_メールアドレス = self.tdss.tds[i][1].get_落札者_メールアドレス(
                        )

                        self.送り先_名前 = self.tdss.tds[i][1].get_送り先_名前()
                        self.送り先_ペンネーム = self.tdss.tds[i][1].get_送り先_ペンネーム()
                        self.送り先_郵便番号 = self.tdss.tds[i][1].get_送り先_郵便番号()
                        self.送り先_住所 = self.tdss.tds[i][1].get_送り先_住所()
                        self.送り先_電話番号 = self.tdss.tds[i][1].get_送り先_電話番号()
                        self.送り先_メールアドレス = self.tdss.tds[i][1].get_送り先_メールアドレス(
                        )

                        self.購入金額 = self.tdss.tds[i][2].get_落札金額()
                        self.送料 = self.tdss.tds[i][2].get_送料()
                        self.合計金額 = self.tdss.tds[i][2].get_合計金額()

                        self.insert_add(session)

                        i = i + 1

                    except:
                        print(f"{i} 新規失敗")
                        i = i + 1

            elif session.query(self.seed).filter(self.seed.code == self.tdss.tds[i][0].get_id()).first() != None:
                # アップデート
                self.code = self.tdss.tds[i][0].get_id()
                # self.update1(i)
                self.update2(i)
                i = i + 1

            else:
                print("エラーです")

    def update1(self, i):
        print("")
        print(i)
        session = Session(bind=self.engine)
        #seed = session.query(self.seed).filter(self.seed.code == self.tdss.tds[i][0].get_id()).first()
        if self.tdss.tds[i][1].get_落札者_名前() == "" or self.tdss.tds[i][1].get_落札者_名前() == "落札者データの表示期間が終了しました。":
            print(f"{i} 落札者データの表示期間が終了しました。")

            i = i + 1
        else:
            print("アップデート")

            try:
                self.code = self.tdss.tds[i][0].get_id()
                self.siteID = self.siteID
                print(self.code)
                # create_at=datetime.datetime.now()
                self.update_at = datetime.datetime.now()

                self.日付 = self.tdss.tds[i][0].get_日付()
                self.商品コード = self.tdss.tds[i][0].get_商品コード()
                self.商品名 = self.tdss.tds[i][0].get_商品名()
                self.数量 = self.tdss.tds[i][0].get_数量()

                self.購入者_名前 = self.tdss.tds[i][1].get_落札者_名前()
                self.購入者_ペンネーム = self.tdss.tds[i][1].get_落札者_ペンネーム()
                self.購入者_郵便番号 = self.tdss.tds[i][1].get_落札者_郵便番号()
                self.購入者_住所 = self.tdss.tds[i][1].get_落札者_住所()
                self.購入者_電話番号 = self.tdss.tds[i][1].get_落札者_電話番号()
                self.購入者_メールアドレス = self.tdss.tds[i][1].get_落札者_メールアドレス(
                )

                self.送り先_名前 = self.tdss.tds[i][1].get_送り先_名前()
                self.送り先_ペンネーム = self.tdss.tds[i][1].get_送り先_ペンネーム()
                self.送り先_郵便番号 = self.tdss.tds[i][1].get_送り先_郵便番号()
                self.送り先_住所 = self.tdss.tds[i][1].get_送り先_住所()
                self.送り先_電話番号 = self.tdss.tds[i][1].get_送り先_電話番号()
                self.送り先_メールアドレス = self.tdss.tds[i][1].get_送り先_メールアドレス(
                )

                self.購入金額 = self.tdss.tds[i][2].get_落札金額()
                self.送料 = self.tdss.tds[i][2].get_送料()
                self.合計金額 = self.tdss.tds[i][2].get_合計金額()

                self.update(session)
            except:
                print(f"{i} アップデート失敗")

    def update2(self, i):
        print("")
        print(i)
        session = Session(bind=self.engine)
        seed = session.query(self.seed).filter(
            self.seed.code == self.tdss.tds[i][0].get_id()).first()
        if self.tdss.tds[i][1].get_落札者_名前() == "" or self.tdss.tds[i][1].get_落札者_名前() == "落札者データの表示期間が終了しました。":
            print(f"{i} 落札者データの表示期間が終了しました。")

            i = i + 1
        else:
            print("アップデート")

            try:
                seed.code = self.tdss.tds[i][0].get_id()
                seed.siteID = self.siteID
                print(seed.code)
                # create_at=datetime.datetime.now()
                seed.update_at = datetime.datetime.now()

                seed.日付 = self.tdss.tds[i][0].get_日付()
                seed.商品コード = self.tdss.tds[i][0].get_商品コード()
                seed.商品名 = self.tdss.tds[i][0].get_商品名()
                seed.数量 = self.tdss.tds[i][0].get_数量()

                seed.購入者_名前 = self.tdss.tds[i][1].get_落札者_名前()
                seed.購入者_ペンネーム = self.tdss.tds[i][1].get_落札者_ペンネーム()
                seed.購入者_郵便番号 = self.tdss.tds[i][1].get_落札者_郵便番号()
                seed.購入者_住所 = self.tdss.tds[i][1].get_落札者_住所()
                seed.購入者_電話番号 = self.tdss.tds[i][1].get_落札者_電話番号()
                seed.購入者_メールアドレス = self.tdss.tds[i][1].get_落札者_メールアドレス(
                )

                seed.送り先_名前 = self.tdss.tds[i][1].get_送り先_名前()
                seed.送り先_ペンネーム = self.tdss.tds[i][1].get_送り先_ペンネーム()
                seed.送り先_郵便番号 = self.tdss.tds[i][1].get_送り先_郵便番号()
                seed.送り先_住所 = self.tdss.tds[i][1].get_送り先_住所()
                seed.送り先_電話番号 = self.tdss.tds[i][1].get_送り先_電話番号()
                seed.送り先_メールアドレス = self.tdss.tds[i][1].get_送り先_メールアドレス(
                )

                seed.購入金額 = self.tdss.tds[i][2].get_落札金額()
                seed.送料 = self.tdss.tds[i][2].get_送料()
                seed.合計金額 = self.tdss.tds[i][2].get_合計金額()

                session.commit()
                # self.save(session)
            except:
                print(f"{i} アップデート失敗")


class TDss():
    def __init__(self):
        self.tds = []

    def add_td(self, td):
        self.tds.append(td)

    def test(self):
        print(self.tds[0][0].test())  # Td3 test
        print(self.tds[1][1].test())  # Td4 test
        print(self.tds[1][2].test())  # Td5 test


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

        print("get_id")
        print(self.get_id())
        print("")
        print("get_日付")
        print(self.get_日付())
        print("")
        print("get_商品コード")
        print(self.get_商品コード())
        print("")
        print("get_商品名")
        print(self.get_商品名())
        print("")
        print("get_数量")
        print(self.get_数量())
        print("")

    def get_id(self):
        temp = ""
        try:
            temp = self.soup.find_all("small")[1].text.replace(
                " （商品ページ）", "").strip()
        except:
            temp = ""
        return temp

    def get_日付(self):
        temp = ""
        try:
            temp = self.soup.find_all("small")[9].text.replace("月", "/")
            temp = temp.replace("日", "/")
            temp = temp.replace("時", ":")
            temp = temp.replace("分", "")
            temp = temp.strip()
        except:
            temp = ""
        return temp

    def get_商品名(self):
        temp = ""
        try:
            temp = self.soup.find_all("small")[7].text.strip()
        except:
            temp = ""
        return temp

    def get_商品コード(self):  # re.split('\d+', sample)
        temp = ""
        try:
            temp = re.split("\s", self.soup.find_all("small")[7].text)
            temp = temp[len(temp)-1]
            temp.strip()
        except:
            temp = ""
        return temp

    def get_数量(self):
        temp = ""
        try:
            temp = int(self.soup.find_all("small")[
                       11].text.replace("個", "").strip())
        except:
            temp = 1
        return temp


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

        print("")
        print("落札者_名前")
        print(self.get_落札者_名前())
        print("")
        print("落札者_ペンネーム")
        print(self.get_落札者_ペンネーム())
        print("")
        print("落札者_郵便番号")
        print(self.get_落札者_郵便番号())
        print("")
        print("落札者_住所")
        print(self.get_落札者_住所())
        print("")
        print("電話番号")
        print(self.get_落札者_電話番号())
        print("")
        print("落札者_メールアドレス")
        print(self.get_落札者_メールアドレス())
        print("")
        print("送り先_郵便番号")
        print(self.get_送り先_郵便番号())
        print("")
        print("送り先_住所")
        print(self.get_送り先_住所())
        print("")
        print("送り先_名前")
        print(self.get_送り先_名前())
        print("")
        print("送り先_ペンネーム")
        print(self.get_送り先_ペンネーム())
        print("")
        print("送り先_電話番号")
        print(self.get_送り先_電話番号())
        print("")
        print("送り先_メールアドレス")
        print(self.get_送り先_メールアドレス())
        print("")

    def get_落札者_名前(self):
        temp = ""
        try:
            temp = self.soup.find_all("small")[9].text.strip()
        except:
            temp = ""
        return temp

    def get_落札者_ペンネーム(self):
        temp = ""
        try:
            return temp
        except:
            temp = ""
        return temp

    def get_落札者_郵便番号(self):
        temp = ""
        try:
            return temp
        except:
            temp = ""
        return temp

    def get_落札者_住所(self):
        temp = ""
        try:
            return temp
        except:
            temp = ""
        return temp

    def get_落札者_電話番号(self):
        temp = ""
        try:
            return temp
        except:
            temp = ""
        return temp

    def get_落札者_メールアドレス(self):
        temp = ""
        try:
            temp = self.soup.find_all("small")[11].text.strip()
        except:
            temp = ""
        return temp

    def get_送り先_名前(self):
        temp = ""
        try:
            temp = self.soup.find_all("small")[3].text.strip()
        except:
            temp = ""
        return temp

    def get_送り先_ペンネーム(self):
        temp = ""
        try:
            return temp
        except:
            temp = ""
        return temp

    def get_送り先_郵便番号(self):  # re.split('\d+', sample)
        temp = ""
        try:
            temp = re.split("\s", self.soup.find_all("small")[5].text)[0]
            temp.strip()
        except:
            temp = ""
        return temp

    def get_送り先_住所(self):
        temp = ""
        try:
            temp = re.split("\s", self.soup.find_all("small")[5].text)[1]
            temp.strip()
        except:
            temp = ""
        return temp

    def get_送り先_電話番号(self):
        temp = ""
        try:
            temp = self.soup.find_all("small")[7].text.strip()
        except:
            temp = ""
        return temp

    def get_送り先_メールアドレス(self):
        temp = ""
        try:
            print("")
        except:
            temp = ""
        return temp


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

        print("落札金額")
        print(self.get_落札金額())
        print("")
        print("送料")
        print(self.get_送料())
        print("")
        print("合計金額")
        print(self.get_合計金額())
        print("")

    def get_落札金額(self):
        temp = ""
        try:
            temp = self.soup.find_all("small")[1].text.strip().replace(",", "")
            temp = temp.replace("円", "")
            temp = int(temp)
        except:
            temp = 0
        return temp

    def get_送料(self):
        temp = ""
        try:
            temp = self.soup.find_all("small")[3].text.strip().replace(",", "")
            temp = temp.replace("円", "")
            temp = int(temp)
        except:
            temp = 0
        return temp

    def get_合計金額(self):
        temp = ""
        try:
            temp = self.soup.find_all("small")[5].text.strip().replace(",", "")
            temp = temp.replace("円", "")
            temp = int(temp)
        except:
            temp = 0
        return temp


if __name__ == '__main__':
    yahoo_auction = Yahoo_auction()
    yahoo_auction.main()
