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

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from openpyxl import load_workbook, Workbook

Base = automap_base()

# Excel path
excel_path = ""

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

print('//DESKTOP-FK98SN0/Users/Public/Documents/吉本さんPCから移動したファイル/メルカリラクマ出品画像/メルカリ')

#ROOT_PATH = '//DESKTOP-FK98SN0/Users/Public/Documents/吉本さんPCから移動したファイル/メルカリラクマ出品画像/メルカリ'#.encode("cp932").replace("/", "\\")
ROOT_PATH = '//DESKTOP-FK98SN0/Users/Public/Documents/吉本さんPCから移動したファイル/メルカリラクマ出品画像/メルカリ'
ROOT_PATH = '//vmware-host/Shared Folders/D/共有/Down'
print(ROOT_PATH)



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

def get_商品コード(file):
    session = Session(engine)
    code = re.split("\\s", file)
    code = code[len(code)-1]
    # ここで商品データベースにSelectして存在したら、それを返す
    data = session.query(Product).filter(code == code).first()
    if data != None:
        return data
    
    code = file.split(")")
    code = code[len(code)-1]
    # ここで商品データベースにSelectして存在したら、それを返す
    data = session.query(Product).filter(code == code).first()
    if data != None:
        return data

    
    # ディレクトリの最後が商品コードの場合
    code = file.split("/")
    code = code[len(code)-1]
    # ここで商品データベースにSelectして存在したら、それを返す
    data = session.query(Product).filter(code == code).first()
    if data != None:
        return data

    return ""
    # ファイルを開いて商品コードらしい文字列があったら、商品データベースにSelectして存在したら、それを返す


    # それでもだめなら、商品データベースから文字列に存在するかチェックする
    
    # ファイルを開いて商品データベースから文字列に存在するかチェックする
    
    
    # それ以外はエラーで、人力でどうにかする

def get_excel_db():
    wb = load_workbook(excel_path)
    ws = wb["data"]
    
    s = 0
    for i in ws.max_row():
        session = Session(engine)
        session.add(Product(code = ws[f"A{s}"],
                            商品名 = ws[f"B{s}"],
                            ))
        save(session)
    

def get_金額():
    return 0

def get_directory_db():
    # ディレクトリDBで思考
    file_path=[]
    file_path = (glob.glob(f'{ROOT_PATH}/**/*.txt', recursive=True))
    #print(file_path)

    for file in file_path:
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

        source = load(file)
        商品名 = re.split("\n", source)[0]
        商品コード = get_商品コード()
        dir = file
        金額 = get_金額()
        source = source
        session.add(dir_db(商品名 = 商品名,
                                    商品コード = 商品コード,
                                    update_at=datetime.datetime.now(),
                                    dir = dir,
                                    状態 = 状態,
                                    金額 = 金額,
                                    source = source,
                                    ))
        save(session)


def save(session):
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
            
def load(dir):
    try:
        with open(dir, 'r', encoding="utf-8") as f:
            seed1 = f.read()
    except:
        with open(dir, 'r', encoding="cp932") as f:
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



if __name__ == '__main__':
    #recursive_file_check(ROOT_PATH)
    get_directory_db()
    # get_excel_db()