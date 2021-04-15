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

class Core():
    def __init__(self)
        Base = automap_base()

        # engine, suppose it has two tables 'user' and 'address' set up
        engine = create_engine("sqlite:///db.sqlite3")

        # reflect the tables
        Base.prepare(engine, reflect=True)

        # mapped classes are now created with names by default
        # matching that of the table name.
        affiliate_video = Base.classes.Affiliate_Video_affiliate_video
        affiliate_video_pic = Base.classes.Affiliate_Video_affiliate_video_pic

        session = Session(engine)
        
        def save(self, seed):
        
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
        