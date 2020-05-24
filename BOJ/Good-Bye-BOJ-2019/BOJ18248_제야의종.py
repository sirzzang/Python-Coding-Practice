# n, m = map(int, input().split())
# for _ in range(n):
#     if sum(list(map(int, input().split()))) != m:
#         print("NO")
#         break
# else:
#     print("YES")

N = int(input())
for i in range(2*N-1):
    if i <= N - 1:
        print("*"*(i+1))
    else:
        print("*"*(2*N-1-i))