import numpy as np
import openpyxl
from data_ulis import update


file_path = './excels/lottery.xlsx'
save_path = '../bang phan tich/analysis.xlsx'


def get_percentage(sheet):
    ###compute percentage
    max_row=sheet.max_row+1
    max_col=sheet.max_column

    row=max_row+1
    sheet.cell(row=row,column=1).value='Tỉ lệ %'
    for i in range(2,max_col+1):
        sheet.cell(row=row,column=i).value='=SUM(INDIRECT(ADDRESS(1,COLUMN())&":"&ADDRESS(ROW()-1,COLUMN())))*100/'+str(max_row)



def get_frequency(sheet):
    max_row=sheet.max_row+1
    max_col=sheet.max_column

    row=max_row +1 +1
    sheet.cell(row=row,column=1).value='Tần suất xuất hiện:'
    row=max_row +1 +1 +1
    sheet.cell(row=row,column=1).value='Trung bình xuất hiện:'
    row=max_row +1 +1 +1 +1
    sheet.cell(row=row,column=1).value='Chuỗi dài nhất:'

    for i in range(2,max_col+1):#loop through column
        frequency=0
        appeareance=[]
        result = ''
        max=0
        for l in range(1,max_row+1+1):#loop through rows

            if sheet.cell(row=l,column=i).value is not None:#when a number appear

                if frequency==0:
                    result+='|'

                else:
                    result+=str(frequency)+'|'

                appeareance.append(frequency)
                frequency=0
                max=np.max(appeareance)

            else:
                frequency+=1
        sheet.cell(row=l+1,column=i).value=result#+1 because don't overwrite percentage
        sheet.cell(row=l+2,column=i).value=np.mean(appeareance)
        sheet.cell(row=l+3,column=i).value=max





def main():
    update('excels/lottery.xlsx')


    wb=openpyxl.load_workbook(file_path)
    for sheet_name in ['100','300','800']:
        sheet=wb[sheet_name]


        get_percentage(sheet)
        get_frequency(sheet)

        wb.save(save_path)







if __name__=='__main__':
    main()
