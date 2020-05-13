# 정답 인정 : 너무 하드하지 않은가?

# 하드한 방식으로 

t = int(input())

for i in range(t):

    n = (int(input())//10)*10

    var1 = n // 50000
    n = n % 50000
    var2 = n // 10000
    n = n % 10000
    var3 = n // 5000
    n = n % 5000
    var4 = n // 1000
    n = n % 1000
    var5 = n // 500
    n = n % 500
    var6 = n // 100
    n = n % 100
    var7 = n // 50
    n = n % 50
    var8 = n // 10

    print(f'#{i+1}')
    print(f'{var1} {var2} {var3} {var4} {var5} {var6} {var7} {var8}')

# 화폐 종류별로 개수를 출력해야 한다.
# 50000, 10000, 5000, 1000, 500, 100, 50, 10
# 0으로 만드는 list를 받아 놓고 바꾸면 된다

# 처음 코드 : 오답 -> 10개 중 1개 맞음.
# 입력 받는 방식 바꿔야 하지 않을까?
# 이렇게 해도 출력에 end가 있어서 출력 형식이 다를 것 같기도?

t = int(input())

for i in range(t):

    n = int(input())

    coins = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    cnts = [0]*8

    for j in range(len(coins)):
        while coins[j] <= n:
            cnts[j] = n // coins[j]
            n = n % coins[j]

    print(f'#{i+1}')
    for cnt in cnts:
        print(cnt, end = ' ')
    print()



