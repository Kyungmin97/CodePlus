"""
print("\tQuestion "+"3085")

n = int(input())
array = []
for _ in range(n):
    array.append(list(map(str,input())))
maxCount = 0

def width():
    global  maxCount

    for i in range(n):
        countRow = 1
        for j in range(n - 1):
            if array[i][j] == array[i][j + 1]:
                countRow += 1 
                maxCount = max(maxCount,countRow) 
            else: 
                countRow = 1 
              
def height():
    global  maxCount

    for i in range(n):
        countRow = 1
        for j in range(n - 1):
            if array[j][i] == array[j+1][i]:
                countRow += 1 
                maxCount = max(maxCount,countRow) 
            else: 
                countRow = 1 
      

for i in range(n):
    for j in range(n - 1):
      if array[i][j] != array[i][j + 1]:
            array[i][j], array[i][j + 1] = array[i][j + 1], array[i][j]
            width()
            height()
            array[i][j + 1], array[i][j] = array[i][j], array[i][j + 1]
    for j in range(n - 1):
      if array[j][i] != array[j+1][i]:
            array[j][i], array[j+1][i] = array[j+1][i], array[j][i]
            width()
            height()
            array[j][i], array[j+1][i] = array[j+1][i], array[j][i]
    
print(maxCount)
"""
"""
print("\tQuestion "+"1476")

e,s,m=map(int,input().split())

cnt=0
a,b,c=0,0,0
while(True):
  cnt+=1
  a+=1
  b+=1
  c+=1
  if a>15:
    a-=15
  if b>28:
    b-=28
  if c>19:
    c-=19
  if a==e and b==s and c== m:
    break

print(cnt)
"""

print("\tQuestion "+"1107")
n = int(input())
m = int(input())
nlist=set()
if(m):
  nlist = set(input().split())
answer=abs(n-100)

for num in range(1000001):
  for i in str(num):
    if i in nlist:
      break
  else:
    answer=min(answer,abs(n-num)+len(str(num)))
      
print(answer)

