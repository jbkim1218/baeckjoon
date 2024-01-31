N, M = map(int, input().split())
baskets = [0] * (N+1)

for _ in range(M):
    x, y, i = map(int, input().split())
    for j in range(x, y+1):
        baskets[j] = i

for i in range(1, len(baskets)):
    print(baskets[i], end=' ')