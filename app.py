import tkinter as tk
from data_ulis import *
from tkinter import ttk
import tkinter.messagebox as tm
import datetime
import logging
'''
TODO:
- create input method note : DONE
- create cover data: DONE
- auto check win-lost method :DONE
- auto compute balance : DONE
- rewrite the scrawl method:DONE
- write update result method:DONE # BUG: but just can update new day
- basic GUI: DONE
- Balance view : DONE
- History view
- write view history :
- write view history balance
'''

class but:
    def __init__(self,root,row,col,text,command):
        global turn
        self.row=row
        self.col=col

        self.button=tk.Button(root,text=text,height=2,width=5,command = command)
        self.button.grid(row=row,column=col,padx=10,pady=5)
        self.button.config( width = '30', height = '4')



def display_balance(frame):
    balance = check_balance()
    display_text = tk.Label(frame,text=balance)
    display_text.pack()
    # display_text.insert(tk.END, balance)


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        self.geometry('300x300')
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, InputPage, HistoryPage,BalancePage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        self.curent_button = 0 #to update button number
        self.file_path='./excels/history.xlsx'
        self.data_path='./excels/lottery100.xlsx'

        tk.Frame.__init__(self, parent)
        self.controller = controller



        balance = check_balance(self.data_path,self.file_path)
        message='Vốn còn: ' + '{:0,}đ'.format(balance)
        self.balance_status = tk.Label(self, text=message)
        self.balance_status.pack(side="top", fill="x", pady=10)
        self.update()


        input_button=self.get_button('InputPage',controller)
        history_button=self.get_button('HistoryPage',controller)
        banlance_button=self.get_button('BalancePage',controller)
        input_button.pack()
        history_button.pack()
        banlance_button.pack()

    def update(self):##update label each 1s
        balance = check_balance(self.data_path,self.file_path)
        message='Vốn còn: ' + '{:0,}đ'.format(balance)
        self.balance_status['text']=message
        self.balance_status.after(1000, self.update) # call this method again in 1,000 milliseconds



    def get_button(self,Page_name,controller):
        return tk.Button(self, text=Page_name,
                            command=lambda: controller.show_frame(Page_name))






class InputPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.file_path='./excels/history.xlsx'
        self.date,self.data='',{}
        self.number_temp=0#temparaty variable to save number input



        label = tk.Label(self, text="Nhập lịch sử chơi ")
        label.pack(side="top", fill="x", pady=10)

        # XXX: title of phase
        self.title = tk.Label(self,text='Chơi ngày nào nhỉ(dd/mm)')
        self.title.pack()


        self.input = tk.Entry(self)
        self.input.pack()

        self.input.bind('<Return>',self.get_date)

        self.done_button = tk.Button(self, text='Done',command=self.go_to_home_page)#generate run button but dont appear


        # write_new_date(date,data,file_path)

        #back to start page
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()



    def get_date(self,event=None):
        current_year = str(datetime.datetime.now().year)

        self.temp = self.input.get()#get date input
        if(date_valid(self.temp)):# if date valid so pass this phase
            date =self.input.get()
            self.date=datetime.datetime.strptime(date + '/'+ current_year, '%d/%m/%Y').strftime('%d-%m-%Y')
            self.input.delete(0,'end')#clear input
            self.input.bind('<Return>',self.get_number)

            self.title['text']='Con nào?'#change title
            self.done_button.pack()#appear the done button out
        else:
            tm.showerror('Error','Ngày không hợp lệ')


    def get_number(self,event=None):
        number = self.input.get() # output of input

        if number.isdigit():
            self.number_temp = number
            self.data[number]=0# initia dicts
            self.input.delete(0,'end')#clear input
            self.input.bind('<Return>',self.get_amount)


            self.title['text']='Bao trứng?'#change title
            self.done_button.pack_forget()#hide the button when input amount

        else:
            tm.showerror('Error','Số không hợp lệ')

        # write_new_date(self.date,self.data,self.file_path)



    def get_amount(self,event=None):

        amount = self.input.get() # output of input

        if amount.isdigit() and int(amount)>0:
            self.data[self.number_temp]=amount
            self.input.delete(0,'end')#clear input
            self.input.bind('<Return>',self.get_number)#back to get_number


            self.title['text']='Con nào?'#change title
            self.done_button.pack()#hide the button when input amount

        else:
            tm.showerror('Error','Số lượng không hợp lệ')

    def go_to_home_page(self,event=None):#when input amount done done_button will appear
        write_new_date(self.date,self.data,self.file_path)
        self.input.bind('<Return>',self.get_date)#reset the input to get date
        self.data,self.data='',[] #delete all the cache
        self.controller.show_frame('StartPage') #back to start page when type click done


class HistoryPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.file_path='./excels/history.xlsx'
        self.data_path='./excels/lottery100.xlsx'

        label = tk.Label(self, text="This is HistoryPage")
        label.pack(side="top", fill="x", pady=10)


        #back to start page
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class BalancePage(tk.Frame):
    # TODO: write warnings when capital low
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.file_path='./excels/history.xlsx'
        self.data_path='./excels/lottery100.xlsx'

        balance = check_balance(self.data_path,self.file_path)
        message='Vốn còn: ' + '{:0,}đ'.format(balance)

        label = tk.Label(self, text=message)
        label.pack(side="top", fill="x", pady=10)


        #back to start page
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()




def main():
    data_path='./excels/lottery100.xlsx'
    file_path='./excels/history.xlsx'

    # input_data(file_path)
    # check_win()
    # convert_data('./excels/history.xlsx')
    # update()
    # scrawl_day('http://ketqua.net/xo-so-mien-bac.php?ngay=19-04-2018')

    '''
    GUI tasks:
    - check balance Button
    - input number and amount
    - update (or auto update when open)
    - watch history balance and play

    '''
    logging.info('Open')
    update()
    app = SampleApp()
    app.mainloop()



if __name__=='__main__':
    main()
