# JSON Editor

import json

with open("example.json", 'r') as f:
    data = json.load(f)

print(data)

comand = "name=harry"

ls = comand.split(".")
ls [-1] = ls[-1].split("=")

new_ls=[]

for i in range(len(ls)-1):
    new_ls.append(ls[i])

new_ls.append(ls[-1][0])
new_ls.append(ls[-1][1])

ls = new_ls

current = data
for key in ls[:-2]:
    current = current[key]


current[ls[-2]] = ls[-1]

with open('example.json', 'w') as f:
    json.dump(data, f)
