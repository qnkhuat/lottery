from tkinter import *
from data_ulis import *



'''
TODO:
- create input method note : DONE
- create cover data: DONE
- auto check win-lost method :DONE
- auto compute balance : DONE
- rewrite the scrawl method:DONE
- write update result method:DOING
- write view history
- write view history balance
'''


def main():
    file_path='./excels/history.xlsx'
    # input_data(file_path)
    # check_win()
    # convert_data('./excels/history.xlsx')
    update()
    # scrawl_day('http://ketqua.net/xo-so-mien-bac.php?ngay=19-04-2018')


if __name__=='__main__':
    main()
