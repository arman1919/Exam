#name_list

with open("namelist.txt","r") as f:
    names = f.read().split("\n")


def vowels_word(name:str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    lett = []
    for i in name:
        if i.lower() == "u":
            lett.append("u")
            break
        if i.lower() in vowels:
            lett.append(i.lower())

    return lett

def check_leter(ls):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in ls:
        if i in vowels:
            vowels.remove(i)
    if len(vowels) == 0:
        return True
    return False

new_names = []

for i in names:
    letters = vowels_word(i)
    print(letters)
    if vowels_word(i) == sorted(vowels_word(i)) and check_leter(letters):
        new_names.append(i)

print(new_names)



