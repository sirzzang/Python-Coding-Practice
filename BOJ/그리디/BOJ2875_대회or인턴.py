n, m, k = map(int, input().split())

W, M = n, m  # input women, men

if n == 0 or n == 1 or m == 0:
    print(0)

else:
    while n > 2 * m:
        n -= 1
    while n < 2 * m:
        m -= 1

    if n % 2:  # n is odd
        n -= 1

    k -= ((W - n) + (M - m))

    while k > 0:
        n -= 1
        k -= 1
        if k == 0:
            break
        n -= 1
        k -= 1
        if k == 0:
            break
        m -= 1
        k -= 1
        if k == 0:
            break

    print(min(n // 2, m))