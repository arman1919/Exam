# analyze a text

def dell_n(word):

    if word[0:1]=="\n":
        return word[1:]
    elif word[-1:] == "\n":
        return word[:-1]
    else:
        return word

def searc_word(line:str,word:str):
    words = line.split(" ")
    if word in words:
        return True
    return False



# name = input("File name -")
name = "data.txt"
text = open(name,"r")

f = text.read()

print("1 Word Count:","\n",
      "2 Character Count:","\n",
      "3 Line Count:","\n",
      "4 Most Frequent Words:","\n",
      "5 Word Search:","\n")
sel = input("select an action - ")



if sel == "1":
    ls = f.split(" ")
    print(len(ls))

elif sel == "2":
    print(len(f))

elif sel == "3":
    print(f.count("\n"))


elif sel == "4":
    ls = f.split(" ")
    new_ls = []
    for i in ls:
        simbol = [",","'",'"',".","=",":",]
        if i not in simbol:
            new_ls.append(dell_n(i))


    words = {}
    for i in new_ls:
        words[i] = ls.count(i)

    counter = 0

    top10 = {}

    while counter !=10:
        word = ""
        count = 0
        for i in words:
            if words[i] >= count:
                word = i
                count = words[i]
        print(word,"--",count)

        top10[word] = count
        del words[word]

        counter +=1



elif sel == "5":
    word = input("Enter search word - ")
    word_line = []
    line_num = 1
    with open(name, 'r') as file:
        for line in file:
            if searc_word(line,word):
                word_line.append(word+'-'+str(line_num))
            line_num += 1
    if len(word_line) == 0:
        print("no this word")
    else:
        print(word_line)


else:
    print("no option!")