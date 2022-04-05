###
"""
print("---17413 단어 뒤집기 2---")

ans = ""
tag = False
stack = ""
for i in input():
    if i == "<":
        tag = True
        ans += stack[::-1]
        stack = ""
        ans += i
        continue
    elif i == ">":
        tag = False
        ans += i
        continue
    elif i == " ":
        ans += stack[::-1] + " "
        stack = ""
        continue
        
    if tag:
        ans += i
    else:
        stack += i
print(ans+stack[::-1])

"""

###
"""
print("---10799 쇠막대기---")

bar_razor = list(input())
answer = 0
st = []

for i in range(len(bar_razor)):
    if bar_razor[i] == '(':
        st.append('(')

    else:
        if bar_razor[i-1] == '(': 
            st.pop()
            answer += len(st)

        else:
            st.pop() 
            answer += 1 

print(answer)
"""

###
"""
print("---17298 오큰수---")

n1=int(input())
nlist1=list(map(int,input().split()))

for i in range(n1):
  for j in range(i,n1):
    x=-1
    if nlist1[j]>nlist1[i]:
      x=nlist1[j]
      break
  print(x, end=' ')
"""  

###
"""
print("---17299 오등큰수---")

n1=int(input())
nlist1=list(map(int,input().split()))
nlist2=[0 for x in range(n1)]
for i in range(n1):
  nlist2[i]=nlist1.count(nlist1[i])

for i in range(n1):
  for j in range(i,n1):
    x=-1
    if nlist2[j]>nlist2[i]:
      x=nlist1[j]
      break
  print(x, end=' ')
"""



