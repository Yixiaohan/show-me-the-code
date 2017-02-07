import re
from collections import Counter


with open("test_doc.txt", "r") as f:
    txt = f.read()
    reg = re.compile(r'[\w]+')
    wordList = reg.findall(txt)
    cntObj = Counter(wordList)
    print(cntObj)
    while True:
        s = input("Enter word for search:\n")
        if s == "":
            break
        print(cntObj[s])
