def troco (coin : list, v : int):   
    global dp
    if(v < 0):
        return 0
    if(v == 0):
        return 1
    if(dp[v] >= 0):
        return dp[v]
    for i in coin:
        if troco(coin, v-i):
            dp[v-i] = 1
            return dp[v-i]
    dp[v] = 0
    return dp[v]

n = int(input('Insira o tamanho do conjunto de moedas: '))

valor = int(input('Insira quantos centavos de troco queremos dar: '))

dp = [-1] * (valor+1)
coins = [0] * (n)

for i in range(n):
    print('Moeda disponivel:', i)
    coins[i] = int(input())

if(troco(coins, valor)):
    print("Podemos dar o troco")
else:
    print("Nao é possivel dar o troco")