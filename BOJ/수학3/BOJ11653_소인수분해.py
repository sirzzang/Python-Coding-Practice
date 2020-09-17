N = int(input())
factor = 2
while N > 1:
    while N % factor == 0:
        N //= factor
        print(factor)
    factor += 1