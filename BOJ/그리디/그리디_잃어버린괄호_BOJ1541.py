# 0) 머릿속으로 생각해서 구현했는데,
# 구현하다가 생긴 문제가, +, - 각각으로 split이 안 된다.

# 1) 첫 번째 구현
# -23-70과 같이 -가 연달아 나올 경우가 안 된다.

# exp_decomposition = exp.split("-")
# print(exp_decomposition)

# sum = 0
# for ele in exp_decomposition:
#     if "+" in ele:
#         for num in ele.split("+"):
#             sum += int(num)
#     else:
#         sum -= int(ele)
# print(sum)

# 2) 이렇게 구현하면 40-23-70일 때 다 빼버린다.

# exp_decomposition = exp.split("+")
# print(exp_decomposition)

# sum = 0
# for ele in exp_decomposition:
#     if "-" in ele:
#         for num in ele.split("-"):
#             sum -= int(num)
#     else:
#         sum += int(ele)
# print(sum)

# 3) -로 나눠서 처음에 있는 것은 +해주도록 하면?
# 55-50+40과 같을 때 문제가 된다.

# exp_decomposition = exp.split("+")
# print(exp_decomposition)

# sum = 0
# for ele in exp_decomposition:
#     if "-" in ele:
#         sum += int(ele.split("-")[0])
#         for idx in range(1, len(ele.split("-"))):
#             sum -= int(ele.split("-")[idx])

#     else:
#         sum += int(ele)
# print(sum)

# 4) 오잉? 1번 경우가 맞는 것 아닌가?
# 틀렸습니다....ㅠ

# import sys

# exp = sys.stdin.readline().rstrip()

# exp_decomposition = exp.split("-")
# total = 0

# first = exp_decomposition.pop(0)
# if "+" in first:
#     for num in first.split("+"):
#         total += int(num)
# else:
#     total = int(first)

# for ele in exp_decomposition:
#     if "+" in ele:
#         print(ele)
#         for num in ele.split("+"): 
#             total -= int(num)
#     else:
#         total -= int(ele)

# print(total)


import sys

exp = sys.stdin.readline().rstrip()
exp_decomposition = exp.split("-")
total = 0
total = sum([int(i) for i in exp_decomposition[0].split("+")])


for ele in exp_decomposition[1:]:
    if "+" in ele:
        for num in ele.split("+"):
            total -= int(num)
    else:
        total -= int(ele)
print(total)


# first = exp_decomposition.pop(0)
# if "+" in first:
#     for num in first.split("+"):
#         total += int(num)
# else:
#     total = int(first)

# for ele in exp_decomposition:
#     if "+" in ele:
#         print(ele)
#         for num in ele.split("+"): 
#             total -= int(num)
#     else:
#         total -= int(ele)

# print(total)