n = int(input())
atm_list = sorted(list(map(int, input().split())))

def atm_time(atm_list):
    
    time = 0
    
    for i in range(len(atm_list)):
        time += atm_list[i]*(n-i)
    
    return time

print(atm_time(atm_list))