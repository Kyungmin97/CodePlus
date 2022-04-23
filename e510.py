"""
print("--- 15649 N과 M (1) ---")
n, m = map(int, input().split())

s = []
def f():
  if len(s) == m:
    print(' '.join(map(str, s)))
    return

  for i in range(1, n + 1):
    if i in s:
      continue
    s.append(i)
    f()
    s.pop()

f()
"""

"""
print("--- 15650 N과 M (2) ---")
n, m = map(int, input().split())

s = []

def f():
  if len(s) == m:
    print(' '.join(map(str, s)))
    return

  for i in range(1, n + 1):
    if i in s:
      continue
    if s:
      if i <= max(s):
        continue
    s.append(i)
    f()
    s.pop()

f()
"""

"""
print("--- 15651 N과 M (3) ---")
n, m = map(int, input().split())

s = []

def f():
  if len(s) == m:
    print(' '.join(map(str, s)))
    return

  for i in range(1, n + 1):
    s.append(i)
    f()
    s.pop()

f()
"""

"""
print("--- 15652 N과 M (4) ---")
n, m = map(int, input().split())

s = []

def f():
  if len(s) == m:
    print(' '.join(map(str, s)))
    return

  for i in range(1, n + 1):
    if s:
      if i < max(s):
        continue
    s.append(i)
    f()
    s.pop()

f()
"""

"""
print("--- 15654 N과 M (5) ---")
n, m = map(int, input().split())

s = []
s2=list(map(int, input().split()))
s2.sort()
def f():
  if len(s) == m:
    print(' '.join(map(str, s)))
    return

  for i in s2:
    if i in s:
      continue
    s.append(i)
    f()
    s.pop()

f()
"""

"""
print("--- 15655 N과 M (6) ---")
n, m = map(int, input().split())

s = []
s2=list(map(int, input().split()))
s2.sort()
def f():
  if len(s) == m:
    print(' '.join(map(str, s)))
    return

  for i in s2:
    if i in s:
      continue
    if s:
      if i < max(s):
        continue
    s.append(i)
    f()
    s.pop()

f()
"""

"""
print("--- 15656 N과 M (7) ---")
n, m = map(int, input().split())

s = []
s2=list(map(int, input().split()))
s2.sort()
def f():
  if len(s) == m:
    print(' '.join(map(str, s)))
    return

  for i in s2:
    s.append(i)
    f()
    s.pop()

f()
"""

"""
print("--- 15657 N과 M (8) ---")
n, m = map(int, input().split())

s = []
s2=list(map(int, input().split()))
s2.sort()
def f():
  if len(s) == m:
    print(' '.join(map(str, s)))
    return

  for i in s2:
    if s:
      if i < max(s):
        continue
    s.append(i)
    f()
    s.pop()

f()
"""

"""
print("--- 15663 N과 M (9) ---")
N, M = map(int, input().split())
L = list(map(int, input().split()))

L.sort()
visited = [False] * N
out = []

def solve(depth, N, M):
    if depth == M:
        print(' '.join(map(str, out)))
        return
    overlap = 0
    for i in range(N):
        if not visited[i] and overlap != L[i]:
            visited[i] = True
            out.append(L[i])
            overlap = L[i]
            solve(depth+1, N, M)
            visited[i] = False
            out.pop()

solve(0, N, M)
"""
































