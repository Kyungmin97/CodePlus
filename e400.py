###
"""
print("--- 1463 1로 만들기 ---")

n=int(input())
cnt=0
nlist=[1]
nlist2=[]
while True:
  for i in nlist:
    nlist2.append(i*3)
    nlist2.append(i*2)
    nlist2.append(i+1)
  for i in nlist2:
    if i not in nlist:
      nlist.append(i)
  cnt+=1
  
  if n in nlist:
    break

print(cnt)
"""
###
"""
print("--- 11726 2×n 타일링 ---")

n=int(input())

dp=[0]*(n+1)
dp[1]=1
if n>1:
  dp[2]=2
cnt=0
for i in range(3,n+1):
  dp[i]=dp[i-1]+dp[i-2]
print(dp[n]%10007)
"""
###
"""
print("--- 11727 2×n 타일링2 ---")

n=int(input())

dp=[0]*(n+1)
dp[1]=1
if n>1:
  dp[2]=3
cnt=0
for i in range(3,n+1):
  dp[i]=dp[i-1]+dp[i-2]*2
print(dp[n]%10007)
"""
###
"""
print("--- 9095 1, 2, 3 더하기 ---")
trynum=int(input())

for _ in range(trynum):
  n=int(input())
  dp=[0]*(11)
  dp[1]=1
  if n>1:
    dp[2]=2
  if n>2:
    dp[3]=4
  cnt=0
  for i in range(4,11):
    dp[i]=dp[i-1]+dp[i-2]+dp[n-3]
  print(dp[n])
"""
###
"""
print("--- 11052 카드 구매하기 ---")

N = int(input())
p = [0] + list(map(int,input().split()))
dp = [0 for _ in range(N+1)]

for i in range(1,N+1):
    for k in range(1,i+1):
        dp[i] = max(dp[i], dp[i-k] + p[k])
print(dp[i])
"""
###
"""
print("--- 16194 카드 구매하기2 ---")

N = int(input())
p = [0] + list(map(int,input().split()))
dp = [False for _ in range(N+1)]


for i in range(1, N+1):
    for k in range(1, i+1):
        if dp[i] == False :
            dp[i] = dp[i-k]+p[k]
        else :
            dp[i] = min(dp[i], dp[i-k]+p[k])
print(dp[N])
"""
###
"""
print("--- 15990 1, 2, 3 더하기2 ---")

import sys
input=sys.stdin.readline

tc=int(input())

dp=[[0 for _ in range(3)] for i in range(100001)]

dp[1]=[1,0,0]
dp[2]=[0,1,0]
dp[3]=[1,1,1]

print(dp)
for i in range(4,100001):
    # 6일때 만약

    # 5에서 2와 3으로 끝난거에 1 붙이기
    dp[i][0]=dp[i-1][1]%1000000009+dp[i-1][2]%1000000009
    # 4에서 1과 3으로 끝난거에 2붙이기
    dp[i][1]=dp[i-2][0]%1000000009+dp[i-2][2]%1000000009
    # 3에서 1과 2로 끝난거에 3붙이기
    dp[i][2]=dp[i-3][0]%1000000009+dp[i-3][1]%1000000009

for i in range(tc):
    n=int(input())
    print(sum(dp[n]) % 1000000009)
"""
###









































