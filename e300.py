###
"""
print("---10430 나머지---")

nlist=list(map(int,input().split()))

A=nlist[0]
B=nlist[1]
C=nlist[2]

print((A+B) % C)
print(((A%C) + (B%C)) % C)
print((A*B)%C)
print(((A%C) * (B%C)) % C)
"""
###
"""
print("--- 1934 최소공배수 ---")

def gcd(x, y):  #최대공약수 구하기
  if y == 0:
    return x
  else:
    return gcd(y, x%y)
  
def lcm(x, y):  ## 최소공배수 구하기
  result = (x*y) // gcd(x,y)
  return result

num = int(input())

for i in range(num):
  x, y = map(int, input().split(" "))
  print(lcm(x, y))
"""
###
"""
print("--- 1978 소수 찾기 ---")

n=int(input())
nlist=list(map(int,input().split()))
cnt=0

for i in nlist:
  if i > 1 :
      for j in range(2, i):  # 2부터 n-1까지
          if i % i == 0:
              cnt += 1  # 2부터 n-1까지 나눈 몫이 0이면 error가 증가
      if cnt == 0:
          cnt += 1  # error가 없으면 소수.
"""
###
"""
print("--- 1929 소수 구하기 ---")

x, y = map(int, input().split())

for i in range(x, y+1):
    if i == 1:
        continue
    for j in range(2, int(i** 0.5)+1 ):
        if i%j==0:
            break
    else:
        print(i)
"""
###
"""
print("--- 6588 골드바흐의 추측 ---")

import sys

num = 1000001
arr = [True for _ in range(num)]
for i in range(2, int((num-1)**0.5)+1):
    if arr[i]:
        for k in range(i+i, num, i):
            arr[k] = False

while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break

    flag = 0

    for a in range(3, len(arr)):
        if arr[a] and arr[n-a]:
            print(str(n) + " = " + str(a) + " + " + str(n-a))
            flag = 1
            break
    if flag == 0:
        print("Goldbach's conjecture is wrong.")
"""

###
"""
print("--- 10872 팩토리얼 ---")

n=int(input())

answer=1
for i in range(n):
  answer*=i+1

print(answer)
"""
###
"""
print("--- 1676 팩토리얼 0의 개수 ---")

n = int(input())
def five_count(n):
    cnt = 0
    while n != 0:
        n //= 5
        cnt += n
    return cnt
    
print(five_count(n))
"""
###
"""
print("--- 2004 조합 0의 개수 ---")

import sys
 
input = sys.stdin.readline
 
def count_two(x):
    cnt = 0
    while x > 0:
        x = x // 2
        cnt += x
 
    return cnt
 
def count_five(x):
    cnt = 0
    while x > 0:
        x = x // 5
        cnt += x
 
    return cnt
 
def count_zero(x, y):
    t = count_two(x) - count_two(y) - count_two(x-y)
    f = count_five(x) - count_five(y) - count_five(x-y)
 
    return min(t, f)
 
 
n, m = map(int, input().split())

print(count_zero(n, m))
"""

















