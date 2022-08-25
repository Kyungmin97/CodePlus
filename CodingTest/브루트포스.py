"""
print("\tQuestion "+"3085")

n = int(input())
array = []
for _ in range(n):
    array.append(list(map(str,input())))
maxCount = 0

def width():
    global  maxCount

    for i in range(n):
        countRow = 1
        for j in range(n - 1):
            if array[i][j] == array[i][j + 1]:
                countRow += 1 
                maxCount = max(maxCount,countRow) 
            else: 
                countRow = 1 
              
def height():
    global  maxCount

    for i in range(n):
        countRow = 1
        for j in range(n - 1):
            if array[j][i] == array[j+1][i]:
                countRow += 1 
                maxCount = max(maxCount,countRow) 
            else: 
                countRow = 1 
      

for i in range(n):
    for j in range(n - 1):
      if array[i][j] != array[i][j + 1]:
            array[i][j], array[i][j + 1] = array[i][j + 1], array[i][j]
            width()
            height()
            array[i][j + 1], array[i][j] = array[i][j], array[i][j + 1]
    for j in range(n - 1):
      if array[j][i] != array[j+1][i]:
            array[j][i], array[j+1][i] = array[j+1][i], array[j][i]
            width()
            height()
            array[j][i], array[j+1][i] = array[j+1][i], array[j][i]
    
print(maxCount)
"""
"""
print("\tQuestion "+"1476")

e,s,m=map(int,input().split())

cnt=0
a,b,c=0,0,0
while(True):
  cnt+=1
  a+=1
  b+=1
  c+=1
  if a>15:
    a-=15
  if b>28:
    b-=28
  if c>19:
    c-=19
  if a==e and b==s and c== m:
    break

print(cnt)
"""
"""
print("\tQuestion "+"1107")
n = int(input())
m = int(input())
nlist=set()
if(m):
  nlist = set(input().split())
answer=abs(n-100)

for num in range(1000001):
  for i in str(num):
    if i in nlist:
      break
  else:
    answer=min(answer,abs(n-num)+len(str(num)))
      
print(answer)
"""

#Question 14500

def dfs(x,y,cnt,depth):
  dx=[1,0,-1,0]
  dy=[0,1,0,-1]
  global answer
  #print(x,y,cnt,depth,answer)

  cnt+=graph[y][x]
  if depth==4:
    #print(answer,cnt)
    answer=max(answer,cnt)
    return
  
  visited[y][x]=True
  
  for i in range(4):
    nx=x+dx[i]
    ny=y+dy[i]
    if nx<0 or ny<0 or nx>=m or ny>=n:
      continue
    if visited[ny][nx]==True:
      continue
    dfs(nx,ny,cnt,depth+1)
  visited[y][x]=False

def fuckyou(x,y,n,m):
  global answer
  p1=p2=p3=p4=p6=p7=p8=p9=0
  if y>0:
    if x>0:
      p7=graph[y-1][x-1]
    p8=graph[y-1][x]
    if x<m-1:
      p9=graph[y-1][x+1]
  if x>0:
    p4=graph[y][x-1]
  if x<m-1:
    p6=graph[y][x+1]
  if y<n-1:
    if x>0:
      p1=graph[y+1][x-1]
    p2=graph[y+1][x]
    if x<m-1:
      p3=graph[y+1][x+1]
  
  cnt=graph[y][x]+max(p7+p8+p9,p7+p4+p1,p1+p2+p3,p3+p6+p9)
  answer=max(cnt,answer)
  return
  


n,m=map(int,input().split())
visited=[[False]*(m) for _ in range(n)]
graph=[]
for _ in range(n):
  graph.append(list(map(int,input().split())))
answer=0

for i in range(n):
  for j in range(m):
    dfs(j,i,0,1)
  
for i in range(n):
  for j in range(m):
    fuckyou(j,i,n,m)
print(answer)
  


