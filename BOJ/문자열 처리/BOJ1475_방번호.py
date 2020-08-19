# 2번째 풀이: 간결하게
N = input().replace('9', '6')
cnt = 0
for n in set(N):
    tmp = (N.count(n)+1)//2 if n =='6' else N.count(n)
    print(f"{n}: {tmp}")
    if tmp > cnt:
        cnt = tmp
print(cnt)


# import math
#
# def solution(N):
#     # N = input().replace('9', '6')
#     N = str(N).replace('9', '6')
#
#     num_dict = {}
#     for n in N:
#         if n in num_dict:
#             num_dict[n] += 1
#         else:
#             num_dict[n] = 1
#
#     num_dict = sorted(num_dict.items(), key=lambda x: x[1])
#     print(N, ":", num_dict)
#
#     if len(num_dict) == 1:
#         print(num_dict[0][1] if num_dict[-1][0] != '6' else math.ceil(num_dict[-1][1]/2))
#     else:
#         if num_dict[-1][0] == '6':
#             print(math.ceil(num_dict[-1][1] / 2) if num_dict[-1][1] / 2 > num_dict[-2][1] else num_dict[-2][1])
#         else:
#             print(num_dict[-1][1])
#     return
#
# for n in range(150):
#     solution(n)

