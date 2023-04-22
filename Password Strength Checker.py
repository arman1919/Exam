# Password Strength Checker

f = open("data.txt","r")

words = f.read().split("\n")

class MyException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"MyException: {self.message}"



special_characters = ['!', '@', '#', '$', '%', '^', '&', '*',
                      '(', ')', '-', '+', '=', '{', '}', '[', ']',
                      '|', '\\', ';', ':', "'", '"', ',', '.',
                      '<', '>', '/', '?', '`', '~']



def check_pas(pasword:str):
    if len(pasword) < 8:
        raise MyException("the password is too short")
    for i in words:
        if i in pasword:
            raise MyException(f"the password contains common vocabulary word-{i}")
    num = 0
    up = 0
    low = 0
    chara = 0
    for i in pasword:
        if i == ' ':
            raise MyException("there are spaces in the password")
        if i.isdigit():
            num =1
        if i in special_characters:
            chara = 1
        if i.islower():
            low = 1
        if i.isupper():
            up = 1

    if low == 0:
        raise MyException("there is no lowercase letter in the password")
    if up == 0:
        raise MyException("there is no capital letter in the password")
    if num == 0:
        raise MyException("there is no digit in the password")
    if chara == 0:
        raise MyException("there are no special characters in the password")





try:
    password = input("enter password -")
    check_pas(password)
except MyException as e:
    print(e)
else:
    print("the password is strong")
