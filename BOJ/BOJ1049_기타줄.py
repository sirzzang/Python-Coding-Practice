# import random
# import time
#
# # 시작 시간
# t = time.process_time()
#
# # 입력 케이스 연습용
# # n, m = map(int, input().split())
# # prices = [list(map(int, input().split())) for _ in range(m)]
#
# # 테스트 케이스 생성용
# n, m = random.randint(1, 50), random.randint(1, 100) # n이 끊어진 개수, m이 브랜드 수.
# prices = [[random.randint(0, 1000), random.randint(0, 1000)] for _ in range(m)]
#
# # 과정
# print(f"== n : {n}, m : {m} ==")
# print(f"가격 리스트\n {prices}")
# package_min, single_min = min([p[0] for p in prices]), min([p[1] for p in prices])
# print(f"패키지 최소 가격 : {package_min}, 낱개 최소 가격 : {single_min}")
#
# q, r = divmod(n, 6)
# cases = (n*single_min, q*package_min + r*single_min, (q+1)*package_min) # 전부 다 낱개로 사는 경우, 패키지와 낱개 함께 구매하는 경우, 패키지로만 구매하는 경우.
# print(f"구매 경우의 수 : {cases}")
#
# print(min(cases))
# # 끝 시간
# elapsed_time = time.process_time() - t
# print(elapsed_time)



n,m=map(int,input().split())
a,b=1000,1000
for _ in range(m):
	c,d=map(int,input().split())
	a,b=min(a,c),min(b,d)
print(f"최소 패키지 가격: {a}, 최소 낱개 가격: {b}")
print(n//6) # 내 꺼에서 q
print(min(a, b*6)) # 패키지를 사는 게 나은지, 낱개로 패키지만큼 구매하는 게 나은지
print(n%6) # 내 꺼에서 r
print(min(a, b*(n%6))) # 낱개를 낱개만큼 구매하는 게 나은지, 한 개 더 올려서 패키지를 하나 더 구매하는 게 나은지
