import tkinter as tk
from data_ulis import *
from tkinter import ttk

'''
TODO:
- create input method note : DONE
- create cover data: DONE
- auto check win-lost method :DONE
- auto compute balance : DONE
- rewrite the scrawl method:DONE
- write update result method:DONE # BUG: but just can update new day
- write view history :
- write view history balance
- GUI: DOING
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

        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the start page")
        label.pack(side="top", fill="x", pady=10)

        balance = check_balance()

        message='Vốn còn: ' + '{:0,}đ'.format(balance)

        label = tk.Label(self, text=message)
        label.pack(side="top", fill="x", pady=10)


        input_button=self.get_button('InputPage',controller)
        history_button=self.get_button('HistoryPage',controller)
        banlance_button=self.get_button('BalancePage',controller)
        input_button.pack()
        history_button.pack()
        banlance_button.pack()



    def get_button(self,Page_name,controller):
        return tk.Button(self, text=Page_name,
                            command=lambda: controller.show_frame(Page_name))



class InputPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is InputPage ")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class HistoryPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is HistoryPage")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class BalancePage(tk.Frame):
    # TODO: write warnings when capital low
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        balance = check_balance()

        message='Vốn còn: ' + '{:0,}đ'.format(balance)

        label = tk.Label(self, text=message)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


def main():
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
    update()
    app = SampleApp()
    app.mainloop()



if __name__=='__main__':
    main()
