"""
print("--- 1697 숨바꼭질 ---")

from collections import deque
q=deque()
depth=[0]*(10**5+1)

def bfs(x):
  q.append(x)
  while q:
    x=q.popleft()

    if x==m:
      return(depth[x])

    for i in (x-1,x+1,x*2):
      if i>=0 and i<=10**5:
        if depth[i]==0:
          q.append(i)
          depth[i]=depth[x]+1

  return("님 좆됨")


n,m=map(int,input().split())
print(bfs(n))
"""
"""
print("--- 13913 숨바꼭질 4 ---")

#몰루


"""

print("--- 14226 이모티콘 ---")


































