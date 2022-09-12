def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

n = int(input('Entre o valor de n (fibo(0) = 0, fibo(1) = 1, fibo(2) = 1): '))
print(fibo(n))
#fibo teste: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584