###
"""
print("\tQuestion "+"4375")
while(True):
  try:
    n = int(input())
  except:
    break
  cnt=0
  while(True):
    cnt+=1
    value1=0
    for i in range(cnt):
      value1+=10**i
    if value1%n==0:
      break
  
  print(cnt)
  
#정답
while True:
    try:
        n = int(input())
    except:
        break
    num = 0
    i = 1
    
    while True:
        num = num*10 + 1
        num %= n
        if num == 0:
            print(i)
            break
        i+=1
"""
###
"""
print("\tQuestion "+"17427")
"""









