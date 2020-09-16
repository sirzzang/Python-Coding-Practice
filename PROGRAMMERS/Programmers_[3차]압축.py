def solution(msg):
    # 압축 dict
    compress_dict = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13,
                'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}
    last_val = 26
   
    answer = []
    w_idx, c_idx = 0, 1 # w, c 슬라이싱 위한 인덱스
    while c_idx < len(msg):
        # 확인할 단어 chunk 단위
        cur = msg[w_idx:c_idx]
        nxt = msg[w_idx:c_idx+1]
        print(f"w: {w_idx}, c: {c_idx}, 현재입력: {cur}, 다음입력: {nxt}")
        
        # 다음 chunk가 사전에 있을 때는 최대한 길게
        if nxt in compress_dict:
            c_idx += 1
        
        # 사전에 추가해야 할 때
        else:
            print(f"     사전 추가: {nxt}")
            answer.append(compress_dict[cur])
            compress_dict[nxt] = last_val + 1
            last_val += 1
            w_idx = c_idx
            c_idx = w_idx + 1
   
    # 마지막에 처리되지 않은 단어 처리
    if c_idx == w_idx + 1: # 하나만 남았을 때ㅇ
        answer.append(compress_dict[msg[-1]])
    else:
        answer.append(compress_dict[nxt])

    return answer
