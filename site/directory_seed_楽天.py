# -*- coding:utf-8 -*-

# 2021/04/25
# pip install -U sqlalchemy


from config import Config
from directory_seed import Mail_order_site

import datetime
import time
import os
import random
import re
import glob

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from bs4 import BeautifulSoup

Base = automap_base()

# engine, suppose it has two tables 'user' and 'address' set up
#engine = create_engine("sqlite:///db.sqlite3")

# reflect the tables
#Base.prepare(engine, reflect=True)

# mapped classes are now created with names by default
# matching that of the table name.

#session = Session(engine)


class Rakuten():
    def __init__(self):
        self.config = Config()
        Base = automap_base()
        # engine, suppose it has two tables 'user' and 'address' set up
        self.engine = create_engine(self.config.db_path)
        # 個人情報の塊なのでGITの外に設置

        # reflect the tables
        Base.prepare(self.engine, reflect=True)

        # mapped classes are now created with names by default
        # matching that of the table name.

        self.seeds = Base.classes.seeds
        self.site = Base.classes.site
        self.sale = Base.classes.sale




    def get_data(self):
        self.data = self.mail_order_site.get_data()
        return str(self.data.seed)

    def get_seed(self):
        self.data = self.get_data()
        return self.data.replace("charset=euc-jp", 'charset="UTF-8"')

    def test(self):
        with open("./../../mail_order_site2.html", 'w', encoding="utf-8") as f:
            f.write(str(self.get_seed()))


    def get_id(self):
<a href="/order-rb/individual-order-detail-sc/init?orderNumber=246369-20210426-00006744" class="rms-status-order-nr">246369-20210426-00006744</a>
        return

    def get_日付(self):
#order-details-1 > div > div.rms-content-order-details-blocks > div.rms-content-order-details-block-history-wrapper.col-sm-12.rms-clear-padding > div > div.rms-col-33-percent > div.rms-content-order-details-block-history-table-wrapper.rms-col-100-percent > table > tbody > tr:nth-child(3) > td:nth-child(2)

<table class="rms-content-order-details-block-history-table"> <tbody><tr> <td>受注番号
    <a href="javascript:void(window.open('https://help.rms.rakuten.co.jp/mw/?hid=989', 'popup', 'scrollbars=yes,resizable=yes,width=600,height=400,left=10,top=10'))" class="rms-icon-help rms-icon hover  dark">
    </a>
  </td> <td>246369-20210426-00006744</td> </tr> <tr> <td>申込番号</td> <td><a target="_blank" href="null?reserveNumber=null&amp;detailId=null"></a></td> </tr> <tr> <td>注文日時</td> <td>2021/04/26 14:48</td> </tr> <tr> <td>注文確認日時</td> <td>2021/04/26 14:49</td> </tr> <tr> <td>注文確定日時</td> <td>2021/04/26 15:21</td> </tr> <tr> <td>発送完了報告日</td> <td>2021/04/27</td> </tr> </tbody></table>


        return

    def get_商品コード(self):
<a target="_blank" href="https://item.rakuten.co.jp/wamall/10000343/" class="rms-span-open-in-new">【ゆうパケット(追跡ナンバー付きゆうメール便)配送ＯＫ】■花柄前板★ベルト無しタイプまえいた　帯板ベビーピンク★着物姿に必須アイテム【207】AWK004</a>




        return

    def get_商品名(self):
<a target="_blank" href="https://item.rakuten.co.jp/wamall/10000343/" class="rms-span-open-in-new">【ゆうパケット(追跡ナンバー付きゆうメール便)配送ＯＫ】■花柄前板★ベルト無しタイプまえいた　帯板ベビーピンク★着物姿に必須アイテム【207】AWK004</a>

         return

    def get_数量(self):
       <div class="rms-table-column-line"><span>1</span></div>
        return

    def get_注文者_名前(self):
<span class="fullname">阿部 和泉</span>

        return

    def get_注文者_ペンネーム(self):
        return

    def get_注文者_郵便番号(self):
        <span class="address">〒441-8123 愛知県豊橋市若松町字豊美379-15</span>
        return

    def get_注文者_住所(self):
<span class="address">〒441-8123 愛知県豊橋市若松町字豊美379-15</span>
        return

    def get_注文者_電話番号(self):
<span class="phone">090-2777-0376</span>
        return

    def get_注文者_メールアドレス(self):
<a target="template_select" href="/order-rb-mail/individual-mail-send-template-select-sc/init?orderNumber=246369-20210426-00006744" class="email">9820883ead5b8e3ef43d733780fa82c7s1@dm.fw.rakuten.ne.jp</a>
        return



    def get_送り先_名前(self):
<span class="fullname">阿部 和泉</span>
        return

    def get_送り先_ペンネーム(self):
        return

    def get_送り先_郵便番号(self):
<span class="address">〒441-8123 愛知県豊橋市若松町字豊美379-15</span>
        return

    def get_送り先_住所(self):
<span class="address">〒441-8123 愛知県豊橋市若松町字豊美379-15</span>
        return

    def get_送り先_電話番号(self):
<span class="phone">090-2777-0376</span>
        return

    def get_送り先_メールアドレス(self):

        return


購買額
<td class="text-right"><strong> <span class="footer-price">540円</span>  </strong></td>


    def main(self):
        self.mail_order_site = Mail_order_site()
        self.mail_order_site.siteID = 2
        self.get_data()
        self.soup = BeautifulSoup(self.get_seed(), "html.parser")
        self.test()
        
        i = 0
        tdss = TDss()
        while i <= 30:

            soup3 = self.soup.find('td', {'id': f'td3_{i}'})
            td3 = Td3(soup3)
            
            soup4 = self.soup.find('td', {'id': f'td4_{i}'})
            td4 = Td4(soup4)

            soup5 = self.soup.find('td', {'id': f'td5_{i}'})
            td5 = Td5(soup5)

            tdss.add_td([td3, td4, td5])
            i = i + 1
        
        #print(tdss.tds[0][0].test())
        print(tdss.tds[0][0].get_id())
        print(tdss.tds[0][0].get_日付())
        print(tdss.tds[0][0].get_商品コード())
        print(tdss.tds[0][0].get_商品名())
        print(tdss.tds[0][0].get_数量())
        
        print(tdss.tds[1][1].test())
        print(tdss.tds[1][1].get_注文者_名前())
        print(tdss.tds[1][1].get_注文者_ペンネーム())
        print(tdss.tds[1][1].get_注文者_郵便番号())
        print(tdss.tds[1][1].get_注文者_住所())
        print(tdss.tds[1][1].get_注文者_電話番号())
        print(tdss.tds[1][1].get_注文者_メールアドレス())
        print(tdss.tds[1][1].get_送り先_郵便番号())
        print(tdss.tds[1][1].get_送り先_名前())
        print(tdss.tds[1][1].get_送り先_ペンネーム())
        print(tdss.tds[1][1].get_送り先_住所())
        print(tdss.tds[1][1].get_送り先_電話番号())
        print(tdss.tds[1][1].get_送り先_メールアドレス())
        print(tdss.tds[1][1].get_送り先_住所())

        
class TDss():
    def __init__(self):
        self.tds = []
        
    def add_td(self, td):
        self.tds.append(td)


class Td3():
    def __init__(self, soup):
        self.soup = soup

    def get_all(self):
        return self.soup.find_all("small")
        
    def test(self):
        s = 0
        print("対応表_表示")
        for i in self.get_all():
            print(f"=={s}==")
            print(i)
            print("")
            s = s + 1

    def get_id(self):
        return self.soup.find_all("small")[1].text.replace(" （商品ページ）", "").strip()

    def get_日付(self):
        temp = self.soup.find_all("small")[9].text.replace("月", "/")
        temp = temp.replace("日", "/")
        temp = temp.replace("時", ":")
        temp = temp.replace("分", "")
        return temp.strip()
    
    def get_商品名(self):
        return self.soup.find_all("small")[7].text.strip()
    
    def get_商品コード(self):
        return self.soup.find_all("small")[7].text.strip()
    
    def get_数量(self):
        return int(self.soup.find_all("small")[11].text.replace("個", "").strip())
    
    
class Td4():
    def __init__(self, soup):
        self.soup = soup

    def get_all(self):
        return self.soup.find_all("small")
        
    def test(self):
        s = 0
        print("対応表_表示")
        for i in self.get_all():
            print(f"=={s}==")
            print(i)
            print("")
            s = s + 1

    def get_注文者_名前(self):
        return self.soup.find_all("small")[9].text.strip()
    
    def get_注文者_ペンネーム(self):
        return
    
    def get_注文者_郵便番号(self):
        return
    
    def get_注文者_住所(self):
        return
    
    def get_注文者_電話番号(self):
        return
    
    def get_注文者_メールアドレス(self):
        return self.soup.find_all("small")[11].text.strip()

    
    def get_送り先_名前(self):
        return self.soup.find_all("small")[3].text.strip()
    
    def get_送り先_ペンネーム(self):
        return
    
    def get_送り先_郵便番号(self):
        temp = self.soup.find_all("small")[5].text.split(" ")[0]
        return temp.strip()
    
    def get_送り先_住所(self):
        temp = self.soup.find_all("small")[5].text.split(" ")[1]
        return temp.strip()
    
    def get_送り先_電話番号(self):
        return self.soup.find_all("small")[7].text.strip()
    
    def get_送り先_メールアドレス(self):
        return





class Td5():
    def __init__(self, soup):
        self.soup = soup

    def get_all(self):
        return self.soup.find_all("small")
        
    def test(self):
        s = 0
        print("対応表_表示")
        for i in self.get_all():
            print(f"=={s}==")
            print(i)
            print("")
            s = s + 1
            

if __name__ == '__main__':
    rakuten = Rakuten()
    rakuten.main()
    print(yahoo_auction.get_id())
    print(yahoo_auction.get_日付())
    print(yahoo_auction.get_商品コード())
    print(yahoo_auction.get_商品名())
    print(yahoo_auction.get_数量())
    print(yahoo_auction.get_注文者_名前())
    print(yahoo_auction.get_注文者_ペンネーム())
    print(yahoo_auction.get_注文者_郵便番号())
    print(yahoo_auction.get_注文者_住所())
    print(yahoo_auction.get_注文者_電話番号())
    print(yahoo_auction.get_注文者_メールアドレス())
    print(yahoo_auction.get_送り先_郵便番号())
    print(yahoo_auction.get_送り先_名前())
    print(yahoo_auction.get_送り先_ペンネーム())
    print(yahoo_auction.get_送り先_住所())
    print(yahoo_auction.get_送り先_電話番号())
    print(yahoo_auction.get_送り先_メールアドレス())
    print(yahoo_auction.get_送り先_住所())
