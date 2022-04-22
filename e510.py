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

print("--- 15652 N과 M (4) ---")
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












































