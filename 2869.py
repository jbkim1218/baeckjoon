A, B, V = map(int, input().split())

x = (V-B)/(A-B)
if x == int(x):
    print(int(x))
else:
    print(int(x) + 1)