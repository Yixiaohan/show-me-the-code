
def count_total(filename):
    file = open(filename)
    word = file.read().split()
    count_word = len(word)
    return count_word

if __name__  == "__main__":
    total = count_total("input.txt")
    print(total)
