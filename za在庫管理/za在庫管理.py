# -*- coding:utf-8 -*-

import os
import glob
import re

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

Base = automap_base()

# engine, suppose it has two tables 'user' and 'address' set up
db_path = "sqlite:///./../../db.sqlite3"
engine = create_engine(db_path)
# 個人情報の塊なのでGITの外に設置

# reflect the tables
Base.prepare(engine, reflect=True)

# mapped classes are now created with names by default
# matching that of the table name.
seeds = Base.classes.seeds
site = Base.classes.site



ROOT_PATH = 'R:/D/共有'


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
    code = re.split("\\s", file)
    code = code[len(code)-1]
    # ここで商品データベースにSelectして存在したら、それを返す
    return code
    
    code = file.split(")")
    code = code[len(code)-1]
    # ここで商品データベースにSelectして存在したら、それを返す
    return code


    # ファイルを開いて商品コードらしい文字列があったら、商品データベースにSelectして存在したら、それを返す


    # それでもだめなら、商品データベースから文字列に存在するかチェックする
    
    # ファイルを開いて商品データベースから文字列に存在するかチェックする
    
    
    # それ以外はエラーで、人力でどうにかする

def run():
    # ディレクトリDBで思考
    file_path=[]
    file_path = (glob.glob(f'{ROOT_PATH}/**/*.txt', recursive=True))
    #print(file_path)
    for file in file_path:
        if "在庫1" in file:
            print(f"在庫1 : {file}")
        elif "在庫0" in file:
            print(f"在庫0 : {file}")
        else:
            print(f"在庫あり : {file}")
        print(get_商品コード(file))

if __name__ == '__main__':
    #recursive_file_check(ROOT_PATH)
    run()