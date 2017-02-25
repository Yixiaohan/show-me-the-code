#! python3
# -*- coding:utf-8 -*-
import xlrd
book = xlrd.open_workbook("移动话费详单.xls")
print("The number of worksheets is {0}".format(book.nsheets))
print("Worksheet name(s): {0}".format(book.sheet_names()))
sh = book.sheet_by_index(0)
print("sheetName:{0} sheetRows:{1} sheetCols:{2}".format(
    sh.name, sh.nrows, sh.ncols))
print("Cell D4 is {0}".format(sh.cell_value(rowx=3, colx=3)))
sum = 0
for rx in range(sh.nrows):
    if rx != 0:
        print(sh.row(rx)[3].value)
        sum += float(sh.row(rx)[3].value)
    if rx == 3:
        print("合计：" + str(sum))
