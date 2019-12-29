# def solve(a: list) -> int
# a: 합을 구해야 하는 정수 n개가 저장되어 있는 리스트 (0 ≤ a[i] ≤ 1,000,000, 1 ≤ n ≤ 3,000,000)
# 리턴값: a에 포함되어 있는 정수 n개의 합 (정수)


n = int(input())
sum_digit = 0
numSet = set()
selfSet = set(range(1, 100))

for i in range(n, 100):
    for j in range(len(str(n))):
        sum_digit += int(str(n)[j])
        n += sum_digit
    numSet.add(n)
selfSet -= numSet
sum_digit = 0
print(selfSet)


# sum_digit = int(n[0]) + int(n[-1])


# while True:
#     if n >= 10000:
#         break
#     else:
#         n = sum_digit