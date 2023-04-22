# An acronym

with open("data.txt","r") as f:
    words = f.read().split("\n")


acronym = "pcydhfd"

acronym_words = []

for i in acronym:
    for j in words:
        if j[0].lower() == i.lower():
            acronym_words.append(j)
            words.remove(j)
            break

print(acronym_words)




