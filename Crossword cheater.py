# Crossword cheater:


fruits = ['apple', 'banana', 'cherry', 'pear', 'orange',
          'pineapple', 'mango', 'kiwi', 'peac', 'pomegranate']


word = input("enter word")

def check(word1,word2):
    if len(word1) != len(word2):
        return False

    for i in range(len(word1)):
        if word1[i] != word2[i] and word2[i] != "*":
            return False
    return True

def check_words(ls,word):
    for i in ls:
        if check(i,word):
            yield i


words = list(check_words(fruits,word))

print(words)