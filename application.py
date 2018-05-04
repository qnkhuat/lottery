from flask import Flask,render_template,request
import openpyxl as xl
import datetime
from collections import OrderedDict
import os
# from data_ulis import check_balance,check_balance_detail,write_new_date,convert_data_to_dict,convert_history_to_dict
from data_ulis import *


app = Flask(__name__)
app.debug =True


@app.route('/')
def index():
    try:
        update('excels/lottery.xlsx')
    except:
        pass
    balance = check_balance('./excels/lottery300.xlsx','./excels/history.xlsx')
    return render_template('index.html',balance='{:0,}đ'.format(balance))

@app.route('/insert', methods=['GET', 'POST'])
def insert():
    if request.method=='GET':
        return render_template('insert.html')
    elif request.method == 'POST':
        date=request.form.get('date')
        numbers=request.form.getlist('number')
        amounts=request.form.getlist('amount')
        data=dict(zip(numbers, amounts))
        write_new_date(date,data,'./excels/history.xlsx')
        balance = check_balance('./excels/lottery300.xlsx','./excels/history.xlsx')
        return render_template('index.html',balance='{:0,}đ'.format(balance))

@app.route('/history')
def history():
    capital ,won,lose,daily_capital= check_balance_detail('./excels/lottery300.xlsx','./excels/history.xlsx')
    data=convert_history_to_dict('./excels/history.xlsx')
    data = OrderedDict(sorted(data.items(), key = lambda x:datetime.datetime.strptime(x[0], '%d-%m-%Y')))
    balance = check_balance('./excels/lottery300.xlsx','./excels/history.xlsx')
    return render_template('history.html',data=data,won=won,lose=lose,daily_capital=daily_capital,balance='{:0,}đ'.format(balance))



# if __name__ == '__main__':
#     import logging
#     logging.basicConfig(filename='error.log',level=logging.DEBUG)
#     app.run()
