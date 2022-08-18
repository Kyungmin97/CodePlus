
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
