# -*- coding:utf-8 -*-

import datetime
import time
import os
import random
import re
import glob

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from config import Config


class Store_Core():
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
        self.seed = Base.classes.seed
        self.site = Base.classes.site

        #session = Session(self.engine)
        
        #config.download_path
        self.name = ""
        self.dir = ""
        self.siteID = 0
        
    def 削除する(self, dir):
        print(f"{dir} 削除します")
        os.remove(dir)
    
    def seed_save_add(self):
        for d in glob.glob(self.dir):
            print(d)
            if d != None:
                self.seed1 = self.load(d)

                session = Session(self.engine)

                #seeds = session.query(self.seed)
                session.add(self.seed(siteID=self.siteID,
                                    seed=self.seed1,
                                    create_at=datetime.datetime.now(),))
                                    解析完了 = False
                self.save(session)
            
                self.削除する(d)

    def save(self, session):
        i = 0
        while i <= 5:
            try:
                time.sleep(1)
                session.commit()
                time.sleep(1)
                i = 6 + 1
            except:
                time.sleep(5)
                i = i + 1
        
    def load(self, dir):
        with open(dir, 'r', encoding="utf-8") as f:
            self.seed1 = f.read()
        self.seed1 = self.seed1.replace("\n", "")
        self.seed1 = self.seed1.replace("\r", "")
        return self.seed1
        
        
if __name__ == '__main__':
    
    config = Config()
    amazon = Store_Core()
    amazon.name = "amazon"
    amazon.dir = f'{config.download_path}{amazon.name}*.html'
    amazon.siteID = 0
    amazon.seed_save_add()
    
    #core.seed_save_amazon()
    
    stores = Store_Core()
    stores.name = "stores"
    stores.dir = f'{config.download_path}{stores.name}*.html'
    stores.siteID = 4
    stores.seed_save_add()
    
    #core.seed_save_stores()
    
    rakuten_rakuma = Store_Core()
    rakuten_rakuma.name = "rakuten_rakuma"
    rakuten_rakuma.dir = f'{config.download_path}{rakuten_rakuma.name}*.html'
    rakuten_rakuma.siteID = 3
    rakuten_rakuma.seed_save_add()
    
    #core.seed_save_rakuten_rakuma()
    
    rakuten = Store_Core()
    rakuten.name = "rakuten"
    rakuten.dir = f'{config.download_path}{rakuten.name}*.html'
    rakuten.siteID = 1
    rakuten.seed_save_add()
    
    #core.seed_save_rakuten()
    
    auctions_yahoo = Store_Core()
    auctions_yahoo.name = "auctions_yahoo"
    auctions_yahoo.dir = f'{config.download_path}{auctions_yahoo.name}*.html'
    auctions_yahoo.siteID = 2
    auctions_yahoo.seed_save_add()
    
    #core.seed_save_auctions_yahoo()
    #print(core)