# read the word
file = open('./filtered_words.txt')
sense_word = set()
word_tmp = "init"
while True:
    word_tmp = file.readline()
    word_tmp = word_tmp.rstrip()
    if word_tmp:
        sense_word.add(word_tmp)
    else:
        break
print(sense_word)

user_input = input()
if(sense_word.issubset(user_input)):
    print('Freedom')
else:
    print('Human Rights')
