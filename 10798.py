li = []
for i in range(5):
    temp = list(map(str, input()))
    while len(temp) != 15:
        temp.append("*")
    li.append(temp)
li2 = list(zip(*li))

for i in range(len(li2)):
    print("".join(li2[i]).replace("*", ""), end="")