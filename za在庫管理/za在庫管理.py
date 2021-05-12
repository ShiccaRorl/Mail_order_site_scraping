# -*- coding:utf-8 -*-

import os
import glob

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


def run():
    file_path=[]
    file_path = (glob.glob(f'{ROOT_PATH}/**/*.txt', recursive=True))
    print(file_path)


if __name__ == '__main__':
    #recursive_file_check(ROOT_PATH)
    run()