# File Compression:

with open("data.txt","r") as f:
    words = f.read().split("\n")


def Compression(word:str):

    new_word = ''
    count = 1
    for i in range(len(word)-1):
        if word[i]==word[i+1]:
            count += 1
        else:
            new_word += word[i]+str(count)
            count = 1
    count = 1
    for i in range(len(word) - 1, -1, -1):

        if word[i]==word[i-1]:
            count += 1
        else:
            new_word += word[i]+str(count)
            break

    return new_word

with open("data_out.txt","w") as f:
    for i in words:
        f.write(Compression(i)+"\n")




