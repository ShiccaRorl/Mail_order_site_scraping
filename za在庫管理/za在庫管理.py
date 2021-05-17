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
#ROOT_PATH = '//vmware-host/Shared Folders/D/共有/Down'
#print(ROOT_PATH)

# Excel path
excel_path = "C:/Users/user/Downloads/バックアップ/プログラム/バックアップ/保存/2020年9月在庫表.xlsx"


def file_run(file_path):
    # 処理を記述
    print(file_path)
    

def recursive_file_check(path):
    if os.path.isdir(path):
        # directoryだったら中のファイルに対して再帰的にこの関数を実行
        files = os.listdir(path)
        for file in files:
            recursive_file_check(path + "\\" + file)
    else:
        # fileだったら処理
        file_run(path)


def get_商品コード(source):
    file = re.split("\n", source)[0]
    
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

def get_excel_db():
    wb = load_workbook(excel_path)
    ws = wb["マスター"]
    
    s = 5
    for i in ws.max_row():
        session = Session(engine)
        if session.query(Product).filter(Product.code == ws[f"B{s}"]).first() == None:
            print(f"insert {s :} {i}")
            session.add(Product(code = ws[f"B{s}"],
                            商品名 = ws[f"C{s}"],
                            下代 = ws[f"E{s}"],
                            update_at = datetime.datetime.now(),
                            ))
            session.commit()
            s = s + 1
            time.sleep(1)
        else:
            print(f"update {s :} {i}")
            session = Session(engine)
            product = session.query(Product).filter(Product.code == ws[f"B{s}"]).first()
            product.code = ws[f"B{s}"]
            product.商品名 = ws[f"C{s}"]
            product.下代 = ws[f"E{s}"]
            product.update_at = datetime.datetime.now()
            
            session.commit()
            s = s + 1
            time.sleep(1)
        #save(session)


def 再登録日(code):
    session = Session(engine)
    商品名 = session.query(Product).filter(Product.code == code).first()
    商品名2 = session.query(dir_db).filter(dir_db.code == code).first()
    session.add(再登録日(code = code,
                            商品名 = 商品名.商品名,
                            商品名2 = 商品名2.商品名,
                            update_at = datetime.datetime.now(),
                            ))
    session.commit()


def get_金額(source):
    data = ""
    for i in re.split("\n", source):
        m = re.match(r'(\\.*?)', i)
        if m != None:
            data = m.group().replace(",", "")
            data = data.replace("\\", "")
            print(f"金額 : {data}")
            return data
    return data
            

def get_directory_db():
    # ディレクトリDBで思考
    file_path=[]
    file_path = (glob.glob(f'{ROOT_PATH}/**/*.txt', recursive=True))
    for file in file_path:
        source = load(file)
        directory_db(file, source)
        
def get_db_source_db():
    session = Session(engine)
    sources = session.query(dir_db).all()
    for db in sources:
        directory_db(db.dir, db.source)


def directory_db(file, source):
        session = Session(engine)
        状態 = ""
        if "在庫1" in file:
            print(f"在庫1 : {file}")
            状態 = "在庫1"
        elif "在庫0" in file:
            print(f"在庫0 : {file}")
            状態 = "在庫0"
        else:
            print(f"在庫あり : {file}")
            状態 = "在庫あり"
            #print(get_商品コード(file))

        
        商品名 = re.split("\n", source)[0]
        code = get_商品コード(source)
        dir = file
        金額 = get_金額(source)
        source = source
        
        if session.query(dir_db).filter(dir_db.商品名 == 商品名).first() == None:
            print("insert")
            session.add(dir_db(商品名 = 商品名,
                                    code = code,
                                    update_at = datetime.datetime.now(),
                                    dir = dir,
                                    状態 = 状態,
                                    金額 = 金額,
                                    source = source,
                                    ))
            session.commit()
            #save(session)
        else:
            print("update")
            seed = session.query(dir_db).filter(dir_db.商品名 == 商品名).first()

            seed.code = code
            seed.update_at=datetime.datetime.now()
            seed.dir = dir
            seed.状態 = 状態
            seed.金額 = 金額
        
            session.commit()
            #save(session)
  
   


def save(session):
    i = 0
    while i <= 5:
        try:
            time.sleep(1)
            session.commit()
            time.sleep(1)
            i = i + 1
        except:
            print("失敗")

def load(dir):
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

def open_folder(path):
    """
    引数のpathを、エクスプローラーで開く
    :param path: エクスプローラーで開きたいフォルダパス
    :type path: unicode
    """
    # 開くときは cp932のstrにして実行する
    subprocess.Popen(['explorer', path.encode("cp932").replace("/", "\\")])

def all_delete():
    session = Session(engine)
    session.query(dir_db).delete()
    session.commit()

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
    
    args = sys.argv
    if args[1] == "clear":
        all_delete()
    elif args[1] == "directory_db":
        get_directory_db()
    elif args[1] == "db_source_db":
        get_db_source_db()
    elif args[1] == "get_excel_db":
        get_excel_db()
    else:
        print("オプションが違います。")
    #all_delete() # 全部消す
    #get_directory_db() # ディレクトリで登録する
    #get_db_source_db() # データベースで登録する
    #get_excel_db() # エクセルからデータを抜く