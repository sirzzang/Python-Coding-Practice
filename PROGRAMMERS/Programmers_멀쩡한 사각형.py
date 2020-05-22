def gcd(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a

w, h = map(int, input().split())
f = gcd(w, h)
w, h = (w//f, h//f)
answer = (w*h*f-w-h+1)*f
print(answer)