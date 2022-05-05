"""
print("--- 11723 집합 ---")

M=int(input())

li=[input().split() for _ in range(M)]
stack=set()

for i in range(len(li)):
  if li[i][0]=='add':
    stack.add(li[i][1])
  elif li[i][0]=='remove':
    try:
      stack.discard(li[i][1])
    except:
      continue
  elif li[i][0]=='check':
    if li[i][1] in stack:
      print("1")
    else:
      print("0")
  elif li[i][0]=='toggle':
    if li[i][1] in stack:
      stack.discard(li[i][1])
    else:
      stack.add(li[i][1])
  elif li[i][0]=='all':
    stack={str(j) for j in range(1,21)}
  elif li[i][0]=='empty':
    stack=set()

"""
"""
print("--- 1182 부분수열의 합 ---")

def dfs(idx, sum):
    global cnt
    if idx >= n:
        return
    sum += li[idx]
    if sum == s:
        cnt += 1
    dfs(idx + 1, sum - li[idx])
    dfs(idx + 1, sum)
  
n, s = map(int, input().split())
li = list(map(int, input().split()))
cnt = 0
dfs(0, 0)
print(cnt)
"""










