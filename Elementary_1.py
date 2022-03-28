###
"""
print("---10828 Stack---")

n=int(input())

stack=[]

while n:
  n-=1
  order=input().split()

  if order[0]=='push':
    stack.append(order[1])
  elif order[0]=='pop':
    if len(stack)==0:
      print(-1)
    else:
      print(stack.pop())
  elif order[0]=='size':
    print(len(stack))
  elif order[0]=='empty':
    if len(stack)==0:
      print(1)
    else:
      print(0)
  elif order[0]=='top':
    if len(stack)==0:
      print(-1)
    else:
      print(stack[-1])
"""
###
"""
print("---9093 Stack---")

n=int(input())

while n:
  n-=1
  order=input().split()
  for i in order:
    for j in range(len(i)-1,-1,-1):
      print(i[j],end='')
    print(end=' ')
"""

###
"""
print("---9012 Stack---")

n=int(input())

while n:
  n-=1
  cnt=0
  
  order=input()
  for i in order:
    if i == '(':
      cnt+=1
    elif i==')':
      cnt-=1
    if cnt<0:
      break

  if cnt==0:
    print("YES")
  else:
    print("NO")
"""      
###
"""
print("---1874 Stack---")

n=int(input())
stack=[]
stack.append(-1)
i=1
while n:
  n-=1
  x=int(input())
  while x!=stack[-1]:
    print("+")
    stack.append(i)
    i+=1
  print("-")
  stack.pop()
  
  

print(stack)
stack.pop()
print(stack)
"""
###
"""
print("---1406 Stack---")

stack=input()
n=int(input())
cursor=len(stack)

while n:
  n-=1
  order=input().split()
  
  if order[0]=='P':
    stack=stack[:cursor]+order[1]+stack[cursor:]
    cursor+=1

  elif order[0]=='L':
    if cursor>0:
      cursor-=1

  elif order[0]=='D':
    if cursor<len(stack):
      cursor+=1

  elif order[0]=='B':
    if cursor>0:
      stack=stack[:cursor-1]+stack[cursor:]
      cursor-=1
    else:
      stack=stack[cursor:]
    
print(stack)
"""  
###    
"""  
print("---10845 Stack---")

n=int(input())
stack=[]

while n:
  n-=1
  order=input().split()
  
  if order[0]=='push':
    stack.append(order[1])
    
  elif order[0]=='front':
    if len(stack)>0:
      print(stack[0])
    else:
      print(-1)
    
  elif order[0]=='back':
    if len(stack)>0:
      print(stack[-1])
    else:
      print(-1)
    
  elif order[0]=='size':
    print(len(stack))
    
  elif order[0]=='empty':
    if len(stack)>0:
      print(0)
    else:
      print(1)
    
  elif order[0]=='pop':
    if len(stack)>0:
      print(stack.pop(0))
    else:
      print(-1)


"""  
###    
"""
print("---1158 요세푸스 문제---")

n=list(map(int,input().split()))
stack=list(map(lambda x:x+1, range(n[0])))
num=0

print("<", end="")
while n[0]:
  n[0]-=1

  for i in range(n[1]-1):
    if num<len(stack):
      num+=1
    else:
      num=0
      if len(stack)>0:
        num=1

  print(stack.pop(num), end=", ")
  
print(">", end="")
"""
###


