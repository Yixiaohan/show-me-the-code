#Converted a text file to a xls file
import ast
import xlwt
import xlrd
f = open('student.txt', 'r')
file=ast.literal_eval(f.read())

row_list=[]
for key, value in file.items():
    row_list.append([key]+value)
column_list = zip(*row_list)

workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('Student')
i=0
for column in column_list:
    for item in range(len(column)):
        value=column[item]
        worksheet.write(item,i,value)
    i+=1
workbook.save('student.xls')
