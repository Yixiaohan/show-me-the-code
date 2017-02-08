#! usr/bin/python3
import re
import time
import urllib.request


url = input("Enter URL >")
with urllib.request.urlopen(url) as response:
    content = response.read()
    try:
        content = content.decode("utf-8")
    except UnicodeDecodeError:
        content = content.decode("gbk")
    content = re.sub(r'<title.+?</title>', '', content, flags=re.DOTALL)
    content = re.sub(r'<head(er)?.+?</head(er)>', '', content, flags=re.DOTALL)
    content = re.sub(r'<(no)?script.+?</(no)?script>', '\
        ', content, flags=re.DOTALL)
    content = re.sub(r'<style.+?</style>', '', content, flags=re.DOTALL)
    content = re.sub(r'<form.+?</form>', '', content, flags=re.DOTALL)
    content = re.sub(r'<footer.+?</footer>', '', content, flags=re.DOTALL)
    result = re.findall(r'(?<=>)[^<>]+?(?=<)', content)
    txt = ''.join(result).strip()
    file_name = time.strftime('%Y%m%d%H%M%S') + '.txt'
    with open(file_name, 'wt') as f:
        print(txt, file=f)
    print('Extract content to file:' + file_name)
