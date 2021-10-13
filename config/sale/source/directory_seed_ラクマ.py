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


class Rakuma(Mail_order_site):
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

        self.seeds = Base.classes.seeds_seeds
        self.site = Base.classes.seeds_t_販売サイト
        self.sale = Base.classes.sale_sele
        
        


    def get_data2(self):
        self.data = self.get_data()
        return str(self.data.seed)

    def get_seed2(self):
        self.data = self.get_data()
        return self.data.replace("charset=euc-jp", 'charset="UTF-8"')

    def test(self):
        with open("./../../mail_order_site3.html", 'w', encoding="utf-8") as f:
            f.write(str(self.get_seed()))
        #print(self.test())
        print("")
        print("id")
        print(self.get_id())
        print("")
        print("日付")
        print(self.get_日付())
        print("")
        #print("商品明細")
        #print(self.get_商品明細())
        print("")
        print(self.get_商品バリエーション())
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

    def get_id(self):
        # <input type="hidden" name="item_id" id="item_id" value="428254311" />
        try:
            soup = self.soup.find('input', {'id': 'item_id'})
            temp = soup.text.strip()
        except:
            temp = ""
        return temp

    def get_日付(self):
        # <p class="small-text right-align">2021/05/19 06:40</p>
        try:
            soup = self.soup.find('p', {'class': 'small-text right-align'})
            #s = 0
            #for i in soup.find_all("td"):
            #    print(s)
            #    print(i)
            #    s = s + 1
            temp = soup.text
            return temp
        except:
            temp = ""
            return temp


    def get_商品明細(self):
        try:
            #s = 0
            #for i in self.soup.find_all('div', {'class': 'rms-row-wrapper'}):
            #    print(f"====={s}====")
            #    print(i)
            #    print("")
            #    s = s + 1
            soup = self.soup.find_all('div', {'class': 'rms-row-wrapper'})[13]
        except:
            soup = ""
        return soup

    def get_商品バリエーション(self):
        try:
            self.products = []
            soup = self.get_商品明細().find('tbody')
            for i in soup.find_all('tr'):
                print(i)
                product = Product()
                product.set_tr(i)
                product.get_商品名()
                self.products.append(product)
            #t = 0
            #for s in soup:
            #    print(f"===={t}====")
            #    print(s)
            #    print("")
            #    t = t + 1
        except:
            soup = ""
        return soup


    def get_商品コード(self):
        try:
            temp = self.product.get_商品コード()
            temp = soup.text.strip()
        except:
            temp = ""
        return temp

    def get_商品名(self):
        # <h2 class="item_name">新品送料込み　腰紐三本セット　白　こしひも　浴衣、着物に　AWK071-3</h2>
        try:
            for i in self.products:
                print(i)
                print(i.get_商品名())
            temp = self.product[2].get_商品名()
            # = self.get_商品バリエーション().find('a', {'class': f'rms-span-open-in-new'})
            temp = temp.text.strip()
        except:
            temp= ""
        return temp

    def get_数量(self):
        try:
            #temp = self.get_商品バリエーション().find('div', {'class': f'rms-table-column-line'})
            temp = self.product.get_数量()
            temp = int(soup.text.strip())
        except:
            temp = 0
        return temp


    def get_注文者_名前(self):
        # <p>
        #    〒 841-0083<br>
        #    山田町721-32 <br>
        #    名前 様
        #  </p>
        try:
            soup = self.soup.find('span', {'class': f'fullname'})
            temp = soup.text.strip()
        except:
            temp = ""
        return temp

    def get_注文者_ペンネーム(self):
        # <p class="small-text">ペンネーム</p>
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
            temp = ""
            return temp
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
            temp = ""
            return temp
        except:
            temp = ""
        return temp

    def get_購買額(self):
        # <div class="col s6 right-align">¥ 750</div>
        try:
            soup = self.soup.find('span', {'class': f'footer-price'})
            temp = soup.text.strip()
        except:
            temp = ""
        return temp

        # ラクマパック
        #<div class="col s6 grey-text">かんたんラクマパック利用料<br><span class="gray-text small-text">ゆうパケット</span></div>
        # <div class="col s6 right-align grey-text">- ¥ 179</div>

    def main(self):
        self.siteID = 1
        all = []
        session = Session(bind = self.engine, autocommit = True, autoflush = True)
        all = session.query(self.seeds).filter(
            self.seeds.siteID == self.siteID and self.seeds.analysis_completed == 0).all()
        
        test = session.query(self.seeds).filter(
            self.seeds.siteID == self.siteID and self.seeds.analysis_completed == 0).first()
        
        print(test)
        
        """
        for t in all:
            # print(i)
            
            #self.get_data()
            self.soup = BeautifulSoup(self.get_seed(), "html.parser")
            self.test()
        
            self.db()
            self.update_analysis_completed(t.id)
            print(t.id)
            time.sleep(1)
            """

    def db(self):

        i = 0
        session = Session(bind = self.engine, autocommit = True, autoflush = True)
        if session.query(self.seed).filter(self.seed.code == self.get_id()).first() == None:
                # 新規追加

                    print("")
                    print(f"{self.get_id()} 新規追加")
                    
                    try:
                        self.code = self.get_id()
                        self.siteID = self.siteID
                        self.create_at = datetime.datetime.now()
                        self.update_at = datetime.datetime.now()

                        self.日付 = self.get_日付()
                        #self.商品コード = self.tdss.tds[i][0].get_商品コード()
                        #self.商品名 = self.tdss.tds[i][0].get_商品名()
                        #self.数量 = self.tdss.tds[i][0].get_数量()

                        self.購入者_名前 = self.get_注文者_名前()
                        self.購入者_ペンネーム = self.get_注文者_ペンネーム()
                        self.購入者_郵便番号 = self.get_注文者_郵便番号()
                        self.購入者_住所 = self.get_注文者_住所()
                        self.購入者_電話番号 = self.get_注文者_電話番号()
                        self.購入者_メールアドレス = self.get_注文者_メールアドレス()

                        self.送り先_名前 = self.get_送り先_名前()
                        self.送り先_ペンネーム = self.get_送り先_ペンネーム()
                        self.送り先_郵便番号 = self.get_送り先_郵便番号()
                        self.送り先_住所 = self.get_送り先_住所()
                        self.送り先_電話番号 = self.get_送り先_電話番号()
                        self.送り先_メールアドレス = self.get_送り先_メールアドレス()

                        self.購入金額 = ""
                        self.送料 = ""
                        self.合計金額 = ""

                        self.insert_add(session)

                        

                    except:
                        print(f"{i} 新規失敗")
                        

        elif session.query(self.seed).filter(self.seed.code == self.get_id()).first() != None:
                # アップデート
                        self.code = self.get_id()
                        #self.update1(i)
                        self.update2()
        else:
                print("エラーです")

    def update2(self): 
                print("")
                session = Session(bind = self.engine, autocommit = True, autoflush = True)
                seed = session.query(self.seed).filter(self.seed.code == self.get_id()).first()
                    

                print("アップデート")

                try:
                        seed.code = self.get_id()
                        seed.siteID = self.siteID
                        print(seed.code)
                        # create_at=datetime.datetime.now()
                        seed.update_at = datetime.datetime.now()

                        seed.日付 = self.get_日付()
                        seed.商品コード = ""
                        seed.商品名 = ""
                        seed.数量 = ""

                        seed.購入者_名前 = self.get_注文者_名前()
                        seed.購入者_ペンネーム = self.get_注文者_ペンネーム()
                        seed.購入者_郵便番号 = self.get_注文者_郵便番号()
                        seed.購入者_住所 = self.get_注文者_住所()
                        seed.購入者_電話番号 = self.get_注文者_電話番号()
                        seed.購入者_メールアドレス = self.get_注文者_メールアドレス()

                        seed.送り先_名前 = self.get_送り先_名前()
                        seed.送り先_ペンネーム = self.get_送り先_ペンネーム()
                        seed.送り先_郵便番号 = self.get_送り先_郵便番号()
                        seed.送り先_住所 = self.get_送り先_住所()
                        seed.送り先_電話番号 = self.get_送り先_電話番号()
                        seed.送り先_メールアドレス = self.get_送り先_メールアドレス()

                        seed.購入金額 = ""
                        seed.送料 = ""
                        seed.合計金額 = ""

                        session.commit()
                        #self.save(session)
                except:
                        print(f"{i} アップデート失敗")

class Product():
    def set_code(self, code):
        self.code = code

    def get_code(self):
        return self.code

    def set_tr(self, tr):
        self.tr_soup = tr

    def get_商品コード(self):
        temp = re.split("\s", self.get_商品名())
        temp = temp[len(temp)-1]
        return temp

    def get_商品名(self):
        return self.tr_soup.find('a', {'class': f'rms-span-open-in-new'}).text.strip()


    def get_数量(self):
        return self.tr_soup.find('div', {'class': "rms-table-column-line"})

if __name__ == '__main__':
    rakuma = Rakuma()
    rakuma.main()
