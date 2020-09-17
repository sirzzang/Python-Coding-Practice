# 배열 안에 배열을 만들어서 해결하자.

# k = int(input())    # k층
# n = int(input())    # n호
# ground = [[i for i in range(1, n+1)]]   # 0층에 거주하는 사람들의 수
# print(ground)
# for i in range(1, k+1):                 # 1층부터 k층까지
#     floor = [1]                         # 각 층의 1호는 항상 1명임. -> 여기다가 그 아래 층에 사는 사람 수 누적해서 더해 나갈 것.
#     for j in range(2, n+1):             # 각 층에서 2호부터 n호까지
#         floor.append(sum(ground[i-1][:j]))    # 각 호마다 그 아래층(층수 -1 로 접근), j호까지 까지 더한값을 append.
#     print(floor)
#     ground.append(floor)                # 1층부터 각 층을 더해나감.
# print(ground)                           # 배열 완성
# print(ground[-1][-1])                   # k층 n호에 사는 사람의 수는 이렇게 된다.

# 재귀로 해결하려면?
# 다 더한다고 생각하는 게 아니라,

dictionary = {}            

def apartment(k, n):           # 인자로 k층, n호 받는다.
    if (k, n) in dictionary:
        return dictionary[(k,n)]
    if n == 1:
        return 1                # 1호는 층에 관계 없이 전부 1명
    elif k == 0:
        return n                # 0층은 호수만큼 사니까 n명
    else:
        result = apartment(k-1, n) + apartment(k, n-1)
        dictionary[(k,n)] = result
        return result # 바로 아래층 n호 + 왼쪽, 재귀 호출

# 전부 다 계산할 필요 없음 -> 초기 케이스, 탈출 조건 잘 정의했기 때문에 알아서 컴퓨터가 구함.

T = int(input())    # 테스트 케이스 개수

for _ in range(T):                  
    k = int(input())        # 각 테스트케이스별로 층
    n = int(input())        # 각 테스트케이스별로 호
    print(apartment(k,n))   # k층 n호 출력해라
