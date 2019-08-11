import jieba.analyse
import os
import docx

def open_docx(filepath):
    d = [j for j in os.listdir(filepath) if j.endswith('.docx')]
    for each in d:
        try:
            file = docx.Document(filepath + '\\' + each)
            text = ''
            for para in file.paragraphs:
                if not para.text == '':
                    text += para.text.strip()
            keywords = jieba.analyse.textrank(text, topK=2, withWeight=False, allowPOS=('n', 'vn'))
            #keywords = jieba.analyse.textrank(text, topK=2, withWeight=False)

            print(each,keywords)
        except:
            pass

#目前的问题在于无法打开加密的文件，而我自己的日记密码我也忘了，有点难受
#open_docx的使用方式是直接传入docx的目录，利用jieba分词对目录中的每一个docx分析提取得出频率最高的关键词
#问题在于，jieba分词所得到的未必就是关键词未必准确，同时加上自己语言使用上的问题，准确度有待考量
open_docx('E:\\Watchwords\\心事二三两')
