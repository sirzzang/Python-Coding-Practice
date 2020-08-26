# 맞은 풀이: 승패표 없이 구현
def solution(A, B):
    # 오름차순 정렬
    A.sort()
    B.sort()
    
    # 이길 수 있으면 다음 사람으로 넘어가기
    answer = 0
    flag = 0
    for b in range(len(B)):
        for a in range(flag, len(A)):
            if A[a] < B[b]:
                flag += 1
                answer += 1
                break
                
    return answer

# 틀린 풀이: 승패표 구현
# def solution(A, B):
#     # 오름차순 정렬
#     A.sort()
#     B.sort()
   
#     # 승패표 만들기
#     table = [[0 for row in range(len(B))] for col in range(len(A))]    
#     print(table)
#     for b in range(len(B)):
#         for a in range(len(A)):
#             if A[a] < B[b]:
#                 table[b][a] = 1
#     print(table)

#     # 승패표의 삼각행렬 부분만 검사
#     flag = 0
#     while flag < len(A):
#         if all(table[i+flag][i] == 1 for i in range(len(table)-flag)):
#             return len(A) - flag
#         else:
#             flag += 1
    
#     return 0