# The Library Management

name_file = "data.txt"

def add_book():
    book_name = input("Enter book name - ")
    author = input("Enter author - ")
    date = input("Enter date - ")

    with open(name_file,"a") as f:
        f.write(book_name +" "+author+" "+date + "\n" )
    with open(name_file,"r") as f:
        books = f.read().split("\n")
        books.sort()
    print(books)
    with open(name_file,'w') as f:
        for i in books[1:]:
            f.write(i + "\n")




def del_book():
    name = input("Enter name delite book - ")
    with open(name_file,"r") as f:
        books = f.read().split("\n")

    for i in books:
        if name in i:
            books.remove(i)
            break

    with open(name_file, 'w') as f:
        for i in books:
            f.write(i + "\n")


def print_bibl():
    with open(name_file,"r") as f:
        print(f.read())


