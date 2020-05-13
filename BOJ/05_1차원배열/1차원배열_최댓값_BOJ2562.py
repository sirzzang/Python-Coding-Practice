import sys

numList = [int(sys.stdin.readline()) for _ in range(9)]
print(max(numList))
print(numList.index(max(numList))+1)