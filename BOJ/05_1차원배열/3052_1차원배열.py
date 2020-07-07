import sys
s = sys.stdin

numList = []
for _ in range(10):
    numList.append(int(s.readline()))

numSet = set()
for num in numList:
    numSet.add(num%42)
print(len(numSet))