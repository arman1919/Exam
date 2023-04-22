# Phone Book

namefile = "Phone_Book.txt"

def new_cotact():
    name = input("name- ")
    surname = input("surname- ")
    phone_number = input("phone number- ")
    address = input("address- ")

    return (name+" "+surname+" "+phone_number+" "+address)

print("add New cotact - 1 \nedit cotact - 2\ndelite contact - 3")

selec = int(input("select operation - "))


if selec == 1:
    with open(namefile,"r") as f:
        count_line = f.read().count("\n")

    with open(namefile, "a") as f:

        f.write(str(count_line)+" "+new_cotact()+"\n")



elif selec == 2:
    with open(namefile,"r") as f:
        print(f.read(),'\n')
        f.seek(0)
        cotacts = f.read().split("\n")

    line = int(input("seclect contact for edit - "))
    cotacts[line] = (str(line)+" "+new_cotact())

    with open(namefile,"w") as f:
        for i in cotacts:
            f.write(str(i)+"\n")


elif selec == 3:
    with open(namefile,"r") as f:
        print(f.read(),'\n')
        f.seek(0)
        cotacts = f.read().split("\n")

    line = int(input("seclect contact for delete - "))
    cotacts.pop(line)
    with open(namefile, "w") as f:
        for i in range(len(cotacts)-1):
            f.write(str(i)+" "+cotacts[i][2:] + "\n")
else:
    print("no operatin")
