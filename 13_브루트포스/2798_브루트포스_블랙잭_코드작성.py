import sys
n, m = map(int, sys.stdin.readline().split())
var = sys.stdin.readline().split()
numList = sorted([int(x) for x in var], reverse = True)

answer = []
for x in numList:
    for y in numList:
        if y != x and y <= x:
            for z in numList:
                if z != x and z != y and z <= y and x+y+z<=m:
                    answer.append(x+y+z)
print(max(answer))