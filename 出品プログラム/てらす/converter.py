# -*- encoding: utf-8 -*-

import re


class core:
    def set_seed(self, seed):
        self.seed = str(seed)
        self.seed = self.seed.split('\t')
        print(self.seed)
        return self.seed

    def set_柄(self, gara):
        self.柄 = gara

    def set_バリエーション(self, bari):
        self.バリエーション = bari

    def get_柄(self):
        return self.柄

    def get_バリエーションの設定(self):
        return self.バリエーション

    def get_code(self):
        if self.seed[0] == None:
            return None
        elif self.seed[0] == "":
            return None
        elif self.seed[0] == '':
            return None
        else:
            return str(self.seed[0])

    def get_商品名(self):
        if self.seed[9] == None:
            return None
        elif self.seed[9] == "":
            return None
        elif self.seed[9] == '':
            return None
        else:
            return str(self.seed[9])

    def get_販売価格(self):
        if self.seed[10] == None:
            return None
        elif self.seed[10] == "":
            return None
        elif self.seed[10] == '':
            return None
        else:
            return int(self.seed[10])

    def get_販売価格_税込(self):
        if self.get_販売価格() == None:
            return None
        elif self.get_販売価格() == "":
            return None
        elif self.get_販売価格() == '':
            return None
        else:
            return int(self.get_販売価格() * 1.1)

    def get_楽天価格(self):
        # 楽天は税抜き価格です。
        return int(self.get_販売価格())

    def get_ラクマ価格(self):
        # ラクマは税金、送料の込々価格
        if self.seed[11] == None:
            return None
        elif self.seed[11] == "":
            return None
        elif self.seed[11] == '':
            return None
        else:
            return int(self.seed[11])

    def get_発送方法(self):
        if self.seed[12] == None:
            return None
        elif self.seed[12] == "":
            return None
        elif self.seed[12] == '':
            return None
        else:
            return str(self.seed[12])

    def get_発送料_ゆうパケット(self):
        if self.seed[13] == None:
            return None
        elif self.seed[13] == "":
            return None
        elif self.seed[13] == '':
            return None
        else:
            return int(self.seed[13])

    def get_定形外郵便(self):
        if self.seed[14] == None:
            return None
        elif self.seed[14] == "":
            return None
        elif self.seed[14] == '':
            return None
        else:
            return int(self.seed[14])

    def get_梱包サイズ(self):
        if self.seed[15] == None:
            return None
        elif self.seed[15] == "":
            return None
        elif self.seed[15] == '':
            return None
        else:
            return int(self.seed[15])

    def get_商品説明(self):
        if self.seed[24] == None:
            return None
        elif self.seed[24] == "":
            return None
        elif self.seed[24] == '':
            return None
        else:
            s = re.search(r'(.*?)サイズ：', str(self.seed[24]))
            t = s.group(0)
            t = t.replace('サイズ：', '')
            if t == None:
                return None
            elif t == "":
                return None
            elif t == '':
                return None
            else:
                return str(t)
        return None

    def set_サイズ(self, size):
        self.サイズ = size

    def set_品質(self, 品質):
        self.品質 = 品質

    def get_サイズ(self):
        if self.seed[24] == None:
            return None
        elif self.seed[24] == "":
            return None
        elif self.seed[24] == '':
            return None
        else:
            s = re.search(r'サイズ：(.*?)品質：', str(self.seed[24]))
            t = s.group(0)
            t = t.replace('サイズ：', '')
            t = t.replace('品質：', '')
            if t == None:
                return None
            elif t == "":
                return None
            elif t == '':
                return None
            else:
                return str(t)
        return None

    def get_品質(self):
        if self.seed[24] == None:
            return None
        elif self.seed[24] == "":
            return None
        elif self.seed[24] == '':
            return None
        else:
            s = re.search(r'品質：(.*)', str(self.seed[24]))
            t = s.group(0)
            t = t.replace('品質：', '')
            if t == None:
                return None
            elif t == "":
                return None
            elif t == '':
                return None
            else:
                return str(t)
        return None


if __name__ == "__main__":

    with open("seed.txt", 'r', encoding="utf-8") as f:
        seed = f.read()
        f.close()

    core = core()
    seed = core.set_seed(seed)

    s = 0
    for i in seed:
        print(str(s) + " : " + i)
        s = s + 1

    print("code               : " + str(core.get_code()))
    #print("柄　　　　　　　　　:　" + str(core.get_柄()))
    #print("バリエーション　　　:　" + str(core.get_バリエーション()))
    print("商品名             : " + str(core.get_商品名()))
    print("販売価格           : " + str(core.get_販売価格()))
    print("販売価格_税込      : " + str(core.get_販売価格_税込()))
    print("ラクマ価格         : " + str(core.get_ラクマ価格()))
    print("発送方法           : " + str(core.get_発送方法()))
    print("発送料_ゆうパケット : " + str(core.get_発送料_ゆうパケット()))
    print("定形外郵便         : " + str(core.get_定形外郵便()))
    print("梱包サイズ         : " + str(core.get_梱包サイズ()))

    print("商品説明           : " + str(core.get_商品説明()))

    print("サイズ             : " + str(core.get_サイズ()))

    print("品質               : " + str(core.get_品質()))
