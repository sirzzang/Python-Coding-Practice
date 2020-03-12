# 가변인자로 받기
import sys
n, *x = map(int, sys.stdin.read().split())
print(x)
print(type(x))

for num in sorted(x, reverse = False):
    print(num)