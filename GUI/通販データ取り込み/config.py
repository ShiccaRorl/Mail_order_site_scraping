# -*- coding:utf-8 -*-

import configparser

# ファイルの存在チェック用モジュール
import os
import errno

class Config():
    def __init__(self):
        
        # --------------------------------------------------
        # read_file()関数によるiniファイルの読み込み
        # --------------------------------------------------
        config_ini = configparser.ConfigParser()
        config_ini_path = './config.ini'

        # iniファイルが存在するかチェック
        if os.path.exists(config_ini_path):
            # iniファイルが存在する場合、ファイルを読み込む
            with open(config_ini_path, encoding='utf-8') as fp:
                config_ini.read_file(fp)

                read_default = config_ini['DEFAULT']

                db_path1 = read_default.get('db_path1')
                db_path2 = read_default.get('db_path2')

                if os.path.exists(db_path1):
                    # iniの値取得
                    print(db_path1)
                    self.db_path = "sqlite:///" + db_path1
                elif os.path.exists(db_path2):
                    print(db_path2)
                    self.db_path = "sqlite:///" + db_path2
                else:
                    print("db_pathがない")


                read_default = config_ini['DEFAULT']
            
                excel_db_path1 = read_default.get('excel_db_path1')
                excel_db_path2 = read_default.get('excel_db_path2')

                if os.path.exists(excel_db_path1):
                    print(excel_db_path1)
                    # iniの値取得
                    self.excel_db_path = excel_db_path1
                elif os.path.exists(excel_db_path2):
                    print(excel_db_path2)
                    self.excel_db_path = excel_db_path2
                else:
                    print("excel_db_pathがない")


                read_default = config_ini['DEFAULT']
            
                download_path1 = read_default.get('download_path1')
                download_path2 = read_default.get('download_path2')

                if os.path.exists(download_path1):
                    # iniの値取得
                    print(download_path1)
                    self.download_path = download_path1
                elif os.path.exists(download_path2):
                    print(download_path2)
                    self.download_path = download_path2
                else:
                    print("download_pathがない")


                read_default = config_ini['DEFAULT']
            
                self.yahoo_auction_page = read_default.get('yahoo_auction_page')
                
        else:
            # iniファイルが存在しない場合、エラー発生
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), config_ini_path)
    
    def test(self):
        print(self.db_path + "を使います")
        print(self.excel_db_path + "を使います")
        print(self.download_path + "を使います")
    
if __name__ == '__main__':
    config = Config()
    print(config.db_path + "を使います")
    print(config.excel_db_path + "を使います")
    print(config.download_path + "を使います")