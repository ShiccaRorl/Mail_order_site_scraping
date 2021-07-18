# -*- encoding: utf-8 -*-

from flask import Flask, request, render_template  # 追加

from sqlalchemy import Column, Integer, String, DateTime, Boolean

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import desc

engine = create_engine("sqlite:///db.db")

Base = automap_base()

# engine, suppose it has two tables 'user' and 'address' set up
#engine = get_engine()

# reflect the tables
Base.prepare(engine, reflect=True)

# mapped classes are now created with names by default
# matching that of the table name.


product_registration = Base.classes.Product_registration
config = Base.classes.Config



from converter import Core
from amazon import Amazon
#from . import rakuten
#from . import yahoo_auction
#from . import rakuma

app = Flask(__name__)

dict01 = {}

@app.route('/')
def index():
    #dict01['seed'] = ''
    if request.method == 'POST':
        dict01['seed'] = request.form.get('seed')
        dict01['code'] = request.form.get('code')
        if dict01['code'] != None or dict01['code'] != "":
            # dbからデータを入れます。
            session = Session(engine)
            product = session.query(Product_registration).filter(product_registration.code == dict01['code']).first()
            
            # dbから読み込み
            dict01['code'] = product.code
            dict01['name'] = product.名前
            dict01['hanbai_kakaku'] = product.販売価格
            dict01['hanbai_kakaku_x_10'] = product.販売価格X10
            dict01['hanbai_kakaku_rakuten'] = product.販売価格_楽天
            dict01['hanbai_kakaku_rakuma'] = product.販売価格_ラクマ
            dict01['gedai'] = product.下代
            dict01['zaiko'] = product.在庫
            dict01['konpo'] = product.梱包サイズ
            dict01['setumei'] = product.商品説明
            dict01['saizu'] = product.サイズ
            dict01['hinsitu'] = product.品質
            dict01['monita'] = config.モニター説明
            dict01['gara'] = config.柄説明
            dict01['yuupa'] = config.ゆうパケット説明
            dict01['comment'] = product.コメント

        else:
            core = Core()
            core.set_seed(dict01['seed'])

            dict01['code'] = core.get_code()
            dict01['name'] = core.get_商品名()
            dict01['hanbai_kakaku'] = core.get_販売価格()
            dict01['hanbai_kakaku_x_10'] = core.get_販売価格_税込()
            dict01['hanbai_kakaku_rakuten'] = core.get_楽天価格()
            dict01['hanbai_kakaku_rakuma'] = core.get_ラクマ価格()
            dict01['gedai'] = "" # core.
            dict01['zaiko'] = "" # core.
            dict01['konpo'] = core.get_梱包サイズ()
            dict01['setumei'] = core.get_商品説明()
            dict01['saizu'] = core.get_サイズ()
            dict01['hinsitu'] = core.get_品質()
            dict01['monita'] = "※ご覧頂くモニター等の環境により、多少色具合が異なって見える場合がございます。" # str(request.form.get('monita'))
            dict01['gara'] = "※商品は、見本品撮影の為、生地裁断の関係により柄の配置は画像と多少異なります。"
            dict01['yuupa'] = "こちらの商品は、ゆうパケット(追跡ナンバー付きゆうメール便)での発送となります。 ゆうパケットは、ポスト投函での配達となり、当店発送の翌日より、日本郵便ホームページにてお荷物追跡が可能となります。到着までの日数は、当店より発送後、北海道４日程度、沖縄、離島７日程度、その他の地域３日程度となります。" # str(request.form.get('yuupa'))
            dict01['comment'] = "" # ""
        
    return render_template('index.html', dict01=dict01)


@app.route('/edit', methods=['POST', 'GET'])
def edit():
    #print(seed)

    if request.method == 'POST':
        
        dict01['seed'] = request.form.get('seed')
        #seed = request.form.get('seed')

        dict01['riyu1'] = request.form.get('riyu1')
        dict01['riyu2'] = request.form.get('riyu2')
        dict01['riyu3'] = request.form.get('riyu3')
        dict01['id'] = str(request.form.get('id'))
        dict01['name'] = str(request.form.get('name'))
        #if dict01['hanbai_kakaku'] == [''] or dict01['hanbai_kakaku'] == None:
        #    dict01['hanbai_kakaku'] = 0
        dict01['hanbai_kakaku'] = str(request.form.get('hanbai_kakaku'))
        #print(dict01['hanbai_kakaku'])
        #if dict01['hanbai_kakaku'] != [''] or dict01['hanbai_kakaku'] != None:
        #    dict01['hanbai_kakaku_x_10'] = str(int(dict01['hanbai_kakaku']) * 1.1) #request.form.get('hanbai_kakaku_x_10')
        dict01['hanbai_kakaku_x_10'] = request.form.get('hanbai_kakaku_x_10')
        dict01['gedai'] = request.form.get('gedai')
        dict01['zaiko'] = request.form.get('zaiko')
        dict01['konpo'] = request.form.get('konpo')
        dict01['setumei'] = str(request.form.get('setumei'))
        dict01['saizu'] = request.form.get('saizu')
        dict01['hinsitu'] = str(request.form.get('hinsitu'))
        dict01['monita'] = str(request.form.get('monita'))
        dict01['gara'] = str(request.form.get('gara'))
        dict01['yuupa'] = str(request.form.get('yuupa'))
        dict01['comment'] = str(request.form.get('comment'))
       

        return render_template('edit1.html', dict01=dict01)
    return render_template('index.html', dict01=dict01)


@app.route('/amazon', methods=['POST', 'GET'])
def amazon_run():
    if request.method == 'POST':
        
        
        
        
        
        
        
        try:
            riyu1 = request.form.get['riyu1']
        except:
            riyu1 = False
        try:
            riyu2 = request.form.get['riyu2']
        except:
            riyu2 = False
        try:
            seed = request.form.get['seed']
        except:
            seed = ""

    amazon_db = Amazon()
    amazon_db.set_seed(seed)
    amazon_db.set_柄(riyu1)
    amazon_db.set_バリエーション(riyu2)

    return render_template('amazon.html', amazon_db=amazon_db, riyu1=riyu1, riyu2=riyu2)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80, threaded=True)