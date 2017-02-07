import re
import glob
from collections import Counter

files = glob.glob("*.txt")
for file in files:
    print(file)
    with open(file, "r") as f:
        txt = f.read()
        reg = re.compile(r'[\w]+')
        wordList = reg.findall(txt)
        cntObj = Counter(wordList)
        print(cntObj.most_common(1))
