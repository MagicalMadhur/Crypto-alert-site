from flask import Flask, render_template, request
import json

f = open('/home/madhur65/mysite/coin.json', 'r')
value= json.load(f)["coins"]

app = Flask(__name__)

Currencies = ["INR", "USD", "PKR","CNY", "EUR"]



@app.route("/")
def hello():
    return render_template('index.html', value=value)

@app.route("/calsi/<string:coin_name>")
def calsi(coin_name):
    return render_template('calci.html',value=value,coin_name=coin_name )

@app.route("/post/<string:coin_symbol>/<string:currency>", methods=['GET'])
def post_route(coin_symbol, currency):

    return render_template('crypto_price.html', coin_symbol=coin_symbol, currency=currency, Currencies=Currencies)

@app.route("/alerts", methods = ['GET', 'POST'])
def alerts():
    if(request.method=='POST'):
        coin = request.form.get('coin')
        email = request.form.get('email')
        price = request.form.get('price')
        renge = request.form.get('range')
        pricelen = len(str(price))
        priceless = pricelen - 3
        price = str(price)[1:int(priceless)]
        price = price.replace(",", "")

        data = {"COIN" : str(coin),"email" : str(email),"Target_Price" : int(price),"Range" : str(renge)}

        with open('config.json', 'r') as jason_file:
            value = json.load(jason_file)
            value["alerts"].append(data)
        with open('config.json', 'w') as jason_file1:
            json.dump(value, jason_file1)




    return render_template('alerts.html')

