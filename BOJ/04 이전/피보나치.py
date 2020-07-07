def fibonnaci(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    elif n >= 3:
        fibonacci(n) = fibonnaci(n-1) + fibonacci(n-2)
        return 
    
print(fibonacci(5))
