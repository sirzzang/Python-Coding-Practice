# 자카드 유사도 나눗셈이 정의되지 않는 경우 있는지 확인
# 먼저 없애면 안 된다
# is.alpha()
# 중복집합 개념으로 구현해야 한다.


def solution(str1, str2):
    answer = 0
    A = [str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    B = [str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    print(A, B)
    if len(A) == 0 and len(B) == 0: # 정의되지 않는 경우
        return 65536

    # 중복집합 개념으로 구현해야 한다.
    union_, intersection_ = [], []
    while A:
        if not B: # B 안 남아 있으면
            union_.extend(A)
            break
        temp = A.pop()
        union_.append(temp) # 일단 합집합에 넣고
        if temp in B:
            B.remove(temp) # B에서 지우고
            intersection_.append(temp)
    if B: # B 남아 있으면
        union_.extend(B)
    print(f"합집합: {union_}, 교집합: {intersection_}")

    answer = int((len(intersection_) / len(union_)) * 65536)
    print(f"자카드 유사도: {answer}")

    return answer

solution("FRANCE", "french")
solution("handshake", "shake hands")
solution("aa1+aa2", "AAAA12")
solution("E=M*C^2", "e=m*c^2")
solution("----=", "123763")
solution("AABBC", "ABBDE") # 교집합[A, B, B], 합집합[AABBCDE]