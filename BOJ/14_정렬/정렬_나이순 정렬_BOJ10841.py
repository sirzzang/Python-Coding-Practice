import sys
N = int(sys.stdin.readline())
members = [sys.stdin.readline().split() for _ in range(N)]
members = sorted(members, key=lambda x : int(x[0]))
for member in members:
    print("{} {}".format(member[0], member[1]))




# 시간 초과

# 나이가 같으면 먼저 가입한 사람이 앞에 와야 하므로,
# 나이가 같은 경우(중복이 있을 때), 입력된 순서가 바뀌지 말아야 한다.
# 안정 정렬을 사용해야 한다.

# def BubbleSort(a, key):
#     for i in range(len(a)):
#         for j in range(len(a)-1):
#             if a[j][key] > a[j+1][key]:
#                 a[j], a[j+1] = a[j+1], a[j]
#     return a

# import sys

# N = int(sys.stdin.readline())

# members = [sys.stdin.readline().split() for _ in range(N)]
# for member in members:
#     member[0] = int(member[0])

# for member in BubbleSort(members, 0):
#     age = member[0]
#     name = member[1]
#     print("{} {}".format(age, name))