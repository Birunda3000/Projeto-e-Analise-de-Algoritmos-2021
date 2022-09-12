def optroute(hoteis):
    lista_de_paradas = ( [ 0 for i in range( len(hoteis) )] )#cria um lista com len(hoteis) posições
    penalidades = ( [ 0 for i in range( len(hoteis) )] )
    for i in range( len(hoteis) ):
        penalidades[i] = ( 200 - hoteis[i] ) ** 2
        lista_de_paradas[i] = 0
        for j in range(i):            
            temp = penalidades[j] + ( (200 - (hoteis[i] - hoteis[j])) ** 2  )
            if (temp < penalidades[i]):
                penalidades[i] = temp
                lista_de_paradas[i] = (j + 1)
    caminho = []
    index = len(lista_de_paradas) - 1
    while (index >= 0):
        #caminho.appendleft(index + 1)
        aux = [index + 1]
        caminho = aux + caminho 
        index = lista_de_paradas[index] - 1   
    print('Custo minimo ', penalidades[len(hoteis) - 1])
    print('Caminho ', caminho)

n = int(input('Qual o hotel de parada: '))
hoteis = ( [ 0 for i in range( n )] )
for i in range (n):
    print('Digite a posição do hotel', i+1)
    hoteis[i] = float(input())
optroute(hoteis)