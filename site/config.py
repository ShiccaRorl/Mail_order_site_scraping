# -*- coding:utf-8 -*-

class Config():
    def __init__(self):
        # DB
        self.db_path = "sqlite:///./../../db.sqlite3"
        
        self.excel_db_path = "./../../売上.xlsx"
        # download
        self.download_path = "C:/Users/ban/Downloads/"
        #self.download_path = "C:/Users/user/Downloads"

        # ヤフオクのページ設定
        self.yahoo_auction_page = 50