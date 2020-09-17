import sys

s = sys.stdin

n = int(s.readline())

scores = s.readline().split()
scores_list = [int(score) for score in scores]

M=max(scores_list)

scores_list_new = [(score/M)*100 for score in scores_list]

result = 0
for score in scores_list_new:
    result += score

avg = result/n
print(avg)

# for _ in range(n):
#     scores = s.readline().split()
#     print(scores)