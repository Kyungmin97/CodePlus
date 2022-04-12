###
"""
print("--- 1463 1로 만들기 ---")

import sys
input = sys.stdin.readline

dp = [0 for i in range(1000001)]
dp[0] = 1
dp[1] = 1
dp[2] = 2
for i in range(3, 1000001):
    dp[i] = dp[i - 1] % 1000000009 + dp[i - 2] % 1000000009 + dp[i - 3] % 1000000009

t = int(input())
for i in range(t):
    n = int(input())
    print(dp[n] % 1000000009)
"""
###
"""
print("--- 1149 RGB거리 ---")

n = int(input())
p = []
for i in range(n):
    p.append(list(map(int, input().split())))
for i in range(1, len(p)):
    p[i][0] = min(p[i - 1][1], p[i - 1][2]) + p[i][0]
    p[i][1] = min(p[i - 1][0], p[i - 1][2]) + p[i][1]
    p[i][2] = min(p[i - 1][0], p[i - 1][1]) + p[i][2]
print(min(p[n - 1][0], p[n - 1][1], p[n - 1][2]))
"""
###
"""
print("--- 1309 동물원 ---")
n = int(input())
dp = [1,3] + [0]*(n-1)
for i in range(2,n+1):
    dp[i] = (dp[i-2] + dp[i-1]*2)%9901
print(dp[n])
"""
###
"""
print("--- 11057 오르막 수 ---")
n = int(input())
s = [[0] * 10 for i in range(1001)]
for i in range(10):
    s[1][i] = 1
for i in range(2, 1001):
    for j in range(10):
        for k in range(j + 1):
            s[i][j] += s[i - 1][k]
print(sum(s[n]) % 10007)
"""
###
"""
print("--- 1932 정수 삼각형 ---")
n = int(input())
t = []
for i in range(n):
    t.append(list(map(int, input().split())))
k = 2
for i in range(1, n):
    for j in range(k):
        if j == 0:
            t[i][j] = t[i][j] + t[i - 1][j]
        elif i == j:
            t[i][j] = t[i][j] + t[i - 1][j - 1]
        else:
            t[i][j] = max(t[i - 1][j - 1], t[i - 1][j]) + t[i][j]
    k += 1
print(max(t[n - 1]))
"""
###
"""
print("--- 11055 가장 큰 증가 부분 수열 ---")
n = int(input())
t = list(map(int, input().split()))
for i in range(n):
    print(t[i])
"""

"""
import sys 
n = int(sys.stdin.readline().strip()) 
a = [int(x) for x in sys.stdin.readline().split()] 
dp = a[:] 
for i in range(n): 
  for j in range(i): 
    if a[i] > a[j]: dp[i] = max(dp[i], dp[j] + a[i]) 
print(max(dp))
"""

###
"""
print("--- 17404 RGB거리 2 ---")
INF = 2147000000
n = int(input())
rgb = []
ans = INF
for _ in range(n):
    rgb.append(list(map(int, input().split())))

for i in range(3):
    dp = [[INF, INF, INF] for _ in range(n)]
    dp[0][i] = rgb[0][i]
    for j in range(1, n):
        dp[j][0] = rgb[j][0] + min(dp[j-1][1], dp[j-1][2])
        dp[j][1] = rgb[j][1] + min(dp[j-1][0], dp[j-1][2])
        dp[j][2] = rgb[j][2] + min(dp[j-1][0], dp[j-1][1])

    for j in range(3):
        if i != j:
            ans = min(ans, dp[-1][j])
print(ans)
"""

"""
print("--- 2225 합분해 ---")
n, k = map(int, input().split())
s = [[0] * 201 for i in range(201)]
for i in range(201):
    s[i][1] = 1
for i in range(1, 201):
    for j in range(201):
        for l in range(j + 1):
            s[j][i] += s[l][i - 1]
print(s[n][k] % 1000000000)
"""

