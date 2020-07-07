def d(n):
    numList = list(range(1,n+1))

    digitList = []
    for num in numList:
        sum_digit = 0
        for i in str(num):
            sum_digit += int(i)
        digitList.append(sum_digit)

    resList = [numList[i] + digitList[i] for i in range(len(numList))]
    answer = sorted(set(numList)-set(resList))

    return answer

answer = d(10000)

for i in answer:
    print(i)