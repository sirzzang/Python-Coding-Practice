import sys

s = sys.stdin

c = s.readline()
scores = s.readlines()

for score in scores:    
    score_list = [int(x) for x in score[1:].split()]
    avg = sum(score_list)/len(score_list)
    nCount = 0
    for x in score_list:
        if x > avg:
            nCount += 1
    percentage = nCount/len(score_list))*100
    print()
    

# score은 string이다.

### boolean indexing list에서는 안 되나?




# scores = list(n, random.sample(range(0, 101), n))
# 점수가 주어지니까 굳이 이렇게 생성할 필요는 없다.
