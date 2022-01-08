import random
import math

class literal:

    def __init__(self, id):
        self.id = abs(id)
        self.signal = 1 if id > 0 else 0

    def retornar_valor(self, sol):
        return self.signal == sol[self.id-1]

class clausula:
    def __init__(self, id, literais):
        self.id = id
        self.literais = literais

    def verificar_clausula(self, sol):
        return (self.literais[0].retornar_valor(sol) or self.literais[1].retornar_valor(sol)) or self.literais[2].retornar_valor(sol)

class formula:
    def __init__(self):
        self.sol = []
        self.clausulas = []
        self.n_variaveis = 0
        self.n_clausulas = 0

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
            x1 = literal(matrix[i][0])
            x2 = literal(matrix[i][1])
            x3 = literal(matrix[i][2])
            self.clausulas.append(clausula(i , [x1,x2,x3]))
  
    def initial_sol(self):
        for _ in range(self.n_variaveis):
            self.sol.append(random.randint(0,1))

    def modify_sol_rand(self, half):
        msol = self.sol.copy()
        if half == 0:
            m = random.randint(0, self.n_variaveis/2)
            msol[m] = (msol[m] + 1) % 2
        else:
            m = random.randint(self.n_variaveis/2, self.n_variaveis-1)
            msol[m] = (msol[m] + 1) % 2

        return msol

    def conta_verdade(self, sol):
        v = 0
        for clausula in self.clausulas:
            if clausula.verificar_clausula(sol):
                v+=1
        return v
    
    def smanl(self, arquivo):

        n_iterations1 = 40
        n_iterations2 = 1000
        T = 1000
        alpha = 0.09

        self.ler_arquivo(arquivo)
        self.initial_sol()

        current_cost = self.conta_verdade(self.sol)

        for _ in range(1,n_iterations1):

            for j in range(n_iterations2):
                print(T,self.conta_verdade(self.sol))

                new_sol = self.modify_sol_rand(j%2)
                new_cost = self.conta_verdade(new_sol)

                delta = new_cost - current_cost

                if(random.random() < math.exp(delta/T)):
                    self.sol = new_sol.copy()
                    current_cost = self.conta_verdade(self.sol)


            T = T * alpha
            if T < 0.005: break

        print(self.conta_verdade(self.sol))
        print(self.sol)
            



formu = formula()
formu.smanl('sat-1.txt')
