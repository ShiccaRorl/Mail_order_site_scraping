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

        self.siteID = 2

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
        self.tdss = TDss()
        while i <= self.config.yahoo_auction_page:

            soup3 = self.soup.find('td', {'id': f'td3_{i}'})
            td3 = Td3(soup3)

            soup4 = self.soup.find('td', {'id': f'td4_{i}'})
            td4 = Td4(soup4)

            soup5 = self.soup.find('td', {'id': f'td5_{i}'})
            td5 = Td5(soup5)

            self.tdss.add_td([td3, td4, td5])
            i = i + 1

        # self.tdss.test() # test mode
        self.db()

    def db(self):

        session = Session(self.engine)
        i = 0
        while i <= self.config.yahoo_auction_page:
            if (session.query(self.seeds).filter(self.seeds.id == self.tdss.tds[i][0].get_id()).first()) == None:
                # 新規追加

                if self.tdss.tds[i][1].get_落札者_名前() == "":
                    print(f"{i} まだ早い")

                    i = i + 1
                else:
                    print(f"{i} 新規追加")
                    try:
                        session.add(self.seeds(id=self.tdss.tds[i][0].get_id(),
                                            siteID=self.siteID,
                                            create_at=datetime.datetime.now(),
                                            update_at=datetime.datetime.now(),

                                            購入日付=self.tdss.tds[i][0].get_日付(),
                                            商品コード=self.tdss.tds[i][0].get_商品コード(),
                                            商品名=self.tdss.tds[i][0].get_商品名(),
                                            数量=self.tdss.tds[i][0].get_数量(),

                                            購入者_名前=self.tdss.tds[i][1].get_落札者_名前(),
                                            購入者_ペンネーム=self.tdss.tds[i][1].get_落札者_ペンネーム(),
                                            購入者_郵便番号=self.tdss.tds[i][1].get_落札者_郵便番号(),
                                            購入者_住所=self.tdss.tds[i][1].get_落札者_住所(),
                                            購入者_電話番号=self.tdss.tds[i][1].get_落札者_電話番号(),
                                            購入者_落札者_メールアドレス=self.tdss.tds[i][1].get_落札者_メールアドレス(),

                                            送り先_名前=self.tdss.tds[i][1].get_送り先_名前(),
                                            送り先_ペンネーム=self.tdss.tds[i][1].get_送り先_ペンネーム(),
                                            送り先_郵便番号=self.tdss.tds[i][1].get_送り先_郵便番号(),
                                            送り先_住所=self.tdss.tds[i][1].get_送り先_住所(),
                                            送り先_電話番号=self.tdss.tds[i][1].get_送り先_電話番号(),
                                            送り先_メールアドレス=self.tdss.tds[i][1].get_送り先_メールアドレス(),

                                            売上金額=self.tdss.tds[i][2].get_落札金額(),
                                            送料=self.tdss.tds[i][2].get_送料(),
                                            合計金額=self.tdss.tds[i][2].get_合計金額(), ))

                        i = i + 1

                        s = 0
                        while s <= 5:
                            try:
                                time.sleep(1)
                                session.commit()
                                time.sleep(1)
                                s = 6 + 1
                            except:
                                time.sleep(5)
                                s = s + 1
                                print(s)
                    except:
                        print(f"{i} 新規失敗")





            elif (session.query(self.seeds).filter(self.seeds.id == self.tdss.tds[i][0].get_id()).first()) != None:
                # アップデート
                print(i)
                session = Session(self.engine)
                seeds = session.query(self.seeds).filter(
                    self.seeds.id == self.tdss.tds[i][0].get_id()).first()
                if "落札者データの表示期間が終了しました。 " == self.tdss.tds[i][1].get_落札者_名前():
                    print("落札者データの表示期間が終了しました。 ")
                else:
                    print("アップデート")

                    try:
                        seeds.siteID = self.siteID

                        # create_at=datetime.datetime.now()
                        seeds.update_at = datetime.datetime.now()

                        seeds.購入日付 = self.tdss.tds[i][0].get_日付()
                        seeds.商品コード = self.tdss.tds[i][0].get_商品コード()
                        seeds.商品名 = self.tdss.tds[i][0].get_商品名()
                        seeds.数量 = self.tdss.tds[i][0].get_数量()

                        if seeds.購入者_名前 == "":
                            seeds.購入者_名前 = self.tdss.tds[i][1].get_落札者_名前()
                        if seeds.購入者_ペンネーム == "":
                            seeds.購入者_ペンネーム = self.tdss.tds[i][1].get_落札者_ペンネーム()
                        if seeds.購入者_郵便番号 == "":
                            seeds.購入者_郵便番号 = self.tdss.tds[i][1].get_落札者_郵便番号()
                        if seeds.購入者_住所 == "":
                            seeds.購入者_住所 = self.tdss.tds[i][1].get_落札者_住所()
                        if seeds.購入者_電話番号 == "":
                            seeds.購入者_電話番号 = self.tdss.tds[i][1].get_落札者_電話番号()
                        if seeds.購入者_落札者_メールアドレス == "":
                            seeds.購入者_落札者_メールアドレス = self.tdss.tds[i][1].get_落札者_メールアドレス()

                        if seeds.送り先_名前 == "":
                            seeds.送り先_名前 = self.tdss.tds[i][1].get_送り先_名前()
                        if seeds.送り先_ペンネーム == "":
                            seeds.送り先_ペンネーム = self.tdss.tds[i][1].get_送り先_ペンネーム()
                        if seeds.送り先_郵便番号 == "":
                            seeds.送り先_郵便番号 = self.tdss.tds[i][1].get_送り先_郵便番号()
                        if seeds.送り先_住所 == "":
                            seeds.送り先_住所 = self.tdss.tds[i][1].get_送り先_住所()
                        if seeds.送り先_電話番号 == "":
                            seeds.送り先_電話番号 = self.tdss.tds[i][1].get_送り先_電話番号()
                        if seeds.送り先_メールアドレス == "":
                            seeds.送り先_メールアドレス = self.tdss.tds[i][1].get_送り先_メールアドレス()
                        if seeds.売上金額 == "":
                            seeds.売上金額 = self.tdss.tds[i][2].get_落札金額()
                        if seeds.送料 == "":
                            seeds.送料 = self.tdss.tds[i][2].get_送料()
                        if seeds.合計金額 == "":
                            seeds.合計金額 = self.tdss.tds[i][2].get_合計金額()

                        i = i + 1

                        s = 0
                        while s <= 5:
                            try:
                                time.sleep(1)
                                session.commit()
                                time.sleep(1)
                                s = 6 + 1
                            except:
                                time.sleep(5)
                                s = s + 1
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
        temp = self.soup.find_all("small")[7].text.split('　')
        temp = temp[len(temp) - 1]
        return temp.strip()

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
        temp = self.soup.find_all("small")[1].text.strip().replace(",", "")
        temp = temp.replace("円", "")
        return int(temp)

    def get_送料(self):
        temp = self.soup.find_all("small")[3].text.strip().replace(",", "")
        temp = temp.replace("円", "")
        return int(temp)

    def get_合計金額(self):
        temp = self.soup.find_all("small")[5].text.strip().replace(",", "")
        temp = temp.replace("円", "")
        return int(temp)


if __name__ == '__main__':
    yahoo_auction = Yahoo_auction()
    yahoo_auction.main()
