n = int(input())
real_factors = list(map(int, input().split()))
real_factors.sort()
print(real_factors[0] * real_factors[-1])