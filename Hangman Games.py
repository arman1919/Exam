# Hangman Games

import random


f = open("data.txt","r")

words = f.read().split("\n")

attempt = 3

word_0 = words[random.randrange(0,len(words))]

w0 = []
w1 = []

for i in word_0:
    w1.append("_")
    w0.append(i)

print(w1,w0)

win_message = "you lose!"

while attempt != 0:
    if "".join(w1) == word_0:
        win_message = "You win!"
        break
    x = input("enter let").lower()
    if x in w0:
        print(w0.index(x))
        w1[w0.index(x)] = x
        w0[w0.index(x)] = " "
        print(w1)
        print("attempt = ",attempt)
    else:
        attempt -=1
        print("attempt = ",attempt)

print(win_message)





