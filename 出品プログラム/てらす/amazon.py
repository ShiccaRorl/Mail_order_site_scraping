# -*- encoding: utf-8 -*-

import re

from converter import core


class amazon(core):
    def __init__(self):
        print("amazon")

    def set_amazon_id(self, amazonid):
        self.set_amazon_id = amazonid

    def get_商品名2(self):
        if self.get_柄() == False or self.get_バリエーション() == False:
            return str(self.get_商品名()) + "  " + str(self.get_code())
        elif self.get_柄() == True or self.get_バリエーション() == True:
            return str(self.get_商品名())

    def get_販売価格2(self):
        # amazonは税込みです
        return self.get_販売価格_税込()

    def get_出品者SKU(self):
        return self.get_code()

    def get_在庫数(self):
        return 0

    def get_ブランド名(self):
        return "和もーる"

    def get_アイテムパッケージ数(self):
        return 1

    def get_バリエーション設定(self):
        if self.get_バリエーション() == True:
            return self.get_code()  # , self.get_販売価格()
        else:
            print("バリエーション無し")
            return None

    def get_商品の仕様(self):
        return self.get_商品説明()

    def get_商品説明文(self):
        return self.get_商品説明()

    def get_素材構成(self):
        return self.get_品質()

    def get_品質2(self):
        return self.get_品質()


if __name__ == "__main__":

    with open("seed.txt", 'r', encoding="utf-8") as f:
        seed = f.read()
        f.close()

    amazon = amazon()
    amazon.set_seed(seed)

    print("商品名 :  " + str(amazon.get_商品名2()))
    print("販売価格   : " + str(amazon.get_販売価格2()))
    print("出品者SKU   : " + str(amazon.get_出品者SKU()))
    print("在庫数   : " + str(amazon.get_在庫数()))
    print("販売価格   : " + str(amazon.get_販売価格2()))
    print("販売価格   : " + str(amazon.get_販売価格2()))
    print("販売価格   : " + str(amazon.get_販売価格2()))
    print("販売価格   : " + str(amazon.get_販売価格2()))
    print("販売価格   : " + str(amazon.get_販売価格2()))
    print("販売価格   : " + str(amazon.get_販売価格2()))
    print("販売価格   : " + str(amazon.get_販売価格2()))
