N = int(input())
numList = []
for _ in range(N):
    numList.append(int(input()))

for i in range(1, len(numList)):
    for j in range(i, 0, -1):
        if numList[j] < numList[j-1]:
            numList[j], numList[j-1] = numList[j-1], numList[j]
        else:
            break

for num in numList:
    print(num)
