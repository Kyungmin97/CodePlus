
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










