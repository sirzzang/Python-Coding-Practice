# 초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지 구하라.

# 제한사항
# prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
# prices의 길이는 2 이상 100,000 이하입니다.

# - for문 로직 많아서 통과 안 될 줄 알았는데 됐다?!
# - 자기 자신보다 뒤에 나오는 애 중에 낮은 애 있으면 기록.

prices = list(map(int, input().split()))
answer = [0]*len(prices)

for i in range(len(prices)):
    price = prices[i]
    for j in range(i+1, len(prices)):
        if prices[j] < price:
            answer[i] = j
            break

for idx, ans in enumerate(answer):
    if ans == 0:
        answer[idx] = len(answer)-1-idx
    else:
        answer[idx] = ans - idx
