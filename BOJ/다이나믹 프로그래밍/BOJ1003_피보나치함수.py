def fibo_dp_0(n): # 0은 1, 0으로 시작하는 피보나치 수열.
    if n == 0:
        return 1
    else:
        memo = [0] * (n+1) # 메모 리스트 초기화
        memo[0] = 1
        memo[1] = 0
        for i in range(2, n+1):
            memo[i] = memo[i-1] + memo[i-2]
        print(f"0 호출 횟수 : {memo}")
        return memo[n]

def fibo_dp_1(n): # 1은 0, 1로 시작하는 피보나치 수열.
    if n == 0:
        return 0
    else:
        memo = [0] * (n+1) # 메모 리스트 초기화
        memo[0] = 0
        memo[1] = 1
        for i in range(2, n+1):
            memo[i] = memo[i-1] + memo[i-2]
        print(f"1 호출 횟수 : {memo}")
        return memo[n]


T = int(input())
for _ in range(T):
    N = int(input())
    print(f"{fibo_dp_0(N)} {fibo_dp_1(N)}")