n = int(input('Entre com o numero do hotel destino:'))

a = ([0] * (n+1))#cria uma lista de n+1 0.0

a[0] = 0
i=1
while i <= n:
    print('Distancia do hotel:', i)
    a[i] = int(input())
    i=i+1#while

T = ([0] * (n+1))#cria uma lista de n+1 0.0
j=1
while j <= n:
    T[j] = ( 200 - a[j] ) ** 2 # pega valor de j   
    i=1
    while i <= j-1:
        aux = T[j]
        # min entre inicio e j ir do inicio para i + ir de i para j
        T[j] = min (  T[j]  ,  T[i] + ( 200 - ( a[j] - a[i] ) ) ** 2  )             
        i=i+1#while
    j=j+1#while
    
print(T)
print('Custo minimo ate o destino: ', T[n])