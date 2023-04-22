#student info corect

# walter melon melon@email.msmary.edu 555-3141

with open("students.txt","r") as f:
    info = f.read().split("\n")

def corect_info(s:str):
    ls = s.split()
    ls[0] = ls[0].capitalize()
    ls[1] = ls[1].capitalize()
    ls[3] = "301-"+ls[3]

    return ls[0]+"    "+ls[1]+"    "+ls[2]+"    "+ls[3]

with open("students2.txt","w") as f:
    for i in info:
        f.write(corect_info(i))

