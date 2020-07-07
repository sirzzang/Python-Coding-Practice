import sys

N, L = map(int, sys.stdin.readline().strip('\n').split())

for l in range(L, 101):
    if l==2 and N%2==1: # 만들어야 할 합이 홀수이고, l=2라면,
        print((N-1)//2, (N+1)//2)
        break
    elif N%l == 0 or N%l == (l//2):
        if (N-(l**2-l)//2)/l != (N-(l**2-l)//2)//l or (N-(l**2-l)//2)//l < 0: # 첫 번째 : `//l`로 인해 정수 처리 되는 것 방지. 두 번째 : 음수부터 시작하는 것 방지.
            continue
        print(l, [(N-(l**2-l)//2)//l + i for i in range(l)], sum([(N-(l**2-l)//2)//l + i for i in range(l)]))
        break
else:
    print(-1)

# import sys
#
# N, L = map(int, sys.stdin.readline().strip('\n').split())
#
# for l in range(L, 101):
#     if l==2 and N%2==1:
#         print((N-1)//2, (N+1)/2)
#         break
#     elif N%l == 0 or N%l == (l//2):
#         if (N-(l**2-l)//2)/l != (N-(l**2-l)//2)//l:
#             continue # 이 조건 없으면 아래 코드에서 //l이 자연스럽게 정수처리되므로 답이 달라짐.
#         print(" ".join([str((N-(l**2-l)//2)//l + i) for i in range(l)]))
#         break
# else:
#     print(-1)