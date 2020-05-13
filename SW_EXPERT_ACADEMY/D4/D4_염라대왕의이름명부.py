# 1.오답
# 채점용 input 파일로 채점한 결과 fail 입니다.
# (오답 : 50개의 테스트케이스 중 3개가 맞았습니다.)

import time
start = time.time()

T = int(input())

for i in range(T):
    nameSet = set()
    n = int(input())
    for _ in range(n):        
        nameSet.add(input().strip('\r'))
    print(f"#{i+1}")
    for name in sorted(list(nameSet)):
        print(name)


print("time : ", time.time()-start)