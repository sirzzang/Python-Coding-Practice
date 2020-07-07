# coin 종류가 주어진다는 것만 다르다!
# coin 종류를 입력받으면 된다.

def greedy_change(k):
    cnt = 0
    global coins

    for coin in coins:
        cnt += k // coin
        k = k % coin

    return print(cnt)

n, k = map(int, input().split())

coins = []

for _ in range(n):
    coins.append(int(input()))
    coins = sorted(coins, reverse = True)

greedy_change(k)