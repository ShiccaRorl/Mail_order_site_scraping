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
        self.data = session.query(self.seeds).filter(self.seeds.siteID == self.siteID).filter(self.seeds.analysis_completed == False).first
        return self.data





if __name__ == '__main__':
    mail_order_site = Mail_order_site()
    data = mail_order_site.get_data()
    print(data.id)
