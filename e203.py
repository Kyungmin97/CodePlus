###
"""
print("---1935 후위 표기식2---")

n1=int(input())
nlist1=list(input())
nlist2=[0 for x in range(n1)]
stack=[]

for i in range(n1):
    nlist2[i] = int(input())

for i in nlist1:
  if 'A' <= i <= 'Z' :
    stack.append(nlist2[ord(i)-ord('A')])
  else:
    str2 = stack.pop()
    str1 = stack.pop()

    if i =='+' :
        stack.append(str1+str2)
    elif i == '-' :
        stack.append(str1-str2)
    elif i == '*' :
        stack.append(str1*str2)
    elif i == '/' :
        stack.append(str1/str2)

print('%.2f' %stack[0])	
"""

###
"""
print("---1918 후위 표기식---")

nlist=input()
stack=[]
str1=''

for i in nlist:
  if i.isalpha():
    str1+=i
  else:
    if i == '(':
        stack.append(i)
    elif i == '*' or i =='/':
        while stack and (stack[-1]=='*' or stack[-1]=='/'):
            str1+=stack.pop()
        stack.append(i)
    elif i == '+' or i == '-':
        while stack and stack[-1] != '(':
            str1 += stack.pop()
        stack.append(i)
    elif i == ')':
        while stack and stack[-1] != '(':
            str1+=stack.pop()
        stack.pop()

             
while stack:
    str1 += stack.pop()
print(str1)
"""
###
"""
print("---10808 알파벳 개수---")

nlist=input()
nlist2=[0]*26

for i in nlist:
  nlist2[ord(i)-ord('a')]+=1

for i in nlist2:  
  print(i,end=' ')
"""
###
"""
print("---10809 알파벳 찾기---")

nlist=input()
nlist2=[-1]*26

for i in range(len(nlist)):
  if nlist2[ord(nlist[i])-ord('a')]==-1:
    nlist2[ord(nlist[i])-ord('a')]+=i+1

for i in nlist2:  
  print(i,end=' ')
"""
###
"""
print("---10820 문자열 분석---")
import sys

while True:
  line = sys.stdin.readline().rstrip('\n')

  if not line:
      break

  l, u, d, s = 0, 0, 0, 0
  for each in line:
      if each.islower():
          l += 1
      elif each.isupper():
          u += 1
      elif each.isdigit():
          d += 1
      elif each.isspace():
          s += 1

  print(l, u, d, s)
"""
###
"""
print("---10655 ROT13---")

nlist=input()
str1=''

for i in nlist:
  if i.islower():
    i=ord(i)+13
    if i>122:
      i-=26
    str1+=chr(i)
  elif i.isupper():
    i=ord(i)+13
    if i>90:
      i-=26
    str1+=chr(i)
  else:
    str1+=i
print(str1)
"""
###
"""
print("---10824 네 수---")

a, b, c, d = map(str, input().split())
e = int(a+b)
f = int(c+d)
print(e+f)
"""
###
print("---11656 접미사 배열---")

nlist=input()
nlist2=[]

for i in range(len(nlist)):
  nlist2.append(nlist[i:])

nlist2.sort()
for i in nlist2:
  print(i)






























