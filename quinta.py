def lista(n, arestas):
    lista = [[] for i in range(n + 1)]
    for i in range(len(arestas)):
        lista[arestas[i][0]].append(arestas[i][1])
    return lista

def dfs(node, lista_de_arestas, dp, nos_visitados):
  
    # visitado
    nos_visitados[node] = True
    
    # i = filho do node sendo visto
    for i in range(0, len( lista_de_arestas[node] )):# para cada filho do node
   
        if not nos_visitados[ lista_de_arestas[node][i] ]:
            
            #print(lista_de_arestas[node][i])
            
            dfs(lista_de_arestas[node][i], lista_de_arestas, dp, nos_visitados)
   
        dp[node] = max(dp[node], 1 + dp[ lista_de_arestas[node][i] ])# salva o maior caminho

def procurar_caminho_longo(lista_de_arestas, n):
    dp = [0] * (n + 1)
    nos_visitados = [False] * (n + 1)
    for i in range(1, n + 1):# DFS em cada vertice não visitado
        if not nos_visitados[i]:
            dfs(i, lista_de_arestas, dp, nos_visitados)
    resposta = 0
    
    #print('dp - ', dp)
   
    for i in range(1, n + 1):#achar o maior em dp
        resposta = max(resposta, dp[i])
  
    return resposta

n = int(input('Digite o numero de Arestas: '))
#arestas = [[1, 2],[1, 3],[3, 2],[2, 4],[3, 4]]
arestas = [[0, 0] for i in range(n)]

for i in range(n):
    print('Digite o vertice de origem: ', i)
    o = int(input())
    print('Digite o vertice de destino: ', i)
    d = int(input())
    arestas[i] = [o, d] 

lista_de_arestas = lista(n, arestas)
print()
print('Saida: ', procurar_caminho_longo(lista_de_arestas, n))