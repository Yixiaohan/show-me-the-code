# -*- coding:utf-8 -*-

import xlsxwriter
import json


def json2xls():
    wb = xlsxwriter.Workbook('student.xls')
    ws = wb.add_worksheet('student')
    with open('student.txt', 'rb') as f:
        data_byte = f.read()
        data = json.loads(str(data_byte, 'utf-8'))
        print(data)
        for i in range(len(data)):
            ws.write(i, 0, i + 1)
            json_data = data[str(i + 1)]
            for j in range(len(json_data)):
                ws.write(i, j + 1, json_data[j])
        wb.close()


if __name__ == '__main__':
    json2xls()
