'''
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.04ms, 10.2MB)
테스트 3 〉	통과 (0.04ms, 10.2MB)
테스트 4 〉	통과 (0.05ms, 10.2MB)
테스트 5 〉	통과 (0.07ms, 10.2MB)
테스트 6 〉	통과 (0.05ms, 10.2MB)
테스트 7 〉	통과 (0.04ms, 10.1MB)
테스트 8 〉	통과 (0.02ms, 10.2MB)
테스트 9 〉	통과 (0.04ms, 10.2MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
테스트 11 〉	통과 (0.06ms, 10.2MB)
테스트 12 〉	통과 (0.04ms, 10.2MB)
테스트 13 〉	통과 (0.04ms, 10.2MB)
테스트 14 〉	통과 (0.05ms, 10.1MB)
테스트 15 〉	통과 (0.07ms, 10.3MB)
테스트 16 〉	통과 (0.02ms, 10.2MB)
'''

def solution(s):
    s_list =  list('_' + s + '_')
    for i in range(1, len(s_list)):
        if s_list[i].isalpha(): # 알파벳인 경우 # 알파벳이고 뒤에 문자가 나오는 경우
            if s_list[i-1] == ' ' or s_list[i-1] == '_': # 첫 문자인 경우만 대문자로
                s_list[i] = s_list[i].upper()
            else:
                s_list[i] = s_list[i].lower()

    return ''.join(s_list[1:-1])

# 테스트
if __name__ == '__main__':
    print(solution('3people unFollowed me'))
    print(solution('for the last week'))
    print(solution('e g 3b'))
    print(solution('1111112223333'))
    print(solution('    '))
    print(solution(' A  Sdf Fft     '))


# 틀린 풀이
'''
1. 공백 여러 개 있을 때 런타임에러
2. 문제 이해 잘못함.
'''

# def lower_to_upper(word):
#     return word[0].upper() + word[1:].lower()
# def solution(s):
#     jaden_list = [lower_to_upper(w) for w in s.split()]
#     return ' '.join(jaden_list)

