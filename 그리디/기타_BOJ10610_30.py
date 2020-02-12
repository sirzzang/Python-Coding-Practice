# 시간 초과
# for, while이 너무 많다.

def digit_sum(num):
    nSum = 0
    for i in num:
        nSum += int(i)
    return nSum

def rearrange(arr):
    new_num = 0
    for i in range(len(arr)):
        new_num += arr[i]*(10**(len(arr)-i-1))
    return new_num

n = input()

digit_arr = sorted([int(x) for x in n], reverse = True)

if '0' in n and digit_sum(n) % 3 == 0:
    print(rearrange(digit_arr))

else:
    print(-1)