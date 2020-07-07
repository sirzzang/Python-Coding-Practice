import sys
from collections import Counter

n = int(sys.stdin.readline())

total = 0
arr = []
for _ in range(n):
    num = int(sys.stdin.readline())
    arr.append(num)
    total += num
arr = sorted(arr)


avg = total / n
print('%.0f' %(avg))


if n == 1:
    print(arr[0])
    print(arr[0])
    print(0)

else:
    print(arr[n//2])
    counts = Counter(arr).most_common()
    if counts[1][1] == counts[0][1]:
        print(counts[1][0])
    else:
        print(counts[0][0])

    print(arr[-1]-arr[0], end = "")