import numpy as np
import openpyxl



file_path = './excels/lottery100.xlsx'
save_path = './excels/analysis100.xlsx'

wb=openpyxl.load_workbook(file_path)
sheet=wb.active

max_row=sheet.max_row+1
max_col=sheet.max_column


def get_percentage():
    ###compute percentage

    row=max_row+1
    sheet.cell(row=row,column=1).value='Tỉ lệ %'
    for i in range(2,max_col+1):
        sheet.cell(row=row,column=i).value='=SUM(INDIRECT(ADDRESS(1,COLUMN())&":"&ADDRESS(ROW()-1,COLUMN())))*100/'+str(max_row)

    wb.save(save_path)

def get_frequency():
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


    wb.save(save_path)



def main():
    get_percentage()
    get_frequency()







if __name__=='__main__':
    main()
