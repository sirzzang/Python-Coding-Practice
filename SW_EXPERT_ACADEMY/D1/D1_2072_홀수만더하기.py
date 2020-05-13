# (n, *x) = map(int, input().split())
# print(x)

n = int(input())

for i in range(n):
    nSum = 0
    x = input().split()
    for num in x:
        if int(num) % 2 == 1:
            nSum += int(num)
    print(f"#{i+1} {nSum}")