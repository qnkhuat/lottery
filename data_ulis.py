from tkinter import *
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
    '''
    Usange
    col_name =[date,number,amount]
    row: row to write
    '''
    col =1 if col_name=='date' else 2 if col_name =='number' else 3 # NOTE: 3 when col_name==amount

    sheet.cell(row=row,column=col).value = content
    return sheet




# IDEA: convert all data to dict and use this to do all check_win,check_balance
def convert_data():
    pass

def check_win():
    pass

def check_balance():
    pass

def get_history():
    pass



def input_data():
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


    print(data)


    pass







# NOTE: input _ulis

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
