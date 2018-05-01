from flask import Flask,render_template,request
import openpyxl as xl
import datetime
from collections import OrderedDict
import os



app = Flask(__name__)
app.debug =True


@app.route('/')
def index():
    balance = check_balance('./excels/lottery300.xlsx','./excels/history.xlsx')
    return render_template('index.html',balance=balance)

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
        return render_template('index.html',balance=balance)

@app.route('/history')
def history():
    data=convert_history_to_dict('./excels/history.xlsx')
    data = OrderedDict(sorted(data.items(), key=lambda t: t[0]))# sort the date
    return render_template('history.html',data=data)

@app.route('/result')
def result():
    data=convert_data_to_dict('./excels/lottery300.xlsx')
    data = OrderedDict(sorted(data.items(), key=lambda t: t[0]))# sort the date
    return render_template('result.html',data=data)


















































































def write_new_date(date,data,file_path):
    '''
    data = {number:amount}
    '''
    wb,sheet,max_row,max_col=open_file(file_path,active=True)


    i=2#to keep track of how many number we write
    for number,amount in data.items():
        row_for_number= max_row+1
        row_for_amount= max_row+2
        sheet.cell(row=row_for_number,column=i).value=number
        sheet.cell(row=row_for_amount,column=i).value=amount
        i+=1

    sheet.cell(row=max_row+1,column=date_col).value=date
    # print(max_row)


    sheet.merge_cells(start_row=int(max_row+1),start_column=date_col,end_row=int(max_row+2),end_column=date_col)
    wb.save(file_path)
    # logging.info('Wrote new transaction')


date_col=1
def open_file(file_path,active=False):# XXX: create a saving file
    try:
        wb=xl.load_workbook(file_path)
    except:
        wb=xl.Workbook()
        wb.save(file_path)
        wb=xl.load_workbook(file_path)

    if active:
        sheet=wb.active

        return wb,wb.active,sheet.max_row,sheet.max_column # NOTE: max_row is the current row has written
    else:
        return wb


def convert_history_to_dict(path_dir):
    '''
    data[date]={
        number:[],
        amount:[]
    }
    '''
    wb,sheet,max_row,max_col = open_file(path_dir,active=True)

    data={}
    for i in range(2,max_row+1,2):# NOTE: loop through date
        temp={}
        numbers=[]
        amounts=[]
        for j in range(2,max_col+1):# NOTE: loop through numbers

            number = sheet.cell(row=i,column=j).value
            amount = sheet.cell(row=i+1,column=j).value


            if number is not None and amount is not None:
                numbers.append(number)
                amounts.append(amount)


        temp['number']= numbers
        temp['amount']= amounts
        date=sheet.cell(row=i,column=date_col).value
        data[date]=temp


    return data

def convert_data_to_dict(path_dir):
    '''
    data[date]=[0,0,0,1,3,0...]
    '''
    wb,sheet,max_row,max_col = open_file(path_dir,active=True)

    data={}
    for i in range(2,max_row+1,1):# NOTE: loop through date
        temp=[]
        for j in range(2,max_col+1):# NOTE: loop through numbers
            amount_of_win_number = 0 if sheet.cell(row=i,column=j).value is None else sheet.cell(row=i,column=j).value
            temp.append(amount_of_win_number)
        data[sheet.cell(row=i,column=date_col).value]=temp
    return data


def check_balance(data_path,history_path):
    capital = 50000000#start capital
    win_rate = 80/22

    win_money_per_tickey=80000
    money_per_ticket=22000

    history=convert_history_to_dict(history_path)
    data=convert_data_to_dict(data_path)

    for date in history.keys():
        day = history[date]
        try:## if day are not in data so pass it
            day_result = data[date]
            for idx,number in enumerate(day['number']):
                capital -= int(day['amount'][idx])*money_per_ticket # NOTE: first it will minus your fee
                capital += int(day['amount'][idx])*win_money_per_tickey*day_result[int(number)] # NOTE: then will plus with win and multiple rate

        except:
            pass

    return capital
