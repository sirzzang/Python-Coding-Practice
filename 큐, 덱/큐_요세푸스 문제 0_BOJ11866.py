import sys

n, k = map(int, sys.stdin.readline().split())
people = list(range(1, n+1))

idx = k-1
gap = k-1 # pop한 후에 더할 간격

print("<", end="")
while people: # 인원 수 남아 있을 때
    if n > 1: # 출력 형식을 위한 n
        print(people.pop(idx), end= ", ")
        idx = (idx + gap) % len(people)
        n -= 1 # pop했으니까 인원수 감소
    else:
        print(people.pop(), end=">")



# 문제를 잘못 이해했다.
# 맨 마지막에 남으면 순서대로 출력하는 게 아니라, 남는 애들끼리 또 진행해야 함.

# import sys

# n, k = map(int, sys.stdin.readline().split())

# people = [i for i in range(1, n+1)]

# front_index = 0
# elm_index = k-1
# elm_num = 0

# print("<", end="")
# while front_index + (k-1) < len(people):
#     elm = people[elm_index]
#     print(elm, end= ", ")
#     elm_num += 1
#     for idx in range(front_index, elm_index):
#         people.append(people[idx])
#     front_index = elm_index + 1
#     elm_index += k

# for idx in range(front_index, len(people)):
#     if idx < len(people)-1:
#         print(people[idx], end =", ")
#     else:
#         print(people[idx], end= ">")

# print(people)
# print(front_index)