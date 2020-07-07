# 총감독관 = B명 감시 가능, 1명씩만 있어야 함.
# 부감독관 = C명 감시 가능, 여러 명 있어도 됨.

# 생각을 해보면,
# 총감독관 감시 인원 + 부감독관 감시 인원이 응시생 수를 넘어야 하겠지?
# 먼저 총감독관을 배치한다 -> 감시 가능 인원만큼 뺀다 -> 빼서 //

a = int(input())
students = list(map(int, input().split()))
b, c = map(int, input().split())
cnt = a

for student in students:
    if student > b:
        if (student-b) % c == 0:
            cnt += (student-b)//c
        else:
            cnt += ((student-b)//c+1)
print(cnt)