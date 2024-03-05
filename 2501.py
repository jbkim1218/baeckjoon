answer = []
N, k = map(int,input().split())

for i in range(1,N+1):
    if N % i == 0:
        answer.append(i)

answer.sort()  

if len(answer) < k:
    result = 0
else:
    result = answer[k-1]

print(result)