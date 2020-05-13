n = int(input())
data = []

for _ in range(n):
    x, y = map(int, input().split())
    data.append((x,y))

print(data)

for x in data:
    count = 1
    for y in data:
        if x[0] < y[0] and x[1] < y[1]:
            count += 1
    print(count)

# 틀렸다. -> ㅁㅊ;; 22125인데 22521이 나왓잖아...
# 왜? 1) 입력 형식이 잘못되었나?
# 왜? 2) 아마도 뭔가 작은 애들을 기준으로 하려고 해서 그런것 같은데

# n = int(input())
# data = []
# for _ in range(n):
#     x, y = map(int, input().split())
#     data.append((x,y))

# for x in data:                                              # 각 몸무게, 키에 대해서
#     count = 1
#     for y in data:
#         if y != x and y[0] < x[0] and y[1] < x[1]:          # 자기 자신은 제외하고, 몸무게가 작고, 키가 작은 경우에만,
#             count += 1                                      # 순위가 1씩 밀려난다.
#     print(count)




# # 그냥 하나씩 잡고 더하게 하면 되는 거 아닌가? ㅇㅋ.


# for x in data:
#     rank = 1
#     for y in data:
#         if y != x and y[0] <= x[0] and y[1] <= x[1]:
#             rank += 1
#     print(rank)


# 처음에는 정렬해서 순위 같은애들 뽑으려고 했는데 이렇게 하면 (58, 183)이 이상해진다.
# sorted_by_weight = sorted(data, key = lambda x: x[0], reverse = True)
# print(sorted_by_weight)
# sorted_by_height = sorted(data, key = lambda x: x[1], reverse = True)
# print(sorted_by_height)

# for datum in data:
#     print(sorted_by_weight.index(datum))
#     print(sorted_by_height.index(datum))

# 키, 덩치 모두 기준을 줘서 한 번씩 정렬하게 하면? -< 그래도 동일.

# sorted_by_weightheight = sorted(sorted(data, key = lambda x: x[0], reverse = True), key = lambda x: x[1], reverse = True)
# sorted_by_heightweight = sorted(sorted(data, key = lambda x: x[1], reverse = True), key = lambda x: x[0], reverse = True)
# print(sorted_by_weightheight)
# print(sorted_by_heightweight)


# 실행 결과
# [(55, 185), (58, 183), (88, 186), (60, 175), (46, 155)]
# ((88, 186), (55, 185))
# ((88, 186), (58, 183))
# ((88, 186), (60, 175))
# ((55, 185), (46, 155))
# ((58, 183), (46, 155))
# ((88, 186), (46, 155))
# ((60, 175), (46, 155))

# for x in data:
#     for y in data:
#             if y != x and y[0]> x[0] and y[1] > x[1]:
#                 print((y, x))

# 실행 결과
# (55, 185) (88, 186)
# (58, 183) (88, 186)

# for i in range(len(data)):
#     for j in range(i+1, len(data)):
#         if data[j][0]>data[i][0] and data[j][1]> data[i][1]:
#             print(data[i], data[j])



# 처음에는 정렬해서 순위 같은애들 뽑으려고 했는데 이렇게 하면 (58, 183)이 이상해진다.
# sorted_by_weight = sorted(data, key = lambda x: x[0], reverse = True)
# print(sorted_by_weight)
# sorted_by_height = sorted(data, key = lambda x: x[1], reverse = True)
# print(sorted_by_height)

# for datum in data:
#     print(sorted_by_weight.index(datum))
#     print(sorted_by_height.index(datum))