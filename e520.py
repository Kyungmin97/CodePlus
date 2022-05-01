
"""
print("--- 10972 다음 순열 ---")
n = int(input())
data = list(map(int, input().split()))

for i in range(n-1, 0, -1): # 맨 뒤 값부터 시작
    if data[i-1] < data[i]:
        for j in range(n-1, 0, -1): # 다시 맨 뒤 값부터 큰 값찾기
            if data[i-1] < data[j]:
                data[i-1], data[j] = data[j], data[i-1] # 둘 값을 swap
                data = data[:i] + sorted(data[i:])
                for i in data:
                    print(i, end=' ')
                exit()
print(-1)
"""


print("--- 6603 로또 ---")
import sys
input = sys.stdin.readline

dp = [0 for i in range(13)]

def dfs(start, depth):
    if depth == 6:
        for i in range(6):
            print(dp[i], end=' ')
        print()
        return
    for i in range(start, len(arr)):
        dp[depth] = arr[i]
        dfs(i + 1, depth + 1)

while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    del arr[0]
    dfs(0, 0)
    print()
  