def fly(x, y):
    for i in range(32):
        if (y - x) == 1:
            print(1)
        elif (y - x) in range((2**i)+1, (2**(i+1))+1):
            print(i+2)
    
    return

fly(1, 5)