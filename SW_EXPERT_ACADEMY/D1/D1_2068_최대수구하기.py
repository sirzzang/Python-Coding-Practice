n = int(input())

for i in range(n):
    x = list(map(int, input().split()))
    print(f"#{i+1} {max(x)}")