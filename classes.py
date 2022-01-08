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
        
    def exibir_formula(self):
        for clausula in self.clausulas:
            print(clausula.literais[0].id, clausula.literais[1].id, clausula.literais[2].id)
    def exibir_valores(self):
        for clausula in self.clausulas:
            print(clausula.literais[0].retornar_valor(), clausula.literais[1].retornar_valor(), clausula.literais[2].retornar_valor())
    def atribuir_valores_iniciais(self):
        for clausula in self.clausulas:
            clausula.literais[0].valor = True if random.randint(0, 1) >= 1 else True
            clausula.literais[1].valor = True if random.randint(0, 1) >= 1 else True
            clausula.literais[2].valor = True if random.randint(0, 1) >= 1 else True
    
    def conta_verdade(self):
        v = 0
        print(len(self.clausulas))
        for clausula in self.clausulas:
            if clausula.verificar_clausula():
                print('Verdade',v)
                v+=1
            else:
                print('Falso')

        f = self.n_clausulas - v
        return v, f
    def atribuir_valores(self, vetor_valor):
        for clausula in self.clausulas:
            
            clausula.literais[0].valor = vetor_valor[clausula.literais[0].id]
            clausula.literais[1].valor = vetor_valor[clausula.literais[1].id]
            clausula.literais[2].valor = vetor_valor[clausula.literais[2].id]

'''formu = formula()
formu.ler_arquivo('sat-0.txt')
formu.atribuir_valores_iniciais()
formu.exibir_formula()
formu.exibir_valores()
v, f = formu.conta_verdade()
print('Verdade - ', v, ' | Falso - ', f)'''