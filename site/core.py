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

class Core():
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
    
    def 削除する(self, code):
        print(f"{code} MGS 削除します")
        os.remove(code)
    
    def seed_save(self):
        for dir in glob.glob(f'{self.config.download_path}amazon*.html'):
            if dir != None:
                with open(dir, 'r', encoding="utf-8") as f:
                    self.seed1 = f.read()
                self.seed1 = self.seed1.replace("\n", "")
                self.seed1 = self.seed1.replace("\r", "")
            
                #dmm = Analysis_MGS(self.seed1)
                session = Session(self.engine)
            
                self.seed = session.query(self.seed).filter(self.seed)
                session.add(self.seed.seed == self.seed)
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
        
    def load(self):
        print("load")
        
        
if __name__ == '__main__':
    
    core = Core()
    core.seed_save()
    print(core)