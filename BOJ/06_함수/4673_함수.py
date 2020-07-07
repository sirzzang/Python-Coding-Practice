# 7) 함수로 만들면?

def selfNum(n):
    numSet = set(range(1, n+1))
    nonselfSet = set()
    for i in range(1, n+1):
        for j in str(i):
            i += int(j)
        nonselfSet.add(i)
    selfSet = numSet - nonselfSet
    
    return sorted(selfSet)    

print(selfNum(100))
print(type(selfNum(100)))



# 6) 다시 set 사용하는 방법으로 돌아가서
# 아래처럼 하면 selfnumber 출력된다.
# numSet = set(range(1, 101))
# nonselfSet = set()

# for i in range(1, 101):
#     for j in str(i):
#         i += int(j)
#     nonselfSet.add(i)
# print(nonselfSet)

# selfSet = numSet - nonselfSet
# print(sorted(selfSet))

# 5) 소수 구할 때처럼!
# 어떤 행렬 True이든 0이든 만들어놓고
# 바꾼 다음에
# index 출력하는 방식으로 가야 한다.
# 굳이 재귀하지 않아도 된다. 입력이 없다!

# def self(n):
#     return n + sum([int(i) for i in str(n)])  # n을 넣으면 n값으로 n + sum([int(i) for i in str(n)])을 return한다.

# selfList = [True] * 10000

# for i in range(10000):
#     if self(i) < 10000:
#         selfList[i] = False

# for i in range(10000):
#     if self(i) == True:
#         print(i)


# n = 123
# for i in str(n):
#     print(i)


# 4) 아래와 같이 재귀 쓰면 생성자 만드는 함수 되는데
# 생성자 만들어서 수열 쭉 쓰면 그건 이상하다.

# def recursive_self(num):
#     sum_digit = 0
#     for i in range(len(str(num))):
#         sum_digit += int(str(num)[i])
#     num += sum_digit
    
#     if num >= 300:
#         return 
#     print(num)
    
#     recursive_self(num)

# recursive_self(2)




# 3) 이렇게 가면 안 될 것 같다
# => 난리나써..

# 근데 10000보다 작은 생성자 모두 하려면...
# set으로 만들어서 빼야 하나?
# 빈 set 만들고, 1부터 시작해서 저게 되면 계속해서 add??
# 시간 존나 오래걸릴거같은디...?

# 일단 숫자 작을 때로 가정해서 print 다 해보자
# 어느 순간 자꾸 중복되면 멈추게 못하나?

# numSet = set()

# for i in range(1,100):
#     sum_digit = 0
#     while i < 10000:
#         for j in range(len(str(i))):
#             sum_digit += int(str(i)[j])
#         i += sum_digit
#         numSet.add(i)
#         sum_digit = 0
#         print(numSet)


# 2) 자리의 숫자 합 구하는 코드 반복
# 자릿수 합 구하는 코드를 계속해서 반복하는데, n이 10000보다 작을 때에만 반복

# n = int(input())
# sum_digit = 0

# while n < 10000:      

#     for i in range(len(str(n))):
#         sum_digit += int(str(n)[i])
#     n += sum_digit                                                        # indentation 주의
#     print(n)
#     sum_digit = 0
  

# 1) 일단 각 자리의 숫자 합을 구하는 것부터 작성

# n = int(input())        # 정수

# len(str(n))          # n의 자릿수

# sum_digit = 0        # 자릿수 더해나갈 초기값 설정

# for i in range(len(str(n))):        # 모든 자릿수 인덱스
#     sum_digit += int(str(n)[i])
# print(sum_digit)                    # 자릿수 합 -> 정수

# print(type(sum_digit))              

# n += sum_digit                      # n에다 자릿수 합 더함

# print(n)                            # 오키!