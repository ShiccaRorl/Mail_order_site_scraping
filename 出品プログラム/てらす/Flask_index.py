# -*- encoding: utf-8 -*-

from flask import Flask, request, render_template  # 追加


from converter import Core
from amazon import Amazon
#from . import rakuten
#from . import yahoo_auction
#from . import rakuma

app = Flask(__name__)


@app.route('/')
def index():
    seed = ""
    if request.method == 'POST':
        seed = request.form.get['seed']
    #riyu1 = False
    #riyu2 = True
    return render_template('edit1.html', seed=seed)


@app.route('/edit', methods=['POST', 'GET'])
def edit():
    #print(seed)

    if request.method == 'POST':
        seed = request.form.get('seed')
        
        core = Core()
        core.set_seed(seed)
        
        
        
        riyu1 = request.form.get('riyu1')
        riyu2 = request.form.get('riyu2')
        riyu3 = request.form.get('riyu3')
        id = str(request.form.get('id'))
        name = str(request.form.get('name'))
        hanbai_kakaku = request.form.get('hanbai_kakaku')
        hanbai_kakaku_x_10 = request.form.get('hanbai_kakaku_x_10')
        gedai = request.form.get('gedai')
        zaiko = request.form.get('zaiko')
        konpo = request.form.get('konpo')
        setumei = str(request.form.get('setumei'))
        saizu = request.form.get('saizu')
        hinsitu = str(request.form.get('hinsitu'))
        monita = str(request.form.get('monita'))
        yuupa = str(request.form.get('yuupa'))
        comment = str(request.form.get('comment'))
       

        return render_template('edit1.html', seed=seed)
    return render_template('index.html', seed=seed)


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