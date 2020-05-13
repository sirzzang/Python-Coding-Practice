n = int(input())
divisors = []

# 제곱근까지만 하면 됨.
for i in range(1, int(n**0.5)+1):
    if n % i == 0:
        divisors.append(i)

# 대칭 약수 포함.
for idx in range(len(divisors)):
    divisors.append(int(n/divisors[idx]))
    divisors.sort()

for divisor in divisors:
    print(divisor, end = " ")
