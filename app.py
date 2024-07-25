from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///investment_game.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    balance = db.Column(db.Float, default=10000.0)

class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(10), unique=True, nullable=False)
    price = db.Column(db.Float, nullable=False)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/buy', methods=['GET', 'POST'])
def buy_stock():
    if request.method == 'POST':
        # 주식 구매 로직 구현
        pass
    return render_template('buy.html')

@app.route('/sell', methods=['GET', 'POST'])
def sell_stock():
    if request.method == 'POST':
        # 주식 판매 로직 구현
        pass
    return render_template('sell.html')

@app.route('/portfolio')
def view_portfolio():
    # 사용자 포트폴리오 표시 로직
    return render_template('portfolio.html')

if __name__ == '__main__':
    app.run(debug=True)