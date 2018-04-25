from tkinter import *
from data_ulis import *




'''
TODO:
- create input method note : DONE
- create cover data: DONE
- auto check win-lost method :DONE
- auto compute balance : DONE
- rewrite the scrawl method:DONE
- write update result method:
'''


def main():
    file_path='./excels/history.xlsx'
    # input_data(file_path)
    check_win()
    # convert_data('./excels/history.xlsx')


if __name__=='__main__':
    main()
