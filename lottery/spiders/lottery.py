import scrapy
import datetime
import pprint
import openpyxl
from openpyxl.styles import Color, PatternFill, Font, Border
from calendar import Calendar



def get_urls(years,months):

    start_urls=[]
    href='http://ketqua.net/xo-so-mien-bac.php?ngay='
    for year in years:
        for mo in months:
            days = Calendar().itermonthdates(year,mo)
            for day in days:
                if day.month == mo:
                    #update date to write initial col
                    url=href+ day.strftime('%d-%m-%Y')
                    start_urls.append(url)
    return start_urls


def get_color(number):
    if number ==1 :
        return PatternFill(start_color='2ecc71',end_color='2ecc71',fill_type='solid')#green
    elif number ==2:
        return  PatternFill(start_color='2980b9',end_color='2980b9',fill_type='solid')#blue
    elif number==3:
        return  PatternFill(start_color='f1c40f',end_color='f1c40f',fill_type='solid')#yellow
    elif number ==4:
        return  PatternFill(start_color='e74c3c',end_color='e74c3c',fill_type='solid')#red
    else:
        return  PatternFill(start_color='FFFF0000',end_color='FFFFFF',fill_type='solid')#white



class lottery(scrapy.Spider):
    name='lot'

    def __init__(self):
        try:
            wb=openpyxl.load_workbook('lottery.xlsx')
        except:
            wb=openpyxl.Workbook()
            wb.save('lottery.xlsx')

        wb=openpyxl.load_workbook('lottery.xlsx')
        sheet = wb.active
        #get the max row to update
        self.row=sheet.max_row if sheet.max_row !=0 else 1
        self.date = ''



        years=[2018]
        months=[4,5]
        self.start_urls=get_urls(years,months)
        self.current=0




    def start_requests(self):
        date= self.start_urls[self.current].split('=')
        yield scrapy.Request(url=self.start_urls[self.current],callback=self.parse,meta={'date':date[1]})



    def parse(self,response):
        divs = response.css('.chu17.need_blank::text')
        ###date don't have number will not save
        if len(divs)!=0:
            numbers = dict((el,0) for el in range(100))
            for div in divs:
                number = int(div.extract())
                numbers[number]+=1


            wb=openpyxl.load_workbook('lottery.xlsx')
            sheet = wb.active

            #write datetime
            sheet.cell(row=self.row,column=1).value=response.meta.get('date')


            ##write numbers
            for col,val in numbers.items():
                if val!=0:
                    sheet.cell(row=self.row,column=col+2).value=val
                    sheet.cell(row=self.row,column=col+2).fill=get_color(val)
            self.row+=1

            wb.save('lottery.xlsx')

        self.current+=1
        date= self.start_urls[self.current].split('=')
        yield scrapy.Request(url=self.start_urls[self.current],callback=self.parse,meta={'date':date[1]})
