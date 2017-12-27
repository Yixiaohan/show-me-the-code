import re

def count_the_words(path):
    with open(path) as f:
        text=f.read()
        wordlist=re.findall(r'[a-zA-Z0-9]+', text)
        print(wordlist)
        count=len(wordlist)

    return count
if __name__ == '__main__':
    nums = count_the_words('.\\file.txt')
print (nums)



