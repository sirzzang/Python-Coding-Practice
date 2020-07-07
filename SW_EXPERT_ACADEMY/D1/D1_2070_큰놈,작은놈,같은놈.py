n = int(input())

for i in range(n):
    x = input().split()
    if int(x[0]) < int(x[1]):
        print(f"#{i+1} <")
    elif int(x[0]) > int(x[1]):
        print(f"#{i+1} >")
    else:
        print(f"#{i+1} =")