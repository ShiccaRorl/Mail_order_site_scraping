# -*- coding:utf-8 -*-


from V6_analysis_MGS import Analysis_MGS
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
engine = create_engine("sqlite:///db.sqlite3")

# reflect the tables
Base.prepare(engine, reflect=True)

# mapped classes are now created with names by default
# matching that of the table name.
affiliate_video = Base.classes.Affiliate_Video_affiliate_video
affiliate_video_pic = Base.classes.Affiliate_Video_affiliate_video_pic

session = Session(engine)


class Directory_seed1():
    def __init__(self):
        self.affiliate_video = Base.classes.Affiliate_Video_affiliate_video
        self.affiliate_video_pic = Base.classes.Affiliate_Video_affiliate_video_pic

    def get_dir_list(self):
        self.file_list = []
        for dir in glob.glob('C:\\Users\\ban\\Downloads\\MGS*.html'):
            #print(dir)
            with open(dir, 'r', encoding="utf-8") as f:
                self.seed1 = f.read()
            self.seed1 = self.seed1.replace("\n", "")
            self.seed1 = self.seed1.replace("\r", "")
            
            dmm = Analysis_MGS(self.seed1)
            
            self.file_list.append(dmm.code)
            self.削除する(dir)
            self.データベースに保存する通常(dmm.code, self.seed1)

    def データベースに保存する通常(self, code2, seed1):
        self.seed1 = seed1
        # if self.flag_データベースにinsert必要 == True:
        #print(code2)
        session = Session(engine)
        # print(session.query(self.affiliate_video).filter(
        #    self.affiliate_video.code == str(code2)).first()) #.order_by(self.affiliate_video.published_date))
        dmm = Analysis_MGS(self.seed1)
        # .order_by(self.affiliate_video.published_date):
        if (session.query(self.affiliate_video).filter(self.affiliate_video.code == str(code2)).first()) == None:
            session.add(self.affiliate_video(code=dmm.code,
                                             seed_yes=True,
                                             seed_error=0,
                                             analysis_completed=False,
                                             release_yes=False,
                                             affiliate_site=1,
                                             number_of_uses=0,
                                             affiliate_genre=1,
                                             created_date=datetime.datetime.now(),
                                             published_date=datetime.datetime.now(),
                                             title=dmm.title,
                                             file_path="",
                                             url=dmm.url,
                                             actress=dmm.actress,
                                             introduction=dmm.introduction,
                                             my_url=dmm.my_url,
                                             article1="",
                                             article2="",
                                             thumbnail1=dmm.thumbnail1,
                                             md_file_name=dmm.md_file_name,
                                             bittorrent="",
                                             reference=0,
                                             seed1=seed1,
                                             #seed2="",
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

        # update
        elif (session.query(self.affiliate_video).filter(self.affiliate_video.code == str(code2)).first()) != None:
            video = session.query(self.affiliate_video).filter(
                self.affiliate_video.code == str(code2)).first()
            """
            video.file_path = f"./www/MGS/{code2}/seed1.txt"
            print(video.file_path)
            try:
                with open(video.file_path, 'r',  encoding="utf-8") as f:
                    data1 = f.read()
                self.seed1 = data1
            except:
                self.seed1 = ""
                self.seed2 = ""
            """
            
            # 記事関係です
            try:
                with open(f"./www/MGS/{code2}/記事1.txt") as f:
                    self.article1 = f.read()
            except:
                self.article1 = ""
                
            try:
                with open(f"./www/MGS/{code2}/記事2.txt") as f:
                    self.article2 = f.read()
            except:
                self.article2 = ""
                
                """
                thumbnail2 = []
                mgs = Analysis_MGS(self.seed1)
                if video.title == "":
                    video.title = mgs.title
                if video.url == "":
                    video.url = f"https://www.mgstage.com/product/product_detail/{code2}/"
                if video.actress == "":
                    video.actress = mgs.actress
                if video.introduction == "":
                    video.introduction = mgs.introduction
                if video.my_url == "":
                    video.my_url = video.url + "?aff=C7EL5ZIM2LIYL36AOUMDGYKNTJ"
                if video.article1 == "":
                    video.article1 = self.article1
                if video.article2 == "":
                    video.article2 = self.article2
                if video.thumbnail1 == "":
                    video.thumbnail1 = mgs.thumbnail1
                #if thumbnail2 == "":
                #    thumbnail2 = mgs.thumbnail2[random.randint(0, len(mgs.thumbnail2))]
                if video.md_file_name == "":
                    video.md_file_name = f"./Video/{code2}.html"
                if video.bittorrent == "":
                    video.bittorrent = ""
                if video.seed1 == "":
                    video.seed1 = self.seed1
                #if video.seed2 == "":
                    #video.seed2 = self.seed2
                """
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
                        
        self.データベースに保存するサムネイル2(code2, self.seed1)

    def データベースに保存するサムネイル2(self, code2, seed1):
        self.seed1 = seed1
        """
        file_path = f"./www/MGS/{code2}/seed1.txt"
        print(file_path)
        seed1 = ""
        try:
            with open(file_path, 'r',  encoding="utf-8") as f:
                seed1 = f.read()
        except:
            seed1 = ""
            seed2 = ""        
        try:
            with open(f"./www/MGS/{code2}/コメント.txt", 'r',  encoding="utf-8") as f:
                comment = f.read()
                self.comment = comment.split('\n')
        except:
            comment = []
        """

        dmm = Analysis_MGS(self.seed1)
        thumbnail2 = []

        # サムネイル2読み込み
        session = Session(engine)
        s = 0
        for url in dmm.thumbnail2:
            if (session.query(self.affiliate_video_pic).filter(self.affiliate_video_pic.code == str(code2), self.affiliate_video_pic.url == url).first()) == None:
                #try:
                #    if self.comment[s] == None:
                #        self.comment.append("")
                #except:
                #    self.comment.append("")
                session.add(self.affiliate_video_pic(code=dmm.code,
                                                     pic_count=s,
                                                     url=url,
                                                     #comment=self.comment[s],
                                                     created_date=datetime.datetime.now(),
                                                     published_date=datetime.datetime.now(),
                                                     ))
                s = s + 1
                
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

    # コメントの取り込み

        """
        try:
            self.comments = []
            comment_path = f"./www/MGS/{code2}/コメント.txt"
            with open(comment_path, 'r',  encoding="utf-8") as f:
                self.comments = f.read().split("\n")
        except:
            print("commentファイル無し")
            self.comments = []

        session = Session(engine)
        try:
            for comment in self.comments:
                # update
                if (session.query(self.affiliate_video_pic).filter(self.affiliate_video_pic.code == str(code2) and self.affiliate_video_pic.url == url).first()) != None:
                    pic = session.query(self.affiliate_video_pic).filter(
                        self.affiliate_video_pic.code == str(code2) and self.affiliate_video_pic.url == url).first()
                    if pic.comment == "":
                        pic.comment = comment

                        pic.published_date = datetime.datetime.now()
                        
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
                                
        except:
            print("コメント取り込み失敗")
        """
        
    def データベースに保存するその他ID(self, code2):
        file_path = f"./www/MGS/{code2}/seed1.txt"
        #print(file_path)
        try:
            with open(file_path, 'r',  encoding="utf-8") as f:
                data1 = f.read()
            data2 = ""
        except:
            data1 = ""
            data2 = ""

        thumbnail2 = []
        mgs = Analysis_MGS(data1)

        # その他のページ読み込み
        session = Session(engine)
        for url in mgs.他のid:
            if (session.query(self.affiliate_video).filter(self.affiliate_video.code == str(code2)).first()) == None:
                session.add(self.affiliate_video(code=code2,
                                                 seed_yes=False,
                                                 seed_error=0,
                                                 analysis_completed=False,
                                                 release_yes=False,
                                                 affiliate_site=1,
                                                 number_of_uses=0,
                                                 affiliate_genre=1,
                                                 created_date=datetime.datetime.now(),
                                                 published_date=datetime.datetime.now(),
                                                 title="",
                                                 file_path="",
                                                 url=f"https://www.mgstage.com/product/product_detail/{code2}/",
                                                 actress="",
                                                 introduction="",
                                                 my_url=url + "?aff=C7EL5ZIM2LIYL36AOUMDGYKNTJ",
                                                 article1="",
                                                 article2="",
                                                 thumbnail1="",
                                                 md_file_name=f"./Video/{code2}.html",
                                                 bittorrent="",
                                                 reference = 0,
                                                 seed1="",
                                                 seed2="",
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
            else:
                """
                reference = session.query(self.affiliate_video).filter(self.affiliate_video.code == str(code2)).first()
                print(reference)
                print(reference.reference)
                reference.reference = reference.reference + 1
                print(code2)
                """
                #print("人気度")
                """
                print(reference)
                
                time.sleep(1)
                #session.commit()
                time.sleep(1)
                """
                
    # 計算で取り出すデータ
    def データベースに保存する計算する(self, code2):
        session = Session(engine)
        video = session.query(self.affiliate_video).filter(
            self.affiliate_video.code == str(code2)).first()
        file_path = f"./www/MGS/{code2}/seed1.txt"
        #print(file_path)
        try:
            with open(file_path, 'r',  encoding="utf-8") as f:
                self.seed1 = f.read()

        except:
            self.seed1 = ""
            self.seed2 = ""

        mgs = Analysis_MGS(self.seed1)
        session = Session(engine)
        
        try:
            # update
            #mgs = Analysis_MGS(self.seed1)
            if video.title == "":
                video.title = mgs.title
            if video.url == "":
                video.url = f"https://www.mgstage.com/product/product_detail/{code2}/"
            if video.actress == "":
                video.actress = mgs.actress
            if video.introduction == "":
                video.introduction = mgs.introduction
            if video.my_url == "":
                video.my_url = video.url + "?aff=C7EL5ZIM2LIYL36AOUMDGYKNTJ"
            if video.article1 == "":
                video.article1 = ""
            if video.article2 == "":
                video.article2 = ""
            if video.thumbnail1 == "":
                video.thumbnail1 = mgs.thumbnail1
            #if video.thumbnail2 == "":
            #    thumbnail2 = mgs.thumbnail2
            if video.md_file_name == "":
                video.md_file_name = f"./Video/{code2}.html"
            if video.bittorrent == "":
                video.bittorrent = ""
            if video.seed1 == "":
                video.seed1 = seed1
            if video.seed2 == "":
                video.seed2 = seed2

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
        except:
            print("計算で取り出すデータ失敗")

        # if self.flag_データベースにupdate必要 == True:

    def アップデータ可能か調べる(self, code):
        session = Session(engine)
        videos = session.query(self.affiliate_video).filter(
            self.affiliate_video.code == str(code)).all()
        file_path = f"./www/MGS/{code}/seed1.txt"
        #print(file_path)
        try:
            with open(file_path, 'r',  encoding="utf-8") as f:
                self.seed1 = f.read()

        except:
            self.seed1 = ""
            self.seed2 = ""

        mgs = Analysis_MGS(self.seed1)
        session = Session(engine)
        
        try:
            for video in videos:
                # update
                i = 0
                mgs = Analysis_MGS(self.seed1)
                if video.title == "":
                    video.title = mgs.title
                    i = 1
                if video.url == "":
                    video.url = f"https://www.mgstage.com/product/product_detail/{code}/"
                    i = 1
                if video.actress == "":
                    video.actress = mgs.actress
                    i = 1
                if video.introduction == "":
                    video.introduction = mgs.introduction
                    i = 1
                if video.my_url == "":
                    video.my_url = video.url + "?aff=C7EL5ZIM2LIYL36AOUMDGYKNTJ"
                    i = 1
                if video.article1 == "":
                    video.article1 = ""
                    i = 1
                if video.article2 == "":
                    video.article2 = ""
                if video.thumbnail1 == "":
                    video.thumbnail1 = mgs.thumbnail1
                    i = 1
                #if video.thumbnail2 == "":
                #    thumbnail2 = mgs.thumbnail2
                if video.md_file_name == "":
                    video.md_file_name = f"./Video/{code}.html"
                    i = 1
                if video.bittorrent == "":
                    video.bittorrent = ""
                if video.seed1 == "":
                    video.seed1 = self.seed1
                #if video.seed2 == "":
                    #video.seed2 = self.seed2

                if i == 0: # 解析が終了した印を入れる
                    video.analysis_completed = 1
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
        except:
            print("コメント取り込み失敗")


    def 削除する(self, code):
        print(f"{code} MGS 削除します")
        os.remove(code)

    def main(self):
        self.get_dir_list()

        for code in self.file_list:
            #print(code)
            #self.データベースに保存する通常(code)
            #self.データベースに保存するサムネイル2(code)
            #self.データベースに保存するコメント(code)
            self.データベースに保存するその他ID(code)
            self.データベースに保存する計算する(code)
            self.アップデータ可能か調べる(code)
            self.削除する(code)
            time.sleep(1)


if __name__ == '__main__':
    directory_seed1 = Directory_seed1()
    directory_seed1.main()
