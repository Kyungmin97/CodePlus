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

print("--- 3085 사탕 게임 ---")




















