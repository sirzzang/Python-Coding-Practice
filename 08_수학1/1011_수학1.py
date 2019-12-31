# 다시 접근하면
# 거리에 따른 이동횟수
# 1 -> 1
# 2 -> 2
# 3 -> 3
# 5 -> 4
# 7 -> 5
# 10 -> 6
# 13 -> 7
# 거리(y-x)를 d라고 하면,

d = int(input())

i = 1
checkSum = 0

while True:
    checkSum += 2*i
    i += 1
    if checkSum >= d:
        break
print(i)
print(checkSum)



# 처음에는 무조건 2의 제곱수로만 접근해서 틀렸다.

# def fly(x, y):
#     for i in range(32):
#         if (y - x) == 1:
#             print(1)
#         elif (y - x) in range((2**i)+1, (2**(i+1))+1):
#             print(i+2)
    
#     return

# fly(1, 5)