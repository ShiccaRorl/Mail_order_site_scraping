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
        
        def save(self):
        
        def load(self):
        