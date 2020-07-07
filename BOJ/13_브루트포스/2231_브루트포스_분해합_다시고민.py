N = int(input())

for i in range(1, N+1):
    divide_sum = sum([int(x) for x in str(i)])
    if divide_sum + i == N:
        print(i)
        break
    elif i == N:
        print(0)
    # print(i+divide_sum, i)



#print([int(x) for i in range(1, N+1) for x in str(i)])
