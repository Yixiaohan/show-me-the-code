# -*- coding:utf-8 -*-

import xlrd
import codecs
from lxml import etree


def xls_xml(file_name):
    # 从xls文件读取
    data = {}
    excel = xlrd.open_workbook(file_name)
    table = excel.sheet_by_name('city')
    nrows = table.nrows
    for i in range(nrows):
        key = str(int(table.row_values(i)[0]))
        value = str(table.row_values(i)[1:])
        data[key] = value
    # 写入到xml文件
    output = codecs.open('city.xml', 'w', 'utf-8')
    root = etree.Element('root')
    citys_xml = etree.ElementTree(root)
    citys = etree.SubElement(root, 'citys')
    citys.append(etree.Comment('城市信息'))
    citys.text = str(data)
    output.write(etree.tounicode(citys_xml.getroot()))
    output.close()


if __name__ == '__main__':
    xls_xml('city.xls')
