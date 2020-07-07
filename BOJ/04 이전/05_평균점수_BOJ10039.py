# total_score = 0
# for _ in range(5):
#     try:
#         score = (int(input()))
#         if score < 40:
#             raise ValueError
#     except ValueError:
#         score = 40
#         total_score += score
#     else:
#         total_score += score
# print(total_score//5)

import sys
total_score = 0
for _ in range(5):
    score = int(sys.stdin.readline())
    if score < 40:
        score = 40
    total_score += score
print(total_score//5)
    
