def matrix(linhas,colunas):#cria uma matrix mxn
    aux = []
    for i in range(linhas):
        aux.append([0.0] * (colunas))
    return aux

def prob(p : list, n : int, k : int):    
    dp = matrix(n+1, k+1)
    dp[0][0] = 1.0
    i=1
    while i<=n:
        j=0
        while j<=k:
            if(j == 0):
                dp[i][j] = dp[i-1][j] * (1.00 - p[i])
            else:
                dp[i][j] = dp[i-1][j] * (1-p[i]) + dp[i-1][j-1] *p[i]
            j=j+1#while
        i=i+1#while
    ans = dp[n][k]
    return ans

n = int(input('Numero de moedas: '))
k = int(input('Numero de caras que se pretende obter: '))

#n = 3#Numero de moedas
#k = 3 #Numero de caras que se pretende obter:
#p = [0.0, 0.5, 0.5, 0.5]#probabilidade de cada moeda

p = ([0.0] * (n+1))

i=1
while i <= n:
    print('Probabilidade da moeda: ', i)
    p[i] = float(input())
    i=i+1#while

print("A probabilidade de obtermos ", k," caras é: ", prob(p,n,k))