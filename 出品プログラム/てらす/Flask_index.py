# -*- encoding: utf-8 -*-

from flask import Flask, request, render_template  # 追加


#from converter import core
from amazon import amazon
#from . import rakuten
#from . import yahoo_auction
#from . import rakuma

app = Flask(__name__)


@app.route('/')
def index():
    #seed = ""
    #riyu1 = False
    #riyu2 = True
    return render_template('index.html')


@app.route('/edit', methods=['POST', 'GET'])
def edit():
    #seed = "seed"
    # print(seed)

    if request.method == 'POST':
        seed = str(request.form['seed'])
        # this is executed if the request method was GET or the
        # credentials were invalid
        return render_template('edit.html', seed=seed)
    return render_template('index.html', seed=seed)


@app.route('/amazon', methods=['POST', 'GET'])
def amazon_run():
    if request.method == 'POST':
        try:
            riyu1 = request.form['riyu1']
        except:
            riyu1 = False
        try:
            riyu2 = request.form['riyu2']
        except:
            riyu2 = False
        try:
            seed = request.form['seed']
        except:
            seed = ""

    amazon_db = amazon()
    amazon_db.set_seed(seed)
    amazon_db.set_柄(riyu1)
    amazon_db.set_バリエーション(riyu2)

    return render_template('amazon.html', amazon_db=amazon_db, riyu1=riyu1, riyu2=riyu2)


# おまじない
if __name__ == "__main__":
    app.run(debug=True)
