user_input = input()
    
input_arr = [int(i) for i in user_input]
k = max(input_arr)

counts = [0] * (k+1)    
output_arr = [-1] * len(input_arr)

for num in input_arr:
    counts[num] += 1

for i in range(len(counts)-1):
    counts[i+1] += counts[i]

for j in range(len(input_arr)):
    output_arr[counts[input_arr[j]]-1] = input_arr[j]
    counts[input_arr[j]] -= 1

print(output_arr)

result = 0
for i in range(len(output_arr)):
    result += output_arr[i]*(10**(len(output_arr)-i-1))
print(result)



# for num in reversed()


# ##### 카운팅 정렬부터 구현하자 : SW expert academy 참고

# user_input = input()
# input_arr = [int(i) for i in user_input]

# # counts 세려면, 가장 큰 수보다 하나 많아야 한다. 01234 들어간다고 치면 5개 있어야 하니까.
# # output array는 input array와 헷갈리지 않기 위해 -1로 초기화한다.04
# k = max(input_arr)
# counts = [0] * (k+1)
# output_arr = [-1] * len(input_arr)

# # 숫자 빈도 세기
# for num in input_arr:
#     counts[num] += 1

# # 누적
# for i in range(len(counts)-1):
#     counts[i+1] += counts[i]

# # output array update
# # 1) input array를 끝에서부터 찾아가는데,
# # 2) 끝에 있는 숫자를 index로 하여, counts에서 그 위치를 찾으면,
# # 3) 그 숫자가 몇 번 나왔는지가 된다.
# # 4) 그 숫자가 3번 나왔다면, index 위치는 1씩 작아지니까
# # 5) counts에서 그 위치에 있는 숫자 1씩 빼준다.

# for j in range(len(input_arr)):
#     output_arr[counts[input_arr[j]]-1] = input_arr[j]
#     counts[input_arr[j]] -= 1





# for num in reversed()



# # 시간 초과
# # for, while이 너무 많다.

# def digit_sum(num):
#     nSum = 0
#     for i in num:
#         nSum += int(i)
#     return nSum

# def rearrange(arr):
#     new_num = 0
#     for i in range(len(arr)):
#         new_num += arr[i]*(10**(len(arr)-i-1))
#     return new_num

# n = input()

# digit_arr = sorted([int(x) for x in n], reverse = True)

# if '0' in n and digit_sum(n) % 3 == 0:
#     print(rearrange(digit_arr))

# else:
#     print(-1)



