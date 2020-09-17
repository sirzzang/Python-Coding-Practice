def lcm(a, b):
    def gcd(a, b):
        if a > b:
            a, b = b, a
        while a > 0:
            a, b = b % a, a
        return b
    return (a*b)//gcd(a, b)

n = int(input())
rings = list(map(int, input().split()))

# 최소공배수

i = 0
while i < len(rings) - 2:
    l = lcm(rings[i], rings[i+1])
    i += 2
print(l)

# l = lcm(rings[0], rings[1])
# for i in range(2, n-1):
#     l = lcm(l, rings[i])

# 기약분수 형태로 나타내기
for i in range(1, n):
    bunja = l//rings[i]
    bunmo = l//rings[0]
    if not bunja % bunmo:
        bunja //= bunmo
        bunmo = 1
    print("{}/{}".format(bunja, bunmo))