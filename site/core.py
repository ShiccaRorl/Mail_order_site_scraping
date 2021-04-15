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

form config from Config

class Core():
    def __init__(self)
        config = Config()
        Base = automap_base()

        # engine, suppose it has two tables 'user' and 'address' set up
        engine = create_engine(config.db_path)
        # 個人情報の塊なのでGITの外に設置

        # reflect the tables
        Base.prepare(engine, reflect=True)

        # mapped classes are now created with names by default
        # matching that of the table name.
        seed = Base.classes.seed
        site = Base.classes.site

        session = Session(engine)
        
        config.download_path
        
    def seed_save(self):
        for dir in glob.glob('C:\\Users\\ban\\Downloads\\amazon*.html'):
            with open(dir, 'r', encoding="utf-8") as f:
                self.seed1 = f.read()
            self.seed1 = self.seed1.replace("\n", "")
            self.seed1 = self.seed1.replace("\r", "")
            
            #dmm = Analysis_MGS(self.seed1)
            session = Session(engine)
            
            self.file_list.append(dmm.code)
            seed = session.query(self.seed).filter(self.seed)
            session.add(self.seed.seed = self.seed)
            save(session)
            
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
        