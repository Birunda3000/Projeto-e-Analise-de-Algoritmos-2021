import random

def verificar_clausula(x1,x2,x3):
    print(x1,x2,x3,end='')
    return x1 or x2 or x3

def sorteia_valor(n_variaveis):
    vetor_valor = []
    for i in range (n_variaveis):
        if random.randint(0, 1) >= 1:
            vetor_valor.append(True)
        else:
            vetor_valor.append(False)
            #vetor_valor.append(True)
    return vetor_valor

def conta_verdade(matrix, valores, n_clausulas, n_variaveis):
    v = 0
    for clausula in matrix:
        
        if clausula[0] > 0:
            x1 = valores[clausula[0]-1] 
        else:
            x1 = not valores[(-1*clausula[0])-1]
        
        if clausula[1] > 0: 
            x2 = valores[clausula[1]-1] 
        else:
            x2 = not valores[(-1*clausula[1])-1]
        
        if clausula[2] > 0: 
            x3 = valores[clausula[2]-1] 
        else:
            x3 = not valores[(-1*clausula[2])-1] 

        if verificar_clausula(x1, x2, x3):
            v+=1
            print(' - Verdade! ')
        else:
            print(' - Falsa ')
        
    f = n_clausulas - v
    return v, f

matrix = []

aux = []
arq = open('sat-0.txt', 'r')
for linha in arq:
    linha = linha.strip()
    linha = linha.split(" ")
    print(linha)
    for i in range(len(linha)):
        aux.append( int( linha[i] ) )
    matrix.append(aux)
    aux = []

n_variaveis = int(matrix[0][0])
n_clausulas = int(matrix[0][1])
matrix = matrix[1:]

vetor_valor = sorteia_valor(n_variaveis)

verdadeiras, falsas = conta_verdade(matrix = matrix, valores = vetor_valor, n_clausulas = n_clausulas, n_variaveis= n_variaveis)

print('Verdadeiras - ', verdadeiras, '  | Falsas - ', falsas)