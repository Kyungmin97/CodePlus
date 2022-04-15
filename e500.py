"""
print("--- 2309 일곱 난쟁이 ---")
nlist=[]
for _ in range(9):
  nlist.append(int(input()))
nlist.sort()
sw=True
for i in range(9):
  for j in range(i+1,9):
    if sum(nlist)-nlist[i]-nlist[j]==100:
      nlist.remove(nlist[j])
      nlist.remove(nlist[i])
      sw=False
      break
  if sw==False:
    break

for i in range(7):
  print(nlist[i])
"""

"""
print("--- 3085 사탕 게임 ---")
n=int(input())
c=[]
candy=[0,0,0,0]#CPZY
ans=0

for i in range(n):
  c.append(list(input()))

for i in range(n):
  for j in range(1,n):
    numcandy=0
    numcandy2=0
    if c[i][j]==c[i][j-1]:
      numcandy+=1
    else:
      numcandy2+=1

      
    if c[i][j]=='C':
      candy[0]+=1
    elif c[i][j]=='P':
      candy[1]+=1
    elif c[i][j]=='Z':
      candy[2]+=1
    elif c[i][j]=='Y':
      candy[3]+=1

  maxcandy=max(candy)
  ans=max(ans,maxcandy)
  candy=[0,0,0,0]
print(ans)
"""

"""
print("--- 1476 날짜 계산 ---")
nlist=list(map(int,input().split()))
cnt=1
day=[1,1,1]
while True:
  if day[0]==nlist[0] and day[1]==nlist[1] and day[2]==nlist[2]:
    break
    
  cnt+=1
  for i in range(3):
    day[i]+=1
    
  if day[0]==16:
    day[0]=1
  if day[1]==29:
    day[1]=1
  if day[2]==20:
    day[2]=1

print(cnt)
"""

"""
print("--- 1107 리모컨 ---")
enable = {str(i) for i in range(10)}  # 0, 1, 2 ... 9 (가능한 수)

# input
N = int(input())  # 이동하려고 하는 채널
M = int(input())  # 고장난 버튼의 개수
if M != 0:
    enable -= set(map(str, input().split()))  # 고장난 버튼 리스트 제거

# case1 (100번에서 +, - 로만 움직이는 경우)
min_cnt = abs(100 - N)

# case2 (1,000,000 채널까지 브루트 포스 진행)
# 500,000 채널까지 존재하기 때문에 500,000 보다 크면서 모든 숫자의 경우를 거치는 1,000,000까지를 범위로 잡음
for num in range(1000001):
    num = str(num)
    for j in range(len(num)):
        if num[j] not in enable:
            break
        elif j == len(num) - 1:
            min_cnt = min(min_cnt, abs(N - int(num)) + len(str(num)))
print(min_cnt)
"""

"""
print("--- 14500 테트로미노 ---")
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
tetromino = [
    [(0,0), (0,1), (1,0), (1,1)], # ㅁ
    [(0,0), (0,1), (0,2), (0,3)], # ㅡ
    [(0,0), (1,0), (2,0), (3,0)], # ㅣ
    [(0,0), (0,1), (0,2), (1,0)], 
    [(1,0), (1,1), (1,2), (0,2)],
    [(0,0), (1,0), (1,1), (1,2)], # ㄴ
    [(0,0), (0,1), (0,2), (1,2)], # ㄱ
    [(0,0), (1,0), (2,0), (2,1)],
    [(2,0), (2,1), (1,1), (0,1)],
    [(0,0), (0,1), (1,0), (2,0)], 
    [(0,0), (0,1), (1,1), (2,1)],
    [(0,0), (0,1), (0,2), (1,1)], # ㅜ
    [(1,0), (1,1), (1,2), (0,1)], # ㅗ
    [(0,0), (1,0), (2,0), (1,1)], # ㅏ
    [(1,0), (0,1), (1,1), (2,1)], # ㅓ
    [(1,0), (2,0), (0,1), (1,1)],
    [(0,0), (1,0), (1,1), (2,1)],
    [(1,0), (0,1), (1,1), (0,2)],
    [(0,0), (0,1), (1,1), (1,2)]
]


def find(x, y):
    global answer
    for i in range(19):
        result = 0
        for j in range(4):
            try:
                next_x = x+tetromino[i][j][0] # x 좌표
                next_y = y+tetromino[i][j][1] # y 좌표
                result += board[next_x][next_y]
            except IndexError:
                continue
        answer = max(answer, result)
        
def solve():
    for i in range (n):
        for j in range(m):
            find(i, j)
            
answer = 0
solve()
print(answer)
"""

"""
print("--- 6064 카잉 달력 ---")
def num(m, n, x, y):
    while x <= m * n:
        if (x - y) % n == 0:
            return x
        x += m
    return -1

t = int(input())
for i in range(t):
    m, n, x, y = map(int, input().split())
    print(num(m, n, x, y))
"""

"""
print("--- 9095 1, 2, 3 더하기 ---")
def sol(n):
  if n==1:
    return 1
  elif n==2:
    return 2
  elif n==3:
    return 4
  else:
    return sol(n-2)+sol(n-1)+sol(n-3)

n=int(input())
for i in range(n):
  m=int(input())
  print(sol(m))
"""























