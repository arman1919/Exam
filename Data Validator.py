# Data Validator

def email_check(email:str):
    if email.count("@") != 1:
        return False
    if not email[0].isalpha():
        return False

    ls = email.split("@")
    ls[-1] = ls[-1].split(".")

    new_ls = []

    for i in range(len(ls) - 1):
        new_ls.append(ls[i])

    new_ls.append(ls[-1][0])
    new_ls.append(ls[-1][1])
    ls = new_ls

    if len(ls) != 3 or len(ls[0]) == 0 or len(ls[1]) == 0 or len(ls[2]) == 0:
        return False

    for i in ls[1]:
        if not i.isalpha():
            return False

    for i in ls[2]:
        if not i.isalpha():
            return False

    if " " in ls[0]:
        return False

    return True


def check_lower(s:str):
    for i in s:
        if not i.islower() and i.isalpha():
            return False
    return True

def url_check(url:str):
    if url.count(".") != 2:
        return False

    if " " in url:
        return False
    if url[0:11] !="http://www." and url[0:12] != "https://www.":
        return False

    ls = url.split(".")

    if not check_lower(ls[1]):
        return False

    path = ls[2]

    ls = path.split("/")

    for i in ls:
        if not check_lower(i):
            return False

    return True


def date_check(date):
    ls = date.split(".")
    if len(ls) != 3:
        return False
    if len(ls[0]) != 2 or len(ls[1]) != 2 or len(ls[2]) != 4:
        return False

    for i in ls:
        if not i.isdigit():
            return False

    if int(ls[0]) > 31 or int(ls[1]) > 12:
        return False

    return True

def number_check(number:str):
    return number.isdigit()


def credit_cart_check(num:str):
    if num.count(" ") != 3:
        return False

    ls = num.split()
    for i in ls:
        if len(i) != 4 or not i.isdigit():
            return False

    return True

def mobile_phone_check(num):
    if len(num) != 9:
        return False
    if num[0] != "0":
        return False
    if not num.isdigit():
        return False
    return  True


select = input("""select data type
1. Email
2. Website URL
3. Date
4. Number
5. Credit Card Number
6. Mobile Phone Number
---- """)

if select == "1":

    mail = input("Enter email -")
    if email_check(mail):
        print("Correct email")
    else:
        print("Uncorrecr emali")

elif select == "2":

    url = input("Enter url -")
    if url_check(url):
        print("Correct url")
    else:
        print("Uncorrecr url")

if select == "3":

    date = input("Enter date -")
    if date_check(date):
        print("Correct date")
    else:
        print("Uncorrecr date")

if select == "4":

    num = input("Enter number -")
    if number_check(num):
        print("Correct number")
    else:
        print("Uncorrecr number")

if select == "5":

    card = input("Enter credit cart number -")
    if credit_cart_check(card):
        print("Correct credit cart number")
    else:
        print("Uncorrecr credit cart number")

if select == "6":

    phone = input("Enter phone number -")
    if mobile_phone_check(phone):
        print("Correct phone number")
    else:
        print("Uncorrecr phone number")


