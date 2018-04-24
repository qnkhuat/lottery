from tkinter import *
import openpyxl as xl
import datetime
'''
- Check balance
- Input
- Auto confirm
- Upload to google docs


### database layout
- date  : number1 number2 number3 number4
- date  : amount1 amount2 amount3 amount3


#solution
- to search,display : loop thourgh the data and create a dictionary.

'''
# NOTE: global vairble
date_col=1
data_path='./excels/history.xlsx'


# NOTE: handle excel file
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



def write_to_sheet(col_name,row,col,sheet,content):# XXX: method to write into excel

    '''
    Usange
    col_name =[date,number,amount]
    row: row to write
    '''

    sheet.cell(row=row,column=col).value = content
    return sheet



def write_new_date(date,data,file_path):
    '''
    data = {number:amount}
    '''
    wb,sheet,max_row,max_col=open_file(file_path,active=True)


    i=2#to keep track of how many number we write
    for number,amount in data.items():
        row_for_number= max_row
        row_for_amount= max_row+1
        sheet.cell(row=row_for_number,column=i).value=number
        sheet.cell(row=row_for_amount,column=i).value=amount
        i+=1

    sheet.cell(row=max_row,column=date_col).value=date

    sheet.merge_cells(start_row=int(max_row),start_column=date_col,end_row=int(max_row+1),end_column=date_col)


    wb.save(file_path)






# IDEA: convert all data to dict and use this to do all check_win,check_balance
def convert_data():
    '''
    data[date]={
        number:[],
        amount:[]
    }
    '''
    wb,sheet,max_row,max_col = open_file(data_path,active=True)

    data={}
    for i in range(1,max_row+1,2):# NOTE: loop through date
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
        data[sheet.cell(row=i,column=date_col).value]=temp

    return data

def check_win():
    pass

def check_balance():
    pass

def get_history():
    pass



def input_data(file_path):
    '''
    ask how many number first
    then ask for number and amount for each of it
    '''
    current_year = str(datetime.datetime.now().year)
    date = input('Đi chợ ngày nào thế?(dd/mm)\n')+'/'+ current_year
    while not date_valid(date):
        print('Ngày không hợp lệ')
        date = input('Đi chợ ngày nào thế?(dd/mm)\n')+'/'+ current_year


    stop = False
    data ={}
    while not stop:
        number = input_digit('Đánh con nào?(Hết thì đánh stop)\n')
        if  number.isdigit():
            amount = input_digit('Bao nhiêu trứng?\n')
            data[number]=amount
        else:
            stop =True

    write_new_date(date,data,file_path)



# NOTE: input _ulis
def date_valid(date):
    try:
        datetime.datetime.strptime(date, '%d/%m/%Y')
    except :
        return False
    return True




def input_digit(content):
    while True:
        value = input(content)
        if value=='stop':
            return value
        elif value.isdigit():
            return value
        else :
            print('Không hợp lệ')
