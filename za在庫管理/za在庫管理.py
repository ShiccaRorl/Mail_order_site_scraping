# -*- coding:utf-8 -*-

# python -m pip install --upgrade pip
# pip install -U sqlalchemy
# pip install -U flake8
# pip install -U autopep8

# pip install -U openpyxl
# pip install -U beautifulsoup4
# pip install -U requests
# pip install -U pyinstaller

# pyinstaller kabu.py --onefile

import os
import glob
import re
import datetime
import time
import subprocess
import argparse
import sys
import logging

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from openpyxl import load_workbook, Workbook

Base = automap_base()

# engine, suppose it has two tables 'user' and 'address' set up
#db_path = "sqlite:///./../../db.sqlite3"
db_path = "sqlite:///./db.sqlite3"
engine = create_engine(db_path)
# 個人情報の塊なのでGITの外に設置

# reflect the tables
Base.prepare(engine, reflect=True)

# mapped classes are now created with names by default
# matching that of the table name.

#seeds = Base.classes.seeds
dir_db = Base.classes.dir_db
Product = Base.classes.Product

#print('//DESKTOP-FK98SN0/Users/Public/Documents/吉本さんPCから移動したファイル/メルカリラクマ出品画像/メルカリ')

#ROOT_PATH = '//DESKTOP-FK98SN0/Users/Public/Documents/吉本さんPCから移動したファイル/メルカリラクマ出品画像/メルカリ'#.encode("cp932").replace("/", "\\")
ROOT_PATH = '//DESKTOP-FK98SN0/Users/Public/Documents/吉本さんPCから移動したファイル/メルカリラクマ出品画像/メルカリ'
#ROOT_PATH = 'C:/Users/user/Downloads/バックアップ/プログラム/バックアップ/保存/メルカリ'
#print(ROOT_PATH)

# Excel path
excel_path1 = "C:/Users/user/Downloads/バックアップ/プログラム/バックアップ/保存/2020年9月在庫表.xlsx"
excel_path2 = "./2020年9月在庫表.xlsx"

formatter = '%(asctime)s:%(message)s'
logging.basicConfig(filename='test.log', level=logging.DEBUG, format=formatter)




class Database_Analysis():
    # データベース解析
    def set_source(self, source):
        self.source = source
        #formatter = '%(asctime)s:%(message)s'
        #self.logging.basicConfig(filename='test.log', level=logging.DEBUG, format=formatter)

    def get_name(self):
        return re.split("\n", self.source)[0]

    def get_金額(self, source):
        data = ""
        for i in re.split("\n", self.source):
            m = re.match(r'￥(.*?)', i)
            if m != None:
                try:
                    data = m.group().replace(",", "")
                    data = data.replace("￥", "")
                    print(f"金額 : {data}")
                    return int(data)
                except:
                    return 0
            m = re.match(r'\\(.*?)', i)
            if m != None:
                try:
                    data = m.group().replace(",", "")
                    data = data.replace("\\", "")
                    print(f"金額 : {data}")
                    return int(data)
                except:
                    return 0
            #self.logger.error(self.get_name() + ' 金額のエラー')


    def get_商品コード(self, source):
        self.source = source
        
        
        file = re.split("\n", self.source)[0]
    
        session = Session(engine)
    
        code = re.split("\\s", file)
        code = code[len(code)-1]
        # ここで商品データベースにSelectして存在したら、それを返す
        data = session.query(Product).filter(Product.code == code).first()
        if data != None:
            return data
    
        code = file.split(")")
        code = code[len(code)-1]
        # ここで商品データベースにSelectして存在したら、それを返す
        data = session.query(Product).filter(Product.code == code).first()
        if data != None:
            return data
    
        # ディレクトリの最後が商品コードの場合
        code = file.split("/")
        code = code[len(code)-1]
        # ここで商品データベースにSelectして存在したら、それを返す
        data = session.query(Product).filter(Product.code == code).first()
        if data != None:
            return data

        return ""
        # ファイルを開いて商品コードらしい文字列があったら、商品データベースにSelectして存在したら、それを返す


        # それでもだめなら、商品データベースから文字列に存在するかチェックする
    
        # ファイルを開いて商品データベースから文字列に存在するかチェックする
    
    
        # それ以外はエラーで、人力でどうにかする




class Database_Registratio(Database_Analysis):
    # データベース登録           
    def 再登録日(self, code):
        session = Session(engine)
        商品名 = session.query(Product).filter(Product.code == code).first()
        商品名2 = session.query(dir_db).filter(dir_db.code == code).first()
        session.add(再登録日(code = code,
                            商品名 = 商品名.商品名,
                            商品名2 = 商品名2.商品名,
                            update_at = datetime.datetime.now(),
                            ))
        session.commit()



    def get_directory_db(self):
        # ディレクトリDBで思考
        file_path=[]
        file_path = (glob.glob(f'{ROOT_PATH}/**/*.txt', recursive=True))
        for file in file_path:
            source = load(file)
            self.directory_db(file, source)
        
    def get_db_source_db(self):
        # dbで思考する
        session = Session(engine)
        sources = session.query(dir_db).all()
        for db in sources:
            self.directory_db(db.dir, db.source)


    def directory_db(self, file, source):
        session = Session(engine)
        状態 = ""
        if "在庫1" in file:
            print(f"在庫1 : {file}")
            self.状態 = "在庫1"
        elif "在庫0" in file:
            print(f"在庫0 : {file}")
            self.状態 = "在庫0"
        else:
            print(f"在庫あり : {file}")
            self.状態 = "在庫あり"
            #print(get_商品コード(file))

        
        self.商品名 = re.split("\n", source)[0]
        self.code = self.get_商品コード(source)
        self.dir = file
        self.金額 = self.get_金額(source)
        self.source = source
        
        if session.query(dir_db).filter(dir_db.商品名 == self.商品名).first() == None:
            print("insert")
            session.add(dir_db(商品名 = self.商品名,
                                    code = code,
                                    update_at = datetime.datetime.now(),
                                    dir = self.dir,
                                    r_状態 = self.状態,
                                    r_金額 = self.金額,
                                    source = self.source,
                                    ))
            session.commit()
            #self.save(session)
        else:
            print("update")
            seed = session.query(dir_db).filter(dir_db.商品名 == self.商品名).first()

            seed.code = self.code
            seed.update_at=datetime.datetime.now()
            seed.dir = self.dir
            seed.状態 = self.状態
            seed.金額 = self.金額
            print(self.code)
            print(self.金額)
            session.commit()
            #self.save(session)
  
            i = 0
            while i <= 5:
                try:
                    time.sleep(1)
                    session.commit()
                    time.sleep(1)
                    print(i)
                    i = i + 1
                except:
                    print("失敗")
   


    def save(self, session):
        i = 0
        while i <= 5:
            try:
                time.sleep(1)
                session.commit()
                time.sleep(1)
                print(i)
                i = i + 1
            except:
                print("失敗")

    def load(self, dir):
        try:
            with open(dir, 'r', encoding="utf-8") as f:
                seed1 = f.read()
        except:
            try:
                with open(dir, 'r', encoding="cp932") as f:
                    seed1 = f.read()
            except:
                with open(dir, 'r', encoding="utf-16") as f:
                    seed1 = f.read()
    
        return seed1

    def all_delete(self):
        session = Session(engine)
        session.query(dir_db).delete()
        session.commit()



def open_folder(path):
    """
    引数のpathを、エクスプローラーで開く
    :param path: エクスプローラーで開きたいフォルダパス
    :type path: unicode
    """
    # 開くときは cp932のstrにして実行する
    subprocess.Popen(['explorer', path.encode("cp932").replace("/", "\\")])



if __name__ == '__main__':
    #recursive_file_check(ROOT_PATH)
    """
    parser = argparse.ArgumentParser(description="なんちゃって在庫管理です")
    #parser.add_argument("a", help="実行")
    parser.add_argument("--directory_db", help="ディレクトリから登録")
    parser.add_argument("--db_source_db", help="データベースから登録")
    parser.add_argument("--get_excel_db", help="エクセルから登録")
    parser.add_argument("--clear", help="全部消しちゃう")
    args = parser.parse_args()
    print("arg1="+args.clear)
    print("arg2="+args.directory_db)
    print("arg3="+args.db_source_db)
    print("arg4="+args.get_excel_db)
    if args.clear == "--clear":
        all_delete()
    elif args.directory_db == "--directory_db":
        get_directory_db()
    elif args.db_source_db == "--db_source_db":
        get_db_source_db()
    elif args.get_excel_db == "--get_excel_db":
        get_excel_db()
    else:
        print("オプションが違います。")
    """
    

    database_registratio = Database_Registratio()



    args = sys.argv
    print(args)
    if args[1] == None:
        print("オプションが違います。")
        database_registratio.get_db_source_db()
            
        print("directory_db")
        print("db_source_db")
        print("")

    elif args[1] == "clear":
        database_registratio.all_delete()
    elif args[1] == "directory_db":
        database_registratio.get_directory_db()
    elif args[1] == "db_source_db":
        database_registratio.get_db_source_db()
    else:
        print("オプションが違います。")
        database_registratio.get_db_source_db()
            
        print("directory_db")
        print("db_source_db")
        print("")
        
        
    #all_delete() # 全部消す
    #get_directory_db() # ディレクトリで登録する
    #get_db_source_db() # データベースで登録する
    #get_excel_db() # エクセルからデータを抜く
    
    # https://fril.jp/item/
    # https://item.fril.jp/
    #※こちらは送料当店負担にてゆうパケット(追跡ナンバー付きゆうメール便)で発送させて頂きます。
    #当店発送の翌日より日本郵便ホームページでのお荷物追跡が可能です。


    #※こちらは送料当店負担にてかんたんラクマパック（日本郵便）で発送させて頂きます。 
    #匿名配送で配達状況が取引ページで確認できて安心です。
