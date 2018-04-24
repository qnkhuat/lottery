from tkinter import *
<<<<<<< HEAD
import openpyxl as xl
=======
>>>>>>> 12d27c74cf4a9645260c82421f6ff8dafb9f3501
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
<<<<<<< HEAD
# NOTE: global vairble
date_col=1


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
=======


# XXX: create a saving file
def open_file(file_path):
    try:
        wb=openpyxl.load_workbook(self.file_path)
    except:
        wb=openpyxl.Workbook()
        wb.save(self.file_path)

    return wb



# XXX: method to write into excel
def write_to_sheet(col_name,row,sheet,content):
>>>>>>> 12d27c74cf4a9645260c82421f6ff8dafb9f3501
    '''
    Usange
    col_name =[date,number,amount]
    row: row to write
    '''
<<<<<<< HEAD
=======
    col =1 if col_name=='date' else 2 if col_name =='number' else 3 # NOTE: 3 when col_name==amount

>>>>>>> 12d27c74cf4a9645260c82421f6ff8dafb9f3501
    sheet.cell(row=row,column=col).value = content
    return sheet



<<<<<<< HEAD
def write_new_date(date,data,file_path):
    '''
    data = {number:amount}
    '''
    wb,sheet,max_row,max_col=open_file(file_path,active=True)


    i=2#to keep track of how many number we write
    for number,amount in data.items():
        row_for_number= max_row+1
        row_for_amount= max_row+2
        sheet.cell(row=alo,column=i).value=number
        sheet.cell(row=alo+1,column=i).value=amount
        i+=1

    sheet.cell(row=max_row+1,column=date_col).value=date
    sheet.merge_cells(start_row=int(max_row+1),start_column=date_col,end_row=int(max_row+2),end_column=date_col)


    wb.save(file_path)


    # sheet.cell(row=max_row+1).value=date









=======
>>>>>>> 12d27c74cf4a9645260c82421f6ff8dafb9f3501

# IDEA: convert all data to dict and use this to do all check_win,check_balance
def convert_data():
    pass

def check_win():
    pass

def check_balance():
    pass

def get_history():
    pass



<<<<<<< HEAD
def input_data(file_path):
=======
def input_data():
>>>>>>> 12d27c74cf4a9645260c82421f6ff8dafb9f3501
    '''
    ask how many number first
    then ask for number and amount for each of it
    '''

    date = input('Đi chợ ngày nào thế?(dd/mm)\n')+'/2018'# BUG: add method to check valid date and auto fill current year


    stop = False
    data ={}
    while not stop:
        number = input_digit('Đánh con nào?(Hết thì đánh stop)\n')

        if  number.isdigit():
            amount = input_digit('Bao nhiêu trứng?\n')
            data[number]=amount
        else:
            stop =True

<<<<<<< HEAD
    write_new_date(date,data,file_path)
=======

    print(data)


    pass



>>>>>>> 12d27c74cf4a9645260c82421f6ff8dafb9f3501




<<<<<<< HEAD
# NOTE: input ulis
=======
# NOTE: input _ulis
>>>>>>> 12d27c74cf4a9645260c82421f6ff8dafb9f3501

def input_digit(content):

    stop = False
    while not stop:
        value = input(content)
        if value=='stop':
            stop = True
        elif value.isdigit():
            stop = True
        else :
            print('Không hợp lệ')

    return value
