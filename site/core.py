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
        
    def 削除する(self, code):
        print(f"{code} MGS 削除します")
        os.remove(code)
    
    def seed_save_add():
        for dir in glob.glob(f"{self.dir}{self.name}*.html"):
            if dir != None:
                print(dir)
                self.seed1 = self.load(dir)
                #dmm = Analysis_MGS(self.seed1)
                session = Session(self.engine)

                self.seed = session.query(self.seed)
                session.add(self.seed(siteID=self.siteID,
                                      seed=self.seed1,
                                      create_at=datetime.datetime.now(),))
                
                self.save(session)
            
                self.削除する(dir)

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
    
    amazon = Store_Core()
    amazon.self.name = "amazon"
    amazon.dir = f'{self.config.download_path}amazon*.html'
    amazon.siteID = 0
    amazon.seed_save_add()
    
    #core.seed_save_amazon()
    
    stores = Store_Core()
    stores.self.name = "stores"
    stores.dir = f'{self.config.download_path}stores*.html'
    stores.siteID = 4
    stores.seed_save_add()
    
    #core.seed_save_stores()
    
    rakuten_rakuma = Store_Core()
    rakuten_rakuma.self.name = "rakuten_rakuma"
    rakuten_rakuma.dir = f'{self.config.download_path}rakuten_rakuma*.html'
    rakuten_rakuma.siteID = 3
    rakuten_rakuma.seed_save_add()
    
    #core.seed_save_rakuten_rakuma()
    
    rakuten = Store_Core()
    rakuten.self.name = "rakuten"
    rakuten.dir = f'{self.config.download_path}rakuten*.html'
    rakuten.siteID = 1
    rakuten.seed_save_add()
    
    #core.seed_save_rakuten()
    
    auctions_yahoo = Store_Core()
    auctions_yahoo.self.name = "auctions_yahoo"
    auctions_yahoo.dir = f'{self.config.download_path}auctions_yahoo*.html'
    auctions_yahoo.siteID = 2
    auctions_yahoo.seed_save_add()
    
    #core.seed_save_auctions_yahoo()
    #print(core)