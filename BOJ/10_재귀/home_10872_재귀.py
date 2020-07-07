def Fibonnaci(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    elif n >= 3:
        Fibonnaci(n) = Fibonnaci(n-1) + Fibonnaci(n-2)
        return
    
Fibonnaci(5)