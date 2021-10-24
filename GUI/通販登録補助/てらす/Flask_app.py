# -*- coding:utf-8 -*-

# pip install sqlalchemy
# pip install flask-sqlalchemy
# pip install sqlalchemy-migrate
# pip install beautifulsoup4
#from Editer.app.models import Affiliate_Video
#from Editer.app.models import Affiliate_Video
from V5_Config import Mgs_config, Dmm_config
from V6_analysis_DMM import Analysis_DMM
from V6_analysis_MGS import Analysis_MGS
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
import subprocess

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import desc

from V6_sqlalchemy_models import Affiliate_Video, Affiliate_Video_Pic
engine = create_engine("sqlite:///db.sqlite3")

Base = automap_base()

# engine, suppose it has two tables 'user' and 'address' set up
#engine = get_engine()

# reflect the tables
Base.prepare(engine, reflect=True)

# mapped classes are now created with names by default
# matching that of the table name.


affiliate_video = Base.classes.Affiliate_Video
affiliate_video_pic = Base.classes.Affiliate_Video_Pic


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret key'
# DBへのパス
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./../../DB/Affiliate.SQLite3'

# SQLAlchemyでデータベース定義

#db = SQLAlchemy(app)


@app.route("/", methods=["GET", "POST"])
@app.route("/kyonoyome_edit", methods=["GET", "POST"])
def index():
    #affiliate_video = Base.classes.Affiliate_Video
    affiliate_video_pic = Base.classes.Affiliate_Video_Pic
    if request.method == "GET":
        # http://localhost:8000/kyonoyome_edit?get_code=hoisw00002
        code = request.args.get('get_code', '')
        print("==================" + code)
        if code == None or code == "":
            code = "390JAC-016"
        session = Session(engine)
        #video = session.query(self.affiliate_video).filter(Affiliate_Video.code == get_code).first()

        pics = session.query(Affiliate_Video_Pic).filter(affiliate_video_pic.code == code).all()
        print("======")
        print(pics)

        cunt = 0
        sam = []
        for pic in pics:
            sam.append([code, cunt, pic.url, pic.comment])
            cunt = cunt + 1
        # print(サムネイル3)
        #pic2 = []

        """
        with open('./temp/sam.csv') as f:
            writer = csv.writer(f)
            cunt = 0
            for pic in pics:
                writer.writerow([code, cunt, pic.url, pic.comment])
                cunt = cunt + 1
        """
        text=[]
        for i in pics:
            text.append(i.url)
        
        
        with open('./temp/code.txt', 'w', encoding='UTF-8') as f:
            f.write(code)
            
        with open('./temp/url.txt', 'w', encoding='UTF-8') as f:
            f.write("\n".join(text))
                

        # 入力取り込み_mgs()

        return render_template("Editer.html",
                               code=code,
                               sam=sam,
                               )

    elif request.method == 'POST':
        print("postだった")
    else:
        print("データが分からない")


@app.route("/kyonoyome_save", methods=["GET", "POST"])
def save():
    if request.method == 'POST':
        """
        #select = request.form.get('select')
        seed1 = request.form.get('seed1')
        seed2 = request.form.get('seed2')
        code = request.form.get('code')
        登録日 = request.form.get('登録日')
        更新日 = request.form.get('更新日')
        seed_有 = request.form.getlist('seed_有')
        seed_error = request.form.get('seed_error')
        サイトid = request.form.get('サイトid')
        女優 = request.form.get('女優')
        解析終了 = request.form.getlist('解析終了')
        作品名 = request.form.get('作品名')
        introduction = request.form.get('introduction')
        url = request.form.get('url')
        my_url = request.form.get('my_url')
        #サンプル動画 = request.form.get('サンプル動画')
        記事1 = request.form.get('記事1')
        記事2 = request.form.get('記事2')
        サムネイル1 = request.form.get('サムネイル1')
        #サムネイル2 = request.form.get('サムネイル2')
        md_file_name = request.form.get('md_file_name')
        使用回数 = request.form.get('使用回数')
        """

        コメント = []
        try:
            コメント.append(request.form.get('コメント0'))
            コメント.append(request.form.get('コメント1'))
            コメント.append(request.form.get('コメント2'))
            コメント.append(request.form.get('コメント3'))
            コメント.append(request.form.get('コメント4'))
            コメント.append(request.form.get('コメント5'))
            コメント.append(request.form.get('コメント6'))
            コメント.append(request.form.get('コメント7'))
            コメント.append(request.form.get('コメント8'))
            コメント.append(request.form.get('コメント9'))
            コメント.append(request.form.get('コメント10'))
            コメント.append(request.form.get('コメント11'))
            コメント.append(request.form.get('コメント12'))
            コメント.append(request.form.get('コメント13'))
            コメント.append(request.form.get('コメント14'))
            コメント.append(request.form.get('コメント15'))
            コメント.append(request.form.get('コメント16'))
            コメント.append(request.form.get('コメント17'))
            コメント.append(request.form.get('コメント18'))
            コメント.append(request.form.get('コメント19'))
            コメント.append(request.form.get('コメント20'))
            コメント.append(request.form.get('コメント21'))
            コメント.append(request.form.get('コメント22'))
            コメント.append(request.form.get('コメント23'))
            コメント.append(request.form.get('コメント24'))
            コメント.append(request.form.get('コメント25'))
            コメント.append(request.form.get('コメント26'))
            コメント.append(request.form.get('コメント27'))
            コメント.append(request.form.get('コメント28'))
            コメント.append(request.form.get('コメント29'))
            コメント.append(request.form.get('コメント30'))
            コメント.append(request.form.get('コメント31'))
            コメント.append(request.form.get('コメント32'))
            コメント.append(request.form.get('コメント33'))
            コメント.append(request.form.get('コメント34'))
            コメント.append(request.form.get('コメント35'))
            コメント.append(request.form.get('コメント36'))
            コメント.append(request.form.get('コメント37'))
            コメント.append(request.form.get('コメント38'))
            コメント.append(request.form.get('コメント39'))
            コメント.append(request.form.get('コメント40'))
            コメント.append(request.form.get('コメント41'))
            コメント.append(request.form.get('コメント42'))
            コメント.append(request.form.get('コメント43'))
            コメント.append(request.form.get('コメント44'))
            コメント.append(request.form.get('コメント45'))
            コメント.append(request.form.get('コメント46'))
            コメント.append(request.form.get('コメント47'))
            コメント.append(request.form.get('コメント48'))
            コメント.append(request.form.get('コメント49'))
            コメント.append(request.form.get('コメント50'))
            コメント.append(request.form.get('コメント51'))
            コメント.append(request.form.get('コメント52'))
            コメント.append(request.form.get('コメント53'))
            コメント.append(request.form.get('コメント54'))
            コメント.append(request.form.get('コメント55'))
            コメント.append(request.form.get('コメント56'))
            print(コメント)
        except:
            print("コメント終了")


        #print(sam)
        コメント2 = []
        s = 0
        for i in コメント:  # samの整理
            #print(i)
            #try:
            if i == None:
                print("NOneキター")
                # コメント.append("")
                break
            elif i == "":
                コメント2.append("")
                print("コメントなしキター")
            else:
                コメント2.append(i)
            #except:
                # コメント.append("")
            #print(i)
            
            print("=================")
            print("コメント")
            print(コメント)
            print("コメント2")
            print(コメント2)
            print("sam")
            #print(sam)
            print("i")
            print(i)
            print("s")
            print(s)
            s = s + 1
        print(コメント2)
        #print(sam)
        #print(code)
        with open('./temp/コメント.txt', 'w', encoding='UTF-8') as f:
            f.write("\n".join(コメント2))
        
        with open('./temp/code.txt', 'r', encoding='UTF-8') as f:
            code = f.read()
        
        urls = []
        with open('./temp/url.txt', 'r', encoding='UTF-8') as f:
            urls.append(f.read().split("\n"))
        
        print("==========")
        print(code)
        urls = urls[0]
        print(urls)
        
        s = 0
        for url in urls:
            print(url)
            session = Session(engine)
            if session.query(Affiliate_Video_Pic).filter(affiliate_video_pic.code == str(code), affiliate_video_pic.url == url).first() == None:
                print("insert")
                print(s)
                pic = Affiliate_Video_Pic()
                pic.code=code
                pic.pic_count=s
                pic.url=url
                pic.comment=コメント[s]
                pic.created_date=datetime.datetime.now()
                pic.published_date=datetime.datetime.now()
                session.add(pic)
                session.commit()
                s = s + 1
                
                """
                session.add(self.affiliate_video_pic(self.affiliate_video_pic.code==code),
                                            pic_count=s,
                                            url=url,
                                            comment=コメント[s],
                                            created_date=datetime.datetime.now(),
                                            published_date=datetime.datetime.now(),
                                            )
                                            """

                

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
    
            #session = Session(engine)
            elif session.query(Affiliate_Video_Pic).filter(affiliate_video_pic.code == str(code), affiliate_video_pic.url == url).first() != None:
                print("update")
                # update
                #if session.query(self.affiliate_video_pic).filter(self.affiliate_video_pic.code == str(code), self.affiliate_video_pic.url == i).first() != None:
                pic = session.query(Affiliate_Video_Pic).filter(affiliate_video_pic.code == code, affiliate_video_pic.url == url).all()
                print(pic)
                for pi in pic:
                    if pi.comment == "":
                        pi.comment = コメント[s]
                        pi.published_date = datetime.datetime.now()
            s = s + 1
                        
                    
        #with open('./temp/code.txt', 'r', encoding='UTF-8') as f:
        #    code = f.read()
        #    code = code
        #    print(code)
        #session = Session(engine)
        #videos = session.query(self.affiliate_video).filter(Affiliate_Video.code == str(code), Affiliate_Video.affiliate_site == 1, Affiliate_Video.affiliate_genre == 0).first()
        #print(videos)
        #for video in videos:
        #    video.published_date = datetime.datetime.now()
        #    session.commit()
        subprocess.run("ruby ./V6_database.rb", shell=True, text=True)

                    
    return render_template("Editer.html",
                               )
    """


def insert_db_mgs(seed1):
    affiliate_video = Base.classes.Affiliate_Video_affiliate_video
    session = Session(engine)
    mgs = Analysis_MGS(seed1)
    session.add(affiliate_video(code=mgs.code,
                                seed_yes=True,
                                seed_error=0,
                                analysis_completed=False,
                                release_yes=False,
                                affiliate_site=1,
                                number_of_uses=0,
                                affiliate_genre=1,
                                created_date=datetime.datetime.now(),
                                published_date=datetime.datetime.now(),
                                title=mgs.title,
                                file_path=f"./www/MGS/{mgs.code}/seed1.txt",
                                url=f"https://www.mgstage.com/product/product_detail/{mgs.code}/",
                                actress=mgs.actress,
                                introduction=mgs.introduction,
                                my_url=f"https://www.mgstage.com/product/product_detail/{mgs.code}/" +
                                    "?aff=C7EL5ZIM2LIYL36AOUMDGYKNTJ",
                                article1="",
                                article2="",
                                thumbnail1=mgs.thumbnail1,
                                md_file_name=f"./Video/{mgs.code}.html",
                                bittorrent="",
                                reference=0,
                                seed1=seed1,
                                # seed2=seed2,
                                ))
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


def update_db_mgs(seed1):
    affiliate_video = Base.classes.Affiliate_Video_affiliate_video
    session = Session(engine)
    mgs = Analysis_MGS(seed1)
    video = session.query(affiliate_video).filter(
        affiliate_video.code == str(mgs.code)).first()

    seed_yes = True,
    # seed_error=0,
    analysis_completed = True,
    release_yes = True,
    affiliate_site = 1,
    number_of_uses = 0,
    affiliate_genre = 1,

    if video.code == "" or video.code == None:
        video.code = request.form.get('code')
    if video.title == "":
        video.title = request.form.get('作品名')
    if video.url == "":
        video.url = f"https://www.mgstage.com/product/product_detail/{mgs.code}/"
    if video.actress == "":
        video.actress = request.form.get('女優')
    if video.introduction == "":
        video.introduction = request.form.get('introduction')
    if video.my_url == "":
        video.my_url = video.url + "?aff=C7EL5ZIM2LIYL36AOUMDGYKNTJ"
    if video.article1 == "":
        video.article1 = request.form.get('記事1')
    if video.article2 == "":
        video.article2 = request.form.get('記事2')
    if video.thumbnail1 == "":
        video.thumbnail1 = request.form.get('サムネイル1')
    # if thumbnail2 == "":
    #    thumbnail2 = mgs.thumbnail2[random.random(len(mgs.thumbnail2))]
    if video.md_file_name == "":
        video.md_file_name = f"./Video/{mgs.code}.html"
    if video.bittorrent == "":
        video.bittorrent = ""
    if video.seed1 == "":
        video.seed1 = request.form.get('seed1')
    if video.seed2 == "":
        video.seed2 = request.form.get('seed2')

    video.published_date = datetime.datetime.now()

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


def update_db_time(seed1):
    affiliate_video = Base.classes.Affiliate_Video_affiliate_video
    session = Session(engine)
    mgs = Analysis_MGS(seed1)
    video = session.query(affiliate_video).filter(
        affiliate_video.code == str(mgs.code)).first()

    video.published_date = datetime.datetime.now()

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
"""

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80, threaded=True)
