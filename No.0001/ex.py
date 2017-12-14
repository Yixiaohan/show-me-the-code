import random
import string

def gener(num):
    time = 0;
    sum = set()
    while  time < num:
        string_tmp = ''
        while len(string_tmp) < 20:
            dic = random.choice([1,2,3,4,5,6,7,8,9])
            if(dic % 4 == 0 ):
                number = random.choice([1,2,3,4,5,6,7,8,9])
                string_tmp += str(number)
            else:
                char_tmp = random.choice(string.ascii_letters)
                string_tmp += char_tmp
        sum.add(string_tmp)
        time += 1
    return sum

if __name__ == "__main__":
    discount = gener(20)
    print(discount)
