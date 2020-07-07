# n = input()

# sum_digit = 0
# for i in range(len(n)):
#     sum_digit += int(n[i])
#     sum_last_digit = str(sum_digit)[-1]
# n_last_digit = n[-1]
# n_new = 10*int(n_last_digit) + int(sum_last_digit)

# if n_new != int(n):
#     n = str(n_new)
#     print(n)
# else:
#     print("그만")

n = input()
n_raw = int(n)
nCount = 1

while True:

    sum_digit = 0
    for i in range(len(n)):
        sum_digit += int(n[i])
    
    sum_last_digit = str(sum_digit)[-1]
    n_last_digit = n[-1]

    n_new = 10*int(n_last_digit) + int(sum_last_digit)

    if n_new == n_raw :
        break
        
    else:
        n = str(n_new)
        nCount += 1
print(nCount)

# 이러면 26 68 84 42 26 무한루프..
# 멈추게 해야 하는데
# 어떻게 멈추게 할까

