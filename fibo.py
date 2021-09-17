def fibo(n):
    if n == 1 :
        return 0
    if n == 2 :
        return 1
    result = fibo(n-1) + fibo(n-2)
    return result

print(fibo(5))
