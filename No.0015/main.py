import xlwt
import json

# create a new workbook
wb = xlwt.Workbook()
ws = wb.add_sheet("city")

file = open("city.txt")
cont = json.load(file)

num_stu = len(cont)

# write into a execl file
row = 0
col = 0
# init the col and row

for id in range(num_stu):
    col = 0 
    prop = cont[str(id+1)]
    num_prop = len(prop)
    ws.write(row, col, id+1)
    col = col + 1
    ws.write(row, col, cont[str(id+1)])
    col = col + 1
    row = row + 1
wb.save('output.xls')


