string = input()
length = len(string)

cnt = 1
for i, elem in enumerate(string):
    if elem == " ":
        cnt += 1

        if i == 0 or i == (length - 1):
            cnt -= 1

if length == 0:
    cnt = 0
if length == 1 and string[0] == " ":
    cnt = 0

print(cnt)