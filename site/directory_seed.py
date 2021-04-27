# -*- coding:utf-8 -*-

# 2021/04/25
# pip install -U sqlalchemy



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
    def __init__(self):
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
        session = Session(self.engine)
        self.data = session.query(self.seeds).filter(self.seeds.siteID == self.siteID and self.seeds.analysis_completed == False).first()
        return self.data
    
    def get_seed(self):
        session = Session(self.engine)
        self.data = session.query(self.seeds).filter(self.seeds.siteID == self.siteID and self.seeds.analysis_completed == False).first()
        return self.data.seed



    def get_id(self):
        #td3_0 > table > tbody > tr:nth-child(1) > td:nth-child(2) > small
        #td3_1 > table > tbody > tr:nth-child(1) > td:nth-child(2) > small
        return
        
    def get_買い主_名前(self):
        #td4_0 > table > tbody > tr:nth-child(5) > td:nth-child(2)

        return
    
    def get_買い主_ペンネーム(self):
        return
    
    def get_買い主_郵便番号(self):
        return

    def get_買い主_住所(self):
        
        return
    
    def get_買い主_電話番号(self):
        
        return
    
    def get_買い主_メールアドレス(self):
        #td4_0 > table > tbody > tr:nth-child(6) > td:nth-child(2) > small
        return



    def get_送り先_郵便番号(self):
        return
    
    def get_送り先_名前(self):
                #td4_0 > table > tbody > tr:nth-child(2) > td:nth-child(2) > small
        #td4_1 > table > tbody > tr:nth-child(2) > td:nth-child(2) > small
        return
    
    def get_送り先_ペンネーム(self):
        return
    
    def get_送り先_住所(self):
        #td4_0 > table > tbody > tr:nth-child(3) > td:nth-child(2) > small
        return
        
    def get_送り先_電話番号(self):
        #td4_0 > table > tbody > tr:nth-child(4) > td:nth-child(2) > small
        return
    
    def get_送り先_メールアドレス(self):
        return
        
    def get_送り先_住所(self):
        return


    def get_日付
    #td3_0 > table > tbody > tr:nth-child(5) > td:nth-child(2) > small
    #td3_1 > table > tbody > tr:nth-child(5) > td:nth-child(2) > small

    def get_商品コード(self):
    #td3_0 > table > tbody > tr:nth-child(4) > td:nth-child(2) > small > a
    #td3_1 > table > tbody > tr:nth-child(4) > td:nth-child(2) > small > a
        
    def get_商品名
    #td3_0 > table > tbody > tr:nth-child(4) > td:nth-child(2) > small > a
    #td3_1 > table > tbody > tr:nth-child(4) > td:nth-child(2) > small > a

    def get_数量
    #td3_1 > table > tbody > tr:nth-child(6) > td:nth-child(2) > small

    def get_下代_消費税抜き
    
    def get_下代_消費税あり
    
    def get_下代_消費税
    
    def get_売上単価

    def get_上代_消費税抜き
    
    def get_上代_消費税あり

    def get_上代_消費税
    
    def get_販売先_id
    
    def get_販売先名
    
    def get_備考

if __name__ == '__main__':
    mail_order_site = Mail_order_site()
    data = mail_order_site.get_data()
    #print(mail_order_site.siteID)
    #print(mail_order_site.get_seed())
