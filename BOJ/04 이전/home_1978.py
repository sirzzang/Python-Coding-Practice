# range 선언할 때
# int 안 붙이면 TypeError: 'float' object cannot be interpreted as an integer 나옴...


n = int(input())

primeList = []

# for _ in range(n):
#     num = int(input())
#     if num > 1:
#         for x in range(2, num//2):
#             if (num % x) == 0:
#                 pass
#             else:
#                 primeList.append(num)
#     else:
#         pass

# print(primeList)

for _ in range(n):
    num = int(input())
    if num == 1:
        pass
    elif num % 2 == 0:
        pass
    else:
        for i in range(2, num//2 + 2):
            if num % i == 0:
                pass
            else:
                primeList.append(num)

print(len(set(primeList)))
