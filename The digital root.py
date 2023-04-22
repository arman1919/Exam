# The digital root




num = int(input("enter number - "))
num = str(num)
while len(num) != 1:
    new_num = 0
    for i in num:
        new_num += int(i)
    num = str(new_num)


print(num)