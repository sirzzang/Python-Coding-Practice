# 가변 변수 인자 사용하면?
import sys
n, *x = map(int, sys.stdin.read().split())  # 시간 줄이기 위해 x를 가변인자로 받아보자.
# readline이면 안되는데, read면 된다???
print(min(x), max(x))


# 시간이 너무 오래 걸리는데?

# n = int(input())
# user_input = input().split()
# myList = [int(x) for x in user_input]
# print(min(myList), max(myList))
