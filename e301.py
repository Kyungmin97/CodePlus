###
"""
print("--- 9613 GCD 합 ---")

import math

num=int(input())

for _ in range(num):
  nlist=list(map(int,input().split()))
  answer=0
  for i in range(1,len(nlist)): 
    for j in range(i+1,len(nlist)): 
      answer+=math.gcd(nlist[i],nlist[j]) 
  print(answer)
"""
###
"""
print("--- 17087 숨바꼭질 6 ---")

import math 
N,S=map(int,input().split()) 
A=list(map(int,input().split())) 
ck=[] 
ans=1000000000 
for i in A: 
  ck.append(abs(i-S)) 
ans=ck[0] 
for i in range(1,N): 
  ans=math.gcd(ck[i],ans) 
print(ans)
"""
###

print("--- 1373 2진수 8진수 ---")

print(oct(int(input(),2))[2:])















