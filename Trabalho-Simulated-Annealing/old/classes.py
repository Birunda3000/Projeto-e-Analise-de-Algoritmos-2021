import random
class literal:
    def __init__(self, id, valor):
        self.id = id
        self.valor = valor
    def retornar_valor(self):#use esse metodo paa retornar o valor
        if self.id >= 0:
            return self.valor
        else:
            return not self.valor

class clausula:
    def __init__(self, id, literais):
        self.id = id
        self.literais = literais
    def verificar_clausula(self):
        return self.literais[0].retornar_valor() or self.literais[1].retornar_valor() or self.literais[2].retornar_valor()

class formula:
    def __init__(self):
        self.clausulas = []
        self.n_variaveis = 0
        self.n_clausulas = 0
        self.valores = []
    def ler_arquivo(self, nome):
        matrix = []
        aux = []
        arq = open(nome, 'r')
        for linha in arq:
            linha = linha.strip()
            linha = linha.split(" ")
            for i in range(len(linha)):
                aux.append( int( linha[i] ) )
            matrix.append(aux)
            aux = []
        
        self.n_variaveis = int(matrix[0][0])
        self.n_clausulas = int(matrix[0][1])
        matrix = matrix[1:]

        for i in range(self.n_clausulas):
            x1 = literal(matrix[i][0], True)
            x2 = literal(matrix[i][1], True)
            x3 = literal(matrix[i][2], True)
            self.clausulas.append(clausula(i , [x1,x2,x3]))
        
        self.valores = []
        for i in range(self.n_variaveis):
            self.valores.append(True)
        
    def exibir_formula(self):
        for clausula in self.clausulas:
            print(clausula.literais[0].id, clausula.literais[1].id, clausula.literais[2].id)
        print('------------------------------')
    def exibir_valores(self):
        for clausula in self.clausulas:
            print(clausula.literais[0].retornar_valor(), clausula.literais[1].retornar_valor(), clausula.literais[2].retornar_valor())
        print('------------------------------')
    def atribuir_valores_iniciais(self):
        for i in range (self.n_variaveis):
            if random.randint(0, 1) >= 1:
                self.valores[i] = True
            else:
                self.valores[i] = False
            
        self.atribuir_valores(self.valores)

    def conta_verdade(self):
        v = 0
        #print(len(self.clausulas))
        for clausula in self.clausulas:
            if clausula.verificar_clausula():
                #print('Verdade',v)
                v+=1
            else:
                pass
                #print('Falso')
        f = self.n_clausulas - v
        return v, f

    def atribuir_valores(self, vetor_valor):
        self.valores = vetor_valor
        for clausula in self.clausulas:
            clausula.literais[0].valor = vetor_valor[abs(clausula.literais[0].id)-1]
            clausula.literais[1].valor = vetor_valor[abs(clausula.literais[1].id)-1]
            clausula.literais[2].valor = vetor_valor[abs(clausula.literais[2].id)-1]
#----------------------------------------------------------------------------

#----------------------------------------------------------------------------
'''
def arrefecer(T, delta=0.99, i=1):
    #return T * (delta - (i/i*delta))
    return T * delta


def simulated_annealing(formula, T_inicial, max_ite):
    T = T_inicial
    formula.atribuir_valores_iniciais()
    aux = formula
    valor_atual = formula.conta_verdade()
    for i in range (max_ite):
        aux.atribuir_valores(nova_sol(formula.valores))
        novo_valor = aux.conta_verdade()
        delta = novo_valor - valor_atual

        if(delta >= 0):
            sol_atual = sol_nova
            val_atual = novo_val
        elif(math.exp(delta/T) > random.random()):
            sol_atual = sol_nova
            val_atual = novo_val
        T = arrefecer(T)

''' 
#---------------------------------------------------------------------------







'''formu = formula()
formu.ler_arquivo('sat-0.txt')
formu.atribuir_valores_iniciais()
formu.exibir_formula()
formu.exibir_valores()
v, f = formu.conta_verdade()
print('Verdade - ', v, ' | Falso - ', f)'''