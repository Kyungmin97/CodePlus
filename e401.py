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














