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



        self.mail_order_site = Mail_order_site()
        self.mail_order_site.siteID = 2
        self.get_data()
        self.test()

    def get_data(self):
        self.data = self.mail_order_site.get_data()
        return self.data
        
    def test(self):
        with open("./../../mail_order_site2.html", 'w', encoding="utf-8") as f:
            f.write(str(self.get_data().seed))


        


if __name__ == '__main__':
    yahoo_auction = Yahoo_auction()
    #yahoo_auction.main()
