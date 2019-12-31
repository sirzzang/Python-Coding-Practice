n = int(input())

for i in range(-n+1, n):
    a = abs(i)
    print(("*"*(2*a+1)).center(2*n).rstrip())