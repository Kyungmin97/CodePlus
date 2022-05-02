"""
print("--- 9095 1, 2, 3 더하기 ---")

def sums(n):
    if n == 1:
        return(1)
    elif n == 2:
        return(2)
    elif n == 3:
        return(4)
    else:
        return sums(n-1) + sums(n-2) + sums(n-3)

T=int(input())

for _ in range(T):
  n=int(input())
  print(sums(n))
"""

"""
print("--- 1759 암호 만들기 ---")

xlist=[]
def dfs(start,depth,L,C):
  if depth==L:
    cnt1=0
    cnt2=0
    for i in xlist:
      for j in temp:
        if j==i:
          cnt1+=1
          break
    cnt2=L-cnt1

    if cnt1>0 and cnt2>1:
      print(''.join(xlist))
    return
  for i in range(start,C):
    xlist.append(clist[i])
    dfs(i+1,depth+1,L,C)
    xlist.pop()
  return
    
L,C=map(int,input().split())
clist=list(map(str,input().split()))
clist.sort()
temp=['a','e','i','o','u']

dfs(0,0,L,C)
"""




















