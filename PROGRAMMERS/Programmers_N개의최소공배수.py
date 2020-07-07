def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

arr = list(map(int, input().split()))

i = 1
while i < len(arr):
    arr[i] = lcm(arr[i-1], arr[i])
    i += 1

print(arr.pop())