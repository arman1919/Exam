# text file analyze
file_name = input("Enter file name - ")


with open(file_name,"r") as  f:
    # count_word
    count_words = len(f.read().split())

    f.seek(0)
    # char_count
    char_count = 0
    for i in f.read():
        special_chars = ['*', '%', '#', '@', '!'," "]
        if i not  in special_chars:
            char_count += 1

    f.seek(0)
    # sentence_count
    separators = ['.', '!', '?']
    sentence_count = 0
    for char in f.read():
        if char in separators:
            sentence_count += 1

    f.seek(0)

    # most used letter

    leters = {}

    for i in f.read():
        if i.isalpha():
            if i.upper() not in leters:
                leters[i.upper()] = 1
            else:
                leters[i.upper()] += 1

    let = ''
    count_let = 0
    for i in leters:
        if leters[i] > count_let:
            count_let = leters[i]
            let = i

    f.seek(0)

    #the most used word in a text

    words_list = f.read().split()

    words = {}
    for i in words_list:
        if i not in words:
            words[i] = 1
        else:
            words[i] += 1


    word = ''
    count_word = 0
    for i in words:
        if words[i] > count_word:
            count_word = words[i]
            word = i


with open("info_text.txt","w") as f:
    f.write("word: "+str(count_words) + "\n" )
    f.write("letters: "+ str(count_let)+ "\n" )
    f.write("Sentences: "+ str(sentence_count)+ "\n")
    f.write("Letter frequency: "+let +" "+ str(count_let)+"\n")
    f.write("word frequency: " + word + " "+ str(count_word))








