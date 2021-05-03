# -*- coding:utf-8 -*-

# 2021/05/04
# python -m pip install --upgrade pip
# pip install -U sqlalchemy
# pip install -U flake8
# pip install -U autopep8

# pip install -U openpyxl
# pip install -U beautifulsoup4
# pip install -U requests
# pip install -U pyinstaller

# pyinstaller kabu.py --onefile

#from openpyxl import load_workbook

from config import Config

import datetime
import time
import os
import random
import re
import glob

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

Base = automap_base()

# engine, suppose it has two tables 'user' and 'address' set up
#engine = create_engine("sqlite:///db.sqlite3")

# reflect the tables
#Base.prepare(engine, reflect=True)

# mapped classes are now created with names by default
# matching that of the table name.
#affiliate_video = Base.classes.Affiliate_Video_affiliate_video
#affiliate_video_pic = Base.classes.Affiliate_Video_affiliate_video_pic

#session = Session(engine)


class Mail_order_site():
    def setup(self):
        Base = automap_base()

        self.config = Config()

        # engine, suppose it has two tables 'user' and 'address' set up
        self.engine = create_engine(self.config.db_path)
        # 個人情報の塊なのでGITの外に設置

        # reflect the tables
        Base.prepare(self.engine, reflect=True)

        # mapped classes are now created with names by default
        # matching that of the table name.
        
        self.seeds = Base.classes.seeds
        self.seed = Base.classes.seed
        self.site = Base.classes.site
        self.sale = Base.classes.sale
        
        self.siteID = 0
        # 0	アマゾン
        # 1	楽天
        # 2	ヤフオク
        # 3	ラクマ
        # 4	ストアーズ
        
        #self.seed = self.get

    def get_data(self):
        session = Session(bind = self.engine, autocommit = True, autoflush = True)
        self.data = session.query(self.seeds).filter(self.seeds.siteID == self.siteID and self.seeds.analysis_completed == False).first()
        return self.data
    
    def get_seed(self):
        session = Session(bind = self.engine, autocommit = True, autoflush = True)
        self.data = session.query(self.seeds).filter(self.seeds.siteID == self.siteID and self.seeds.analysis_completed == False).first()
        return self.data.seed



    def get_id(self):
        return
        
    def get_購入者_名前(self):
        return
    
    def get_購入者_ペンネーム(self):
        return
    
    def get_購入者_郵便番号(self):
        return

    def get_購入者_住所(self):
        return
    
    def get_購入者_電話番号(self):
        return
    
    def get_購入者_メールアドレス(self):
        return


    
    def get_送り先_名前(self):
        return
    
    def get_送り先_ペンネーム(self):
        return
    
    def get_送り先_郵便番号(self):
        return
    
    def get_送り先_住所(self):
        return
        
    def get_送り先_電話番号(self):
        return
    
    def get_送り先_メールアドレス(self):
        return
        


    def get_日付(self):
        return

    def get_商品コード(self):
        return
        
    def get_商品名(self):
        return

    def get_数量(self):
        return

    def get_下代_消費税抜き(self):
        return
    
    def get_下代_消費税あり(self):
        return
    
    def get_下代_消費税(self):
        return
    
    def get_売上単価(self):
        return

    def get_上代_消費税抜き(self):
        return
    
    def get_上代_消費税あり(self):
        return

    def get_上代_消費税(self):
        return

    def get_備考(self):
        return

    def insert_add(self, session):
            try:
                session.add(self.seed(code = self.code,
                                            siteID=self.siteID,
                                            create_at=datetime.datetime.now(),
                                            update_at=datetime.datetime.now(),

                                            purchase_date = self.日付,
                                            product_code = self.商品コード,
                                            Product_name = self.商品名,
                                            quantity = self.数量,

                                            buyer_name = self.購入者_名前,
                                            buyer_pen_name = self.購入者_ペンネーム,
                                            buyer_zip_code = self.購入者_郵便番号,
                                            buyer_address = self.購入者_住所,
                                            buyer_phone_number = self.購入者_電話番号,
                                            buyer_email_address = self.購入者_メールアドレス,

                                            destination_name = self.送り先_名前,
                                            destination_pen_name = self.送り先_ペンネーム,
                                            destination_zip_code = self.送り先_郵便番号,
                                            destination_address = self.送り先_住所,
                                            destination_phone_number = self.送り先_電話番号,
                                            destination_email_address = self.送り先_メールアドレス,

                                            purchase_price = self.購入金額,
                                            shipping = self.送料,
                                            total_fee = self.合計金額,
                                            ))
                self.save(session)
            except:
                print("追加失敗")


    def update(self, session):
        try:

            session = session
            seed = session.query(self.seed).filter(self.seed.code == self.code)
            
            seed.update_at = datetime.datetime.now

            seed.purchase_date = self.日付
            seed.product_code = self.商品コード
            seed.Product_name = self.商品名
            seed.quantity = self.数量
            

            #if seed.buyer_name == "":
            seed.buyer_name = self.購入者_名前
            #if seed.buyer_pen_name == "":
            seed.buyer_pen_name = self.購入者_ペンネーム
            #if seed.buyer_zip_code == "":
            seed.buyer_zip_code = self.購入者_郵便番号
            #if seed.buyer_address == "":
            seed.buyer_address = self.購入者_住所
            #if seed.buyer_phone_number == "":
            seed.buyer_phone_number = self.購入者_電話番号
            #if seed.buyer_email_address == "":
            seed.buyer_email_address = self.購入者_メールアドレス

            #if seed.destination_name == "":
            seed.destination_name = self.送り先_名前
            #if seed.destination_pen_name == "":
            seed.destination_pen_name = self.送り先_ペンネーム
            #if seed.destination_zip_code == "":
            seed.destination_zip_code = self.送り先_郵便番号
            #if seed.destination_address == "":
            seed.destination_address = self.送り先_住所
            #if seed.destination_phone_number == "":
            seed.destination_phone_number = self.送り先_電話番号
            #if seed.destination_phone_number == "":
            seed.destination_email_address = self.送り先_メールアドレス

            #if seed.purchase_price == "" or seed.purchase_price == None:
            seed.purchase_price = self.購入金額
            #if seed.shipping == "":
            seed.shipping = self.送料
            #if seed.total_fee == "":
            seed.total_fee = self.合計金額

            self.save(session)
            
        except:
            print(f"アップデート失敗")

    def update_analysis_completed(self):
        session = Session(bind = self.engine, autocommit = True, autoflush = True)
        print("self.siteID")
        print(self.siteID)
        seeds = session.query(self.seeds).filter(self.seeds.siteID == self.siteID and self.seeds.analysis_completed == False).first()
        print("seeds.siteID")
        print(seeds.siteID)
        print("seeds.analysis_completed")
        print(seeds.analysis_completed)
        seeds.code = self.code
        seeds.analysis_completed = True
        seeds.update_at = datetime.datetime.now()
        print("回収")
        #session.commit()
        self.save(session)
        

    def save(self, session):
        session = session
        i = 0
        while i <= 5:
            try:
                time.sleep(1)
                #session.commit()
                time.sleep(1)
                i = 6 + 1
            except:
                print(i)
                time.sleep(5)
                i = i + 1
    


if __name__ == '__main__':
    mail_order_site = Mail_order_site()
    mail_order_site.setup()
    mail_order_site.update_analysis_completed()
    
    #print(mail_order_site.siteID)
    #print(mail_order_site.get_seed())
