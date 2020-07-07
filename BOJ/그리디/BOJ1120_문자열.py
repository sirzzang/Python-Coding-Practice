a, b = input().split()
answer = 50 # 초기값 설정

for i in range(len(b)-len(a)+1):
    flag = b[i:i+len(a)]
    print(f"======== Checking '{a}' in '{flag}' ========")
    diff_cnt = 0
    for j in range(len(flag)):
        if a[j] != flag[j]:
            diff_cnt += 1
    print(f"Different Letters Cnt : {diff_cnt}")
    if diff_cnt < answer:
        answer = diff_cnt


print(answer)