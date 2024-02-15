import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def DFS(now,last):
  global id
  visited[now] = ID[now] = id
  for next in graph[now]:
    if next==last:
      continue
    if not visited[next]:
      id += 1
      DFS(next,now)
      if ID[next]==visited[next]:
        result.append(sorted((now,next)))
    visited[now] = min(visited[now],visited[next])

N,M = map(int,input().split())
graph = [[] for i in range(N+1)]
for _ in range(M):
  a,b = map(int,input().split())
  graph[a].append(b); graph[b].append(a)
visited = [0]*(N+1); ID = [0]*(N+1)
result = []
for i in range(1,N+1):
  if not visited[i]:
    id = 1
    DFS(i,i)
print(len(result))
for r in sorted(result):
  print(*r)