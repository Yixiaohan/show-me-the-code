from html.parser import HTMLParser
from urllib.request import urlopen
from re import sub

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        pass
    def handle_endtag(self, tag):
        pass
    def handle_data(self, data):
        print(data)

def GetHTML():
    html = urlopen("http://www.baidu.com/")
    html_code = html.read(300)
    print( html_code)

if __name__ == '__main__':
    parser = MyHTMLParser()
    html = GetHTML()    
    

