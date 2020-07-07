# 1. 배열

# T = int(input())                                # 테스트 case 수
# for _ in range(T):                      
#     k = int(input())                            # k층
#     n = int(input())                            # n호
#     ground = [[i for i in range(1, n+1)]]       # 0층 : 1명, 2명, 3명, ..., n명
#     for i in range(1, k+1):                     # 1층부터 k층까지 구하는데,
#         floor = [1]                             # 각 층마다 1호는 항상 1명(규칙 상)
#         for j in range(2, n+1):                 # 2호부터 n호까지는
#             floor.append(sum(ground[i-1][:j]))  # 한 층 아래(i-1 접근) 그 호수까지(j) 사는 사람의 합(sum)
#         ground.append(floor)                    # 0층에서 차곡 차곡 층별로 쌓아 올라감.
#     print(ground[-1][-1])                       # 제일 마지막 원소 꺼내오면 그게 k층 n호 사람의 수.

# 2. 재귀 

dictionary = {}                # 메모 저장할 dictionary, key는 tuple로 넣을 것.

def apartment(k, n):           # 인자로 k층, n호 받는다.
    if (k, n) in dictionary:   # k층 n호 key가 있으면 그거 꺼내와라.
        return dictionary[(k,n)]
    if n == 1:
        return 1                # 1호 층 무관 1명
    elif k == 0:
        return n                # 0층 n명
    else:
        result = apartment(k-1, n) + apartment(k, n-1) # 바로 아래층 n호 + 왼쪽, 재귀 호출.
        dictionary[(k,n)] = result                     # 결과값 메모
        return result           


T = int(input())    # 테스트 케이스 개수

for _ in range(T):                  
    k = int(input())        
    n = int(input())        
    print(apartment(k,n))   # k층 n호 출력



# 런타임에러/시간초과

# def apt(k,n):
#     if n == 1:
#         return 1
#     elif k == 0:
#         return n
#     else:
#         return apt(n-1, k) + apt(n, k-1)
    
# T = int(input())
# for _ in range(T):
#     k = int(input())
#     n = int(input())
#     print(apt(k,n))