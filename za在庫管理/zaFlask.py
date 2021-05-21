# -*- coding:utf-8 -*-

# pip install sqlalchemy
# pip install flask-sqlalchemy
# pip install sqlalchemy-migrate
# pip install beautifulsoup4
#from Editer.app.models import Affiliate_Video
#from Editer.app.models import Affiliate_Video
import os
import sys
import re
import subprocess
from flask import Flask, render_template, request, make_response
#from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, DateTime, Boolean

from flask import g

#from . import models
import datetime
import time
import random
import html

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import desc

from V6_database import Tags

Base = automap_base()

# engine, suppose it has two tables 'user' and 'address' set up
engine = create_engine("sqlite:///db.sqlite3")

# reflect the tables
Base.prepare(engine, reflect=True)

# mapped classes are now created with names by default
# matching that of the table name.
dir_db = Base.classes.dir_db
Product = Base.classes.Product
再登録日 = Base.classes.再登録日

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret key'



@app.route("/")
def index():
    return render_template("jumbotron-narrow.html")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000, threaded=True)