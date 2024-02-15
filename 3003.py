n_list = [1, 1, 2, 2, 2, 8]
y_list = list(map(int,input().split()))

for i in range(6):
    print(n_list[i] - y_list[i], end=' ')