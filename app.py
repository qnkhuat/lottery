from tkinter import *
from data_ulis import *




'''
TODO:
- create input method note : DONE
- create cover data: DONE
- auto check win-lost method :DOING
- auto compute balance
'''


def main():
    file_path='./excels/history.xlsx'
    # input_data(file_path)
    # check_win()
    convert_data('./excels/history.xlsx')


if __name__=='__main__':
    main()
