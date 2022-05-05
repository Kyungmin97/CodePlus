"""
print("--- 9095 1, 2, 3 더하기 ---")

def sums(n):
    if n == 1:
        return(1)
    elif n == 2:
        return(2)
    elif n == 3:
        return(4)
    else:
        return sums(n-1) + sums(n-2) + sums(n-3)

T=int(input())

for _ in range(T):
  n=int(input())
  print(sums(n))
"""

"""
print("--- 1759 암호 만들기 ---")

xlist=[]
def dfs(start,depth,L,C):
  if depth==L:
    cnt1=0
    cnt2=0
    for i in xlist:
      for j in temp:
        if j==i:
          cnt1+=1
          break
    cnt2=L-cnt1

    if cnt1>0 and cnt2>1:
      print(''.join(xlist))
    return
  for i in range(start,C):
    xlist.append(clist[i])
    dfs(i+1,depth+1,L,C)
    xlist.pop()
  return
    
L,C=map(int,input().split())
clist=list(map(str,input().split()))
clist.sort()
temp=['a','e','i','o','u']

dfs(0,0,L,C)
"""
"""
print("--- 14501 퇴사 ---")

def consult(day, p_total):
    global answer
    # 퇴사일의 경우
    if day == N:
        answer = max(answer, p_total) # 최대이익으로 정산
        return
    t = Work[day][0] # 상담 소요일
    p = Work[day][1] # 상담 수입

    # 해당 일부터 상담하는 경우
    if t + day <= N:
        consult(t + day, p_total + p)
    # 해당 일의 다음 날부터 상담하는 경우
    consult(day + 1, p_total)

N = int(input())
Work = [list(map(int, input().split())) for _ in range(N)]
answer = 0
# 시작일 순차적으로 방문
for day in range(N):
    consult(day, 0)
print(answer)

"""

"""
print("--- 14889 스타트와 링크 ---")

def dfs(depth, idx):
    global min_diff
    if depth == n//2:
        power1, power2 = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    power1 += graph[i][j]
                elif not visited[i] and not visited[j]:
                    power2 += graph[i][j]
        min_diff = min(min_diff, abs(power1-power2))
        return

    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs(depth+1, i+1)
            visited[i] = False


n = int(input())

visited = [False for _ in range(n)]
graph = [list(map(int, input().split())) for _ in range(n)]
min_diff = int(1e9)

dfs(0, 0)
print(min_diff)
"""

print("--- 2529 부등호---")

num = int(input())
op = input().split()
check = [False] * 10
mx , mn = "",""

def poss(i,j,k): # 부등호 조건이  만족할 때만 작동
    if k == ">":
        return i>j
    else:
        return i<j


def recu(cnt, s):
    global mx,mn
  
    if cnt > num: #맨처음 나타나는 값이 최소, 마지막 저장되는 것이 최대
        if len(mn) == 0:
            mn = s
        else:
            mx = s
        return
      
    for i in range(10): #재귀 함수
        if check[i] == False:
            if cnt == 0 or poss(s[-1],str(i),op[cnt-1]):
                check[i] = True
                recu(cnt+1,s+str(i))
                check[i] = False

recu(0,"")
print(mx)
print(mn)




















