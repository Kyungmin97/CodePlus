
"""
print("--- 16929 Two Dots  ---")

n,m=map(int,input().split())
graph=[]
visited=[[0]*m for _ in range(n)]
for i in range(n):
  graph.append(str(input()))
               
dx=[0,0,-1,1]
dy=[-1,1,0,0]

def dfs(depth,x,y,alpha):
  if visited[y][x]==0:
    visited[y][x]=depth
    
  for i in range(4):
    nx=x+dx[i]
    ny=y+dy[i]

    if nx<0 or ny<0 or nx>=m or ny>=n:
      continue
    if visited[ny][nx]==1 and graph[ny][nx]==alpha and visited[y][x] != 2:
      print('Yes')
      exit()
    if visited[ny][nx] == 0 and graph[ny][nx]==alpha:
      dfs(depth+1,nx,ny,alpha)

for i in range(n):
  for j in range(m):
    visited=[[0]*m for _ in range(n)]
    dfs(1,j,i,graph[i][j])
print('No')
"""

print("--- 16947 서울 지하철 2호선  ---")

import sys
sys.setrecursionlimit(10**5)
n = int(input())
array = [[i] for i in range(0,n+1)]
for _ in range(n):
    a, b = map(int,input().split())
    array[a].append(b)
    array[b].append(a)
visit = [False] * (n+1)
surcle = []

def DFS(x,start,v):
    visit[x] = True
    
    if x in array[start] or x == start:
        if v >= 3:
            surcle.append(x)
            return
    
    for i in array[x]:
        if visit[i] == False:
            DFS(i,start,v+1)
            visit[i] = False

for i in range(1,n+1):
    DFS(i,i,1)
    visit[i] = False

t = n+1

def mmin(start,v):
    global t
    visit[start] = True
    for i in array[start]:
        if i in surcle:
            t = min(t,v)
            return
        if visit[i] != True:
            mmin(i,v+1)
            visit[i] = False
    
brray = []
for i in range(1,n+1):
    if i in surcle:
        brray.append(0)
    else:
        mmin(i,1)
        brray.append(t)
        t = n+1
        visit[i] = False

print(*brray)

