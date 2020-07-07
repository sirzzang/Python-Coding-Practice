
def greedy(change):
    cnt = 0
    coins = [500, 100, 50, 10, 5, 1]

    # greedy하게 모든 동전에 대해서 작업 진행
    
    for coin in coins:
        cnt += change // coin
        change = change % coin

    return print(cnt)

change = 1000 - int(input())
greedy(change)






