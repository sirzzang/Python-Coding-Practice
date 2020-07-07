import sys
n= int(sys.stdin.readline().strip('\n'))
cnt = 0

for num in range(1, n+1):
    if num//100 == 0: # 두 자리 수까지는 반드시 한수
        cnt+=1
    else:
        for i in range(len(str(num))-2):
            if int(str(num)[i+1])*2 == int(str(num)[i])+int(str(num)[i+2]):
                cnt+=1
print(cnt)