# 1) 알고리즘 없이 풀기 : 가변변수 인자 사용
import sys
n, *x = map(int, sys.stdin.read().split())

for num in sorted(x):
    print(num)

# print(x)
# print(type(x))
# print(sorted(x))


# 2) 삽입정렬 알고리즘(list) 사용해서 풀기