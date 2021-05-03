# -*- coding:utf-8 -*-

import sys

from sqlalchemy import Column, String, Integer, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from setting import Base
from setting import ENGINE


# user.db というデータベースを使うという宣言です
#engine = create_engine('sqlite:///./DB/Affiliate.SQLite3')
# Base = declarative_base()  # データベースのテーブルの親です


class Seed(Base):
    """
    ユーザモデル
    """
    __tablename__ = 'seed'
    id = Column('id', Integer, primary_key=True)
    code = Column('cood', String())
    siteID = Column('siteID', Integer())
    create_at = Column('create_at', DateTime())
    update_at = Column('update_at', DateTime())
    
    purchase_date = Column('日付', DateTime())
    product_code = Column('商品コード', String())
    Product_name = Column('商品名', String())
    quantity = Column('数量', Integer)

    buyer_name = Column('購入者_名前', String())
    buyer_pen_name = Column('購入者_ペンネーム', String())
    buyer_zip_code = Column('購入者_郵便番号', String())
    buyer_address = Column('購入者_住所', String())
    buyer_phone_number = Column('購入者_電話番号', String())
    buyer_email_address = Column('購入者_メールアドレス', String())
    
    destination_name = Column('送り先_名前', String())
    destination_pen_name = Column('送り先_ペンネーム', String())
    destination_zip_code = Column('送り先_郵便番号', String())
    destination_address = Column('送り先_住所', String())
    destination_phone_number = Column('送り先_電話番号', String())
    destination_email_address = Column('送り先_メールアドレス', String())
    
    purchase_price = Column('購入金額', Integer())
    shipping = Column('送料', Integer())
    total_fee = Column('合計金額', Integer())


class Seeds(Base):
    __tablename__ = 'seeds'
    id = Column('id', Integer, primary_key=True)
    code = Column('code', String())
    siteID = Column('siteID', Integer())
    seed = Column('seed', String())
    analysis_completed = Column('解析完了', Boolean())
    create_at = Column('create_at', DateTime())
    update_at = Column('update_at', DateTime())

def main(args):
    """
    メイン関数
    """
    Base.metadata.create_all(bind=ENGINE)


if __name__ == "__main__":
    main(sys.argv)
