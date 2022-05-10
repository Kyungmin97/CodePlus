
"""
print("--- 13023 ABCDE ---")

n,m=map(int,input().split())
arr=[[] for i in range(n)]
visited=[False]*n

for _ in range(m):
  a,b=map(int,input().split())
  arr[a].append(b)
  arr[b].append(a)

def dfs(idx,number):
  if number==4:
    print(1)
    exit()
  for i in arr[idx]:
    if not visited[i]:
      visited[i]=True
      dfs(i,number+1)
      visited[i]=False

for i in range(n):
  visited[i]=True
  dfs(i,0)
  visited[i]=False
print(0)
"""

"""
print("--- 1260 DFS와 BFS ---")
from collections import deque

def dfs(v):
  print(v, end=' ')
  visited[v]=True
  for i in range(n+1):
    if not visited[i] and graph[v][i]==1:
      dfs(i)


def bfs(v):
  queue=deque()
  visited[v]=True
  queue.append(v)
  while queue:
    v=queue.popleft()
    print(v,end=' ')
    for i in range(n+1):
      if not visited[i] and graph[v][i]==1:
        queue.append(i)
        visited[i]=True



n,m,v=map(int,input().split())
graph=[[0]*(n+1) for i in range(n+1)]
visited=[False]*(n+1)
for i in range(m):
  x,y=map(int,input().split())
  graph[x][y]=graph[y][x]=1


dfs(v)
print()
visited=[False]*(n+1)
bfs(v)
"""

"""
print("--- 11724 연결 요소의 개수 ---")

n,m=map(int,input().split())
graph=[[0]*(n+1) for _ in range(n+1)]
visited=[False]*(n+1)
for i in range(m):
  x,y=map(int,input().split())
  graph[x][y]=graph[y][x]=1

def dfs(idx):
  if visited[idx]==False:
    visited[idx]=True
    for i in range(n+1):
      if graph[idx][i]==1:
        dfs(i)

answer=0
for i in range(1,n+1):
  if visited[i]==False:
    answer+=1
    dfs(i)

print(answer)
"""

print("--- 1707 이분 그래프 ---")


















