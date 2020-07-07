def solution(heights):
    answer = []
    while heights:
        temp = heights.pop()
        # print(f"현재 heights: {heights}, temp: {temp}")
        if len(heights) == 0:
            # print("맨 처음")
            answer.append(0)
            break
        for i, v in enumerate(heights[::-1]):
            print(i, v)
            if v > temp:
                # print(v, "수신", len(heights)-i, "번째")
                answer.append(len(heights) - i)
                break
            if i == len(heights) - 1:
                # print("어디도 수신 못 함")
                answer.append(0)
    return answer[::-1]