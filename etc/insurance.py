def solution(insurances):
    nb_items = len(insurances[0])
    table = [0]*len(insurances[0]) # 보장되는 항목
    selected = []

    # 과정 반복
    # TODO: 그리디식으로 선택하지 않은 항목 먼저 보장하도록.
    while sum(table) < nb_items:
        # print("현재 선택한 보험:", selected, "보장되는 항목:", table)
        insurances.sort(key=lambda x: x.count('O'))
        selected.append(insurances.pop())

        for row in range(len(selected)):
            print(selected[row])
            for col in range(len(table)):
                if table[col] == 1:
                    continue
                if selected[row][col] == 'O':
                    table[col] = 1
    return len(selected)

if __name__ == '__main__':
    print("정답:", solution(['OXOXO', 'OOOOO', 'XOXOX']))
    print("정답:", solution(['OXXO', 'XOXO', 'XXOO']))
    print("정답:", solution(['XOXO', 'OXXO', 'XXOX', 'XOOO']))


